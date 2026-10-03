# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Real local TLS socket and real SQLite restore; no external provider claim."""
import hashlib,importlib.util,ipaddress,os,socketserver,sqlite3,ssl,sys,tempfile,threading,unittest
from pathlib import Path
from datetime import datetime,timedelta,timezone
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes,serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.exceptions import InvalidTag
ROOT=Path(__file__).resolve().parents[2]
def module(name,path):
    s=importlib.util.spec_from_file_location(name,ROOT/path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
backup=module('backup','examples/integrations/backup/unified.py')
mail=module('mail','examples/integrations/email/delivery.py')
queue=module('outbox','examples/integrations/email/queue.py')
operations=module('operations','examples/integrations/backup/operations.py')


class BackupTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name)
        self.app=self.root/'app';self.app.mkdir();self.rel='attachments/tenant/workspace/2026/10/03/fixture.bin'
        f=self.app/self.rel;f.parent.mkdir(parents=True);f.write_bytes(b'synthetic attachment')
        with sqlite3.connect(self.app/'app.db') as db:
            db.execute('CREATE TABLE attachments(storage_path TEXT PRIMARY KEY,checksum TEXT NOT NULL)')
            db.execute('INSERT INTO attachments VALUES (?,?)',(self.rel,hashlib.sha256(f.read_bytes()).hexdigest()))
            db.execute('CREATE TABLE business(id INTEGER PRIMARY KEY,value TEXT)');db.execute('INSERT INTO business VALUES(1,?)',('before backup',))
        self.key=os.urandom(32);self.archive=self.root/'backup.enc'
    def create(self):return backup.create(self.app,self.archive,self.key,'fixture-1','1')
    def test_real_restore_after_mutation(self):
        self.create()
        with backup.barrier(self.app),sqlite3.connect(self.app/'app.db') as db:db.execute('UPDATE business SET value=?',('after backup',))
        (self.app/self.rel).write_bytes(b'changed after backup')
        result=backup.restore(self.archive,self.root/'restored',self.key)
        self.assertEqual(result['status'],'restored_and_consistency_verified')
        with sqlite3.connect(self.root/'restored/app.db') as db:self.assertEqual(db.execute('SELECT value FROM business').fetchone()[0],'before backup')
        self.assertEqual((self.root/'restored'/self.rel).read_bytes(),b'synthetic attachment')
    def test_missing_attachment_prevents_backup(self):
        (self.app/self.rel).unlink()
        with self.assertRaises(FileNotFoundError):self.create()
        self.assertFalse(self.archive.exists())
    def test_inconsistent_attachment_prevents_backup(self):
        (self.app/self.rel).write_bytes(b'wrong')
        with self.assertRaises(ValueError):self.create()
    def test_authenticated_tamper_rejection(self):
        self.create();p=bytearray(self.archive.read_bytes());p[-1]^=1;self.archive.write_bytes(p)
        with self.assertRaises(InvalidTag):backup.restore(self.archive,self.root/'restored',self.key)
        self.assertFalse((self.root/'restored').exists())
    def test_wrong_key(self):
        self.create()
        with self.assertRaises(InvalidTag):backup.restore(self.archive,self.root/'restored',os.urandom(32))
    def test_existing_destination_never_overwritten(self):
        self.create()
        with self.assertRaises(FileExistsError):backup.restore(self.archive,self.app,self.key)
    def test_private_archive_permissions(self):
        self.create();self.assertEqual(self.archive.stat().st_mode & 0o777,0o600)
    def test_symlink_rejected(self):
        (self.app/self.rel).unlink();(self.app/self.rel).symlink_to('/etc/passwd')
        with self.assertRaises(ValueError):self.create()


class Handler(socketserver.StreamRequestHandler):
    def handle(self):
        self.request.settimeout(5);self.wfile.write(b'220 localhost sandbox\r\n')
        while True:
            line=self.rfile.readline()
            if not line:return
            verb=line.split(b' ',1)[0].strip().upper()
            if verb in [b'EHLO',b'HELO']:self.wfile.write(b'250-localhost\r\n250 8BITMIME\r\n')
            elif verb==b'DATA':
                self.wfile.write(b'354 End with dot\r\n');body=[]
                while True:
                    part=self.rfile.readline()
                    if part==b'.\r\n':break
                    if not part:return
                    body.append(part)
                self.server.received.append(b''.join(body));self.wfile.write(b'250 captured locally\r\n')
            elif verb==b'QUIT':self.wfile.write(b'221 bye\r\n');return
            else:self.wfile.write(b'250 OK\r\n')


