# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

from vcgf_lib import *

def main():
    errors=[]; excluded={'LICENSE','VERSION'}
    for p in text_files():
        rp=rel(p)
        if rp in excluded or rp.startswith('docs/project-history/v1.0.0/source-snapshots/'): continue
        text=p.read_text(encoding='utf-8',errors='replace')
        if p.suffix=='.json':
            try: obj=load_json(p)
            except Exception as e: errors.append(f"{rp}: invalid JSON: {e}"); continue
            c=str(obj.get('$comment',''))
            if 'SPDX-FileCopyrightText: 2026 Eng. Hamada Sami' not in c or 'SPDX-License-Identifier: Apache-2.0' not in c: errors.append(f"{rp}: JSON attribution missing in $comment")
        else:
            marker='SPDX-FileCopyrightText: 2026 Eng. Hamada Sami'
            if marker not in text: errors.append(f"{rp}: missing SPDX copyright")
            if 'SPDX-License-Identifier: Apache-2.0' not in text: errors.append(f"{rp}: missing SPDX license")
            if rp.startswith('controls/') and p.name != 'README.md' and text.count(marker) != 1:
                errors.append(f"{rp}: control must contain exactly one SPDX attribution block")

    primary=['README.md','README.ar.md','AUTHORS.md','NOTICE.md','COPYRIGHT.md','CITATION.cff']
    full_signature=['Eng. Hamada Sami','+966560000934','i@hamada.io','https://www.linkedin.com/in/hamadas/','https://github.com/Vibe-Coding-Commons']
    for rp in primary:
        text=(ROOT/rp).read_text(encoding='utf-8',errors='replace')
        for value in full_signature:
            if value not in text:
                errors.append(f"{rp}: missing required public founder signature element {value}")

    fail_if(errors); print("PASS validate-attribution")
if __name__=="__main__": main()
