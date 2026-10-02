# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

from vcgf_lib import ROOT, fail_if

PLATFORMS=['generic','lovable','claude','bolt','v0','replit','cursor']

def main():
    errors=[]
    required=[ROOT/'README.md', ROOT/'README.ar.md', ROOT/'docs/user-guide.md', ROOT/'docs/platform-guides/README.md']
    required += [ROOT/f'docs/platform-guides/{p}.md' for p in PLATFORMS]
    for p in required:
        if not p.is_file(): errors.append(f'missing documentation file {p.relative_to(ROOT)}')
    if errors: fail_if(errors)

    en=(ROOT/'README.md').read_text(encoding='utf-8')
    ar=(ROOT/'README.ar.md').read_text(encoding='utf-8')
    en_required=['# What is VCGF?','# Why does VCGF exist?','# What changes when you use VCGF?','# 5-minute quick start','# Supported AI coding platforms','# Install VCGF','# What does VCGF include?','# Practical examples','# How do I know VCGF is active?','# Do I need to be a programmer?','# What VCGF does not do','# What results should you expect?']
    ar_required=['# ما هو VCGF؟','# لماذا تم إنشاء VCGF؟','# ماذا يتغير عند استخدام VCGF؟','# البدء خلال 5 دقائق','# منصات AI Coding المدعومة','# تثبيت VCGF','# ماذا يحتوي VCGF؟','# أمثلة عملية','# كيف أعرف أن VCGF فعال؟','# هل يجب أن أكون مبرمجًا؟','# ما الذي لا يفعله VCGF؟','# ما النتائج المتوقعة؟']
    for s in en_required:
        if s not in en: errors.append(f'README.md missing required onboarding section: {s}')
    for s in ar_required:
        if s not in ar: errors.append(f'README.ar.md missing required onboarding section: {s}')
    if 'README.ar.md' not in en: errors.append('README.md missing Arabic documentation link')
    if 'README.md' not in ar: errors.append('README.ar.md missing English documentation link')
    for p in PLATFORMS:
        guide=(ROOT/f'docs/platform-guides/{p}.md').read_text(encoding='utf-8')
        for section in ['## Who this guide is for','## What you need','## Files used by this adapter','## Step 1 — Download VCGF','## Step 8 — Initialize VCGF','## Step 9 — Verify VCGF is active','## How approvals work','## How to collect evidence','## Troubleshooting','## Platform limitations']:
            if section not in guide: errors.append(f'{p} guide missing section: {section}')
        pread=(ROOT/f'platforms/{p}/README.md').read_text(encoding='utf-8')
        expected=f'../../docs/platform-guides/{p}.md'
        if expected not in pread: errors.append(f'platforms/{p}/README.md does not link to full platform guide')
        if f'docs/platform-guides/{p}.md' not in en: errors.append(f'README.md missing platform guide link for {p}')
        if f'docs/platform-guides/{p}.md' not in ar: errors.append(f'README.ar.md missing platform guide link for {p}')
    if '1.0.0' not in en or '1.0.0' not in ar: errors.append('README version missing/inconsistent')
    fail_if(errors)
    print('PASS validate-documentation')

if __name__=='__main__': main()