class MailTests(unittest.TestCase):
    def test_no_plaintext_mode(self):
        with self.assertRaises(ValueError):mail.SMTPProvider('localhost',25,['sink@example.test'],tls_mode='none')
    def test_recipient_guard_before_connection(self):
        p=mail.SMTPProvider('localhost',1,['allowed@example.test'])
        with self.assertRaises(PermissionError):p.send(mail.message('from@example.test','other@example.test'))
    def test_m365_no_basic_fallback(self):
        with self.assertRaises(ValueError):mail.Microsoft365Provider(['sink@example.test']).send(mail.message('from@example.test','sink@example.test'),username='from@example.test',access_token='')
    def test_real_local_tls_delivery_ar_en(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);key=rsa.generate_private_key(public_exponent=65537,key_size=2048)
            subject=x509.Name([x509.NameAttribute(NameOID.COMMON_NAME,'localhost')]);now=datetime.now(timezone.utc)
            cert=(x509.CertificateBuilder().subject_name(subject).issuer_name(subject).public_key(key.public_key()).serial_number(x509.random_serial_number()).not_valid_before(now-timedelta(minutes=1)).not_valid_after(now+timedelta(days=1)).add_extension(x509.SubjectAlternativeName([x509.DNSName('localhost'),x509.IPAddress(ipaddress.ip_address('127.0.0.1'))]),critical=False).sign(key,hashes.SHA256()))
            (root/'cert.pem').write_bytes(cert.public_bytes(serialization.Encoding.PEM));(root/'key.pem').write_bytes(key.private_bytes(serialization.Encoding.PEM,serialization.PrivateFormat.PKCS8,serialization.NoEncryption()))
            tls=ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER);tls.load_cert_chain(root/'cert.pem',root/'key.pem')
            with socketserver.TCPServer(('127.0.0.1',0),Handler) as server:
                server.socket=tls.wrap_socket(server.socket,server_side=True);server.received=[]
                worker=threading.Thread(target=server.serve_forever,daemon=True);worker.start()
                try:
                    p=mail.SMTPProvider('localhost',server.server_address[1],['sink@example.test'],tls_mode='implicit',cafile=str(root/'cert.pem'))
                    for language in ['ar','en']:self.assertEqual(p.send(mail.message('from@example.test','sink@example.test',language))['status'],'accepted_by_smtp')
                    self.assertEqual(len(server.received),2);self.assertTrue(all(b'Content-Type: text/plain' in m for m in server.received))
                finally:server.shutdown();worker.join(timeout=5)


class OperationTests(unittest.TestCase):
    def test_queue_retry_only_explicit_temporary_refusal(self):
        import smtplib
        with tempfile.TemporaryDirectory() as d:
            out=queue.Outbox(Path(d)/'outbox.db',os.urandom(32));self.addCleanup(out.close)
            out.enqueue(mail.message('a@example.test','b@example.test'),now=0)
            def refuse(_):raise smtplib.SMTPDataError(451,b'temporary')
            self.assertEqual(out.process_one(refuse,now=0)['status'],'pending')
            self.assertEqual(out.process_one(lambda _:None,now=1)['status'],'idle')
            self.assertEqual(out.process_one(lambda _:None,now=31)['status'],'accepted_by_provider')
    def test_queue_ambiguous_timeout_needs_review(self):
        with tempfile.TemporaryDirectory() as d:
            out=queue.Outbox(Path(d)/'outbox.db',os.urandom(32));self.addCleanup(out.close)
            out.enqueue(mail.message('a@example.test','b@example.test'),now=0)
            def timeout(_):raise TimeoutError()
            self.assertEqual(out.process_one(timeout,now=0)['status'],'needs_reconciliation')
    def test_download_once_and_bound(self):
        gate=operations.DownloadGate();token=gate.issue('a'*64,'owner',lambda s,h:True,100)
        with self.assertRaises(PermissionError):gate.consume(token,'other','a'*64,101)
        self.assertTrue(gate.consume(token,'owner','a'*64,101)['authorized'])
        with self.assertRaises(PermissionError):gate.consume(token,'owner','a'*64,101)
    def test_download_without_stepup(self):
        with self.assertRaises(PermissionError):operations.DownloadGate().issue('a'*64,'owner',lambda s,h:False,100)
    def test_download_expired(self):
        gate=operations.DownloadGate();token=gate.issue('a'*64,'owner',lambda s,h:True,100,ttl=1)
        with self.assertRaises(PermissionError):gate.consume(token,'owner','a'*64,101)
    def test_recovery_requires_objectives_and_verified_backup(self):
        self.assertFalse(operations.recovery_gate('production',True,{}, {'restore_verified':False},100,50)['allowed'])
        self.assertTrue(operations.recovery_gate('production',True,{'rpo':60,'rto':120,'justification':'synthetic test only'}, {'restore_verified':True,'created_at':90},100,50)['allowed'])
    def test_schedule_and_retention(self):
        self.assertEqual(operations.schedule('daily'),'0 2 * * *')
        history=[{'backup_id':str(n),'created_at':n,'restore_verified':True,'hold':n==1} for n in range(5)]
        self.assertEqual(operations.retention_candidates(history,2,100),['2','0'])
    def test_invalid_custom_schedule(self):
        for value in ['99 2 * * *','*/0 * * * *','0 2 32 * *','0 2 * 13 *','0 2 * * 8']:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):operations.schedule('custom',value)
    def test_invalid_recovery_targets_rejected(self):
        self.assertFalse(operations.recovery_gate('production',True,{'rpo':-1,'rto':True,'justification':'invalid'}, {'restore_verified':True,'created_at':90},100,50)['allowed'])


if __name__=='__main__':unittest.main(verbosity=2)
