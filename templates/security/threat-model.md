<!--
VCGF - Vibe Coding Governance Framework
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
Author: Eng. Hamada Sami
Mobile + WhatsApp: +966560000934
Email: i@hamada.io
LinkedIn: https://www.linkedin.com/in/hamadas/
GitHub: https://github.com/Vibe-Coding-Commons
-->

# Threat Model Template

## System
Purpose:  
Trust boundaries:  
External actors:  
Sensitive assets:  

## Entry points
- web UI
- API
- webhooks
- uploads
- admin
- background jobs
- external URLs
- AI/LLM tools

## Threat record
For each threat document:
- asset
- attacker
- entry point
- scenario
- impact
- existing control
- residual risk
- test
- owner

## Minimum categories
- broken authorization
- tenant escape
- account takeover
- password recovery abuse
- injection
- XSS
- SSRF
- file upload abuse
- secret leak
- sensitive-data exposure
- key compromise
- business-logic abuse
- dependency compromise
- AI prompt/tool injection where AI is used
