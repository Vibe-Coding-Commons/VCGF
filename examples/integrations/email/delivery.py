# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Sandbox SMTP providers. Caller owns token acquisition and recipient approval."""
import base64
from email.message import EmailMessage
import smtplib
import ssl


def message(sender,recipient,locale='en',reply_to=None):
    """Non-sensitive connection-test template only; no passwords or reset tokens."""
    if locale not in ['ar','en']:raise ValueError('unsupported locale')
    m=EmailMessage();m['From']=sender;m['To']=recipient
    if reply_to:m['Reply-To']=reply_to
    m['Subject']='اختبار VCGF' if locale=='ar' else 'VCGF sandbox test'
    m.set_content('رسالة اختبار غير حساسة.' if locale=='ar' else 'Non-sensitive sandbox test message.')
    return m


class SMTPProvider:
    def __init__(self,host,port,allowed_recipients,*,tls_mode='starttls',cafile=None,timeout=15):
        if tls_mode not in ['starttls','implicit']:raise ValueError('TLS required')
        if not 0<timeout<=60:raise ValueError('bounded timeout required')
        self.host,self.port=host,port;self.allowed=set(allowed_recipients)
        if not self.allowed:raise ValueError('explicit sandbox allowlist required')
        self.mode=tls_mode;self.timeout=timeout;self.context=ssl.create_default_context(cafile=cafile)
        self.context.minimum_version=ssl.TLSVersion.TLSv1_2

    def send(self,m,*,username=None,password=None,access_token=None):
        recipients=m.get_all('To',[])
        if len(recipients)!=1 or str(recipients[0]) not in self.allowed or m.get('Cc') or m.get('Bcc'):
            raise PermissionError('recipient outside authorized sandbox')
        if access_token and password:raise ValueError('one authentication mode only')
        client=(smtplib.SMTP_SSL(self.host,self.port,timeout=self.timeout,context=self.context)
                if self.mode=='implicit' else smtplib.SMTP(self.host,self.port,timeout=self.timeout))
        with client as c:
            c.ehlo()
            if self.mode=='starttls':c.starttls(context=self.context);c.ehlo()
            if access_token:
                if not username or any(x in username+access_token for x in ['\x00','\x01','\r','\n']):raise ValueError('invalid OAuth credential')
                encoded=base64.b64encode(f'user={username}\x01auth=Bearer {access_token}\x01\x01'.encode()).decode()
                status,_=c.docmd('AUTH','XOAUTH2 '+encoded)
                if status!=235:raise PermissionError('OAuth SMTP authentication rejected')
            elif username and password:c.login(username,password)
            refused=c.send_message(m,from_addr=str(m['From']),to_addrs=[str(recipients[0])])
            if refused:raise RuntimeError('sandbox recipient refused')
        return {'status':'accepted_by_smtp','delivered_to_inbox':'Unverified','content_logged':False}


class Microsoft365Provider(SMTPProvider):
    def __init__(self,allowed_recipients,timeout=15):
        super().__init__('smtp.office365.com',587,allowed_recipients,timeout=timeout)
    def send(self,m,*,username,access_token):
        if not access_token:raise ValueError('Microsoft 365 requires OAuth token; no Basic Auth fallback')
        return super().send(m,username=username,access_token=access_token)
