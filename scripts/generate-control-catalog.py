# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
# VCGF — Vibe Coding Governance Framework
# Founder & Maintainer: Eng. Hamada Sami
# Email: i@hamada.io
# GitHub: https://github.com/Vibe-Coding-Commons

import yaml
from vcgf_lib import *

def main():
    rows=[]
    for p in control_files():
        meta,_=parse_frontmatter(p)
        rows.append({'id':meta['id'],'domain':meta['domain'],'title':meta['title'],'status':meta['status'],'requirement_level':meta['requirement_level'],'framework_version_introduced':meta['framework_version_introduced'],'profiles':meta['profiles'],'path':rel(p)})
    rows.sort(key=lambda x:x['id'])
    header="# VCGF — Vibe Coding Governance Framework\n# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami\n# SPDX-License-Identifier: Apache-2.0\n# Founder & Maintainer: Eng. Hamada Sami\n# Email: i@hamada.io\n# GitHub: https://github.com/Vibe-Coding-Commons\n# AUTO-GENERATED — DO NOT EDIT MANUALLY\n\n"
    out={'catalog_version':'1.0.0','framework_version':'1.0.0','source':'Control Markdown front matter','control_count':len(rows),'controls':rows}
    (ROOT/'spec/control-catalog.yaml').write_text(header+yaml.safe_dump(out,sort_keys=False,allow_unicode=True),encoding='utf-8')
    print(f"generated control catalog: {len(rows)}")
if __name__=='__main__': main()
