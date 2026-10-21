# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Chromium checks for a synthetic static reference, not target-product acceptance."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--output', required=True)
p.add_argument('--browser', default='/usr/bin/chromium')
a = p.parse_args()
out = Path(a.output); out.mkdir(parents=True, exist_ok=True)
checks, errors, requests = [], [], []

def check(name, passed):
    checks.append({'name': name, 'passed': bool(passed)})

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True, executable_path=a.browser,
                                args=['--no-sandbox', '--disable-dev-shm-usage'])
    version = browser.version
    for width in [320, 390, 768, 1280, 1440, 1920]:
        for language in ['ar', 'en']:
            ctx = browser.new_context(viewport={'width': width, 'height': 1000})
            page = ctx.new_page()
            page.on('pageerror', lambda error: errors.append(str(error)))
            page.on('request', lambda request: requests.append(request.url))
            page.set_content((ROOT/'examples/adaptive/rtl-ltr-crm.html').read_text(encoding='utf-8'))
            if language == 'en': page.locator('#langToggle').click()
            label = f'{language}-{width}'
            check(label+'-direction', page.locator('html').get_attribute('dir') == ('rtl' if language=='ar' else 'ltr'))
            check(label+'-no-root-overflow', page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'))
            check(label+'-one-visible-view', page.locator('.table-wrap').is_visible() != page.locator('.mobile-cards').is_visible())
            check(label+'-appropriate-view', page.locator('.table-wrap').is_visible() == (width>860))
            prefix = '.table-wrap' if width>860 else '.mobile-cards'
            check(label+'-four-records', page.locator(prefix+' button[data-id]').count()==4)
            details = page.locator(prefix+' details').first
            details.locator('summary').focus(); page.keyboard.press('Enter')
            check(label+'-keyboard-details', details.get_attribute('open') is not None)
            action = page.locator(prefix+' button[data-id]').first
            action.focus(); page.keyboard.press('Enter')
            check(label+'-focus-retained', page.evaluate("document.activeElement.dataset.id === 'CRM-1042'"))
            check(label+'-details-retained', details.get_attribute('open') is not None)
            check(label+'-live-action-announcement', bool(page.locator('#actionStatus').text_content().strip()))
            check(label+'-calendar-preserved', '2026' in page.locator(prefix+' .date').first.text_content())
            check(label+'-isolated-identifiers', page.locator(prefix+' .id').first.evaluate("x=>getComputedStyle(x).direction==='ltr' && getComputedStyle(x).unicodeBidi==='isolate'"))
            page.locator('#searchInput').fill('CRM-1043')
            check(label+'-search', page.locator(prefix+' button[data-id]').count()==1)
            page.locator('#searchInput').fill('nonexistent-record-xyz')
            check(label+'-empty-state', page.locator(prefix+' button[data-id]').count()==0 and bool(page.locator(prefix).text_content().strip()))
            page.locator('#searchInput').fill('')
            page.evaluate("document.documentElement.style.fontSize='32px'")
            check(label+'-200-percent-text-root-reflow', page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'))
            page.evaluate("document.documentElement.style.fontSize=''")
            if width in [390,1440]: page.screenshot(path=str(out/f'crm-{label}.png'), full_page=True)
            ctx.close()
    ctx=browser.new_context(viewport={'width':1440,'height':900});page=ctx.new_page()
    page.set_content((ROOT/'examples/adaptive/rtl-ltr-crm.html').read_text(encoding='utf-8'))
    page.evaluate("records[0].ar='<img src=x onerror=window.xssFlag=true>';render()")
    check('record-content-escaped', page.locator('tbody img').count()==0 and page.evaluate('window.xssFlag!==true'))
    ctx.close();browser.close()
check('no-page-javascript-errors', not errors)
check('no-external-requests', not requests)
report={'observed_at':datetime.now(timezone.utc).isoformat(), 'scope':'synthetic_static_html_chromium_only',
        'browser':version, 'checks':checks, 'passed':sum(x['passed'] for x in checks),
        'failed':sum(not x['passed'] for x in checks), 'page_errors':errors,
        'network_requests':requests,
        'limitations':['No real Laravel/React/Vue application tested','No Firefox/WebKit or physical mobile device tested',
                       'No manual screen-reader or WCAG conformance claim','200% text sizing is not full browser zoom certification',
                       'Uses system fonts; local font binaries and shaping not verified']}
(out/'browser-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'passed':report['passed'],'failed':report['failed'],'scope':report['scope']}))
raise SystemExit(1 if report['failed'] else 0)
