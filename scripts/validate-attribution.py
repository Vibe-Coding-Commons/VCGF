# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

from vcgf_lib import *

SPDX_COPYRIGHT='SPDX-FileCopyrightText: 2026 Eng. Hamada Sami'
SPDX_LICENSE='SPDX-License-Identifier: Apache-2.0'
PACKAGE_ATTRIBUTION_SCOPES={
    'packs/ux/smart-ui/': 'packs/ux/SMART-UI-ATTRIBUTION.md',
}

def package_scope_for(rp):
    for prefix, attribution in PACKAGE_ATTRIBUTION_SCOPES.items():
        if rp.startswith(prefix):
            return attribution
    return None

def main():
    errors=[]; excluded={'LICENSE','VERSION'}
    checked_package_attribution={}
    for p in text_files():
        rp=rel(p)
        if rp in excluded or rp.startswith('docs/project-history/v1.0.0/source-snapshots/'):
            continue

        package_attribution=package_scope_for(rp)
        if package_attribution:
            if package_attribution not in checked_package_attribution:
                ap=ROOT/package_attribution
                if not ap.is_file():
                    checked_package_attribution[package_attribution]=False
                    errors.append(f"{rp}: package attribution file missing: {package_attribution}")
                else:
                    at=ap.read_text(encoding='utf-8',errors='replace')
                    ok=SPDX_COPYRIGHT in at and SPDX_LICENSE in at
                    checked_package_attribution[package_attribution]=ok
                    if not ok:
                        errors.append(f"{package_attribution}: package attribution missing required SPDX markers")
            # Frozen package files are covered by the explicit repository-level
            # attribution bridge; their bytes must remain unchanged for package integrity.
            continue

        text=p.read_text(encoding='utf-8',errors='replace')
        if p.suffix=='.json':
            try:
                obj=load_json(p)
            except Exception as e:
                errors.append(f"{rp}: invalid JSON: {e}"); continue
            if not isinstance(obj,dict):
                errors.append(f"{rp}: top-level JSON must be an object unless covered by an explicit package attribution scope")
                continue
            c=str(obj.get('$comment',''))
            if SPDX_COPYRIGHT not in c or SPDX_LICENSE not in c:
                errors.append(f"{rp}: JSON attribution missing in $comment")
        else:
            if SPDX_COPYRIGHT not in text: errors.append(f"{rp}: missing SPDX copyright")
            if SPDX_LICENSE not in text: errors.append(f"{rp}: missing SPDX license")
            if rp.startswith('controls/') and p.name != 'README.md' and text.count(SPDX_COPYRIGHT) != 1:
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
