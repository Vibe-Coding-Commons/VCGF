# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

import hashlib
from vcgf_lib import ROOT, fail_if

APACHE_2_0_SHA256 = 'cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30'


def main():
    data=(ROOT/'LICENSE').read_bytes()
    digest=hashlib.sha256(data).hexdigest()
    errors=[]
    if digest != APACHE_2_0_SHA256:
        errors.append(f'LICENSE differs from the canonical Apache-2.0 text expected by VCGF v1.0.0: {digest}')
    fail_if(errors)
    print('PASS validate-license')

if __name__=='__main__':
    main()
