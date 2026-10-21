# SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
# SPDX-License-Identifier: Apache-2.0
"""Explainable ranking over explicitly classified goals, audiences and tasks.

This is not natural-language inference. Goal classifications must be reviewed by
an owner/researcher; raw prose, including injected instructions, is never executed.
"""
from __future__ import annotations

RTL_SCRIPTS = {'Arab', 'Hebr', 'Thaa', 'Nkoo', 'Adlm', 'Rohg', 'Syrc', 'Samr', 'Mand'}
LTR_SCRIPTS = {'Latn', 'Cyrl', 'Grek', 'Deva', 'Hans', 'Hant', 'Jpan', 'Kore', 'Beng', 'Thai', 'Ethi', 'Geor', 'Armn'}
RTL_LANGUAGES = {'ar', 'he', 'fa', 'ur', 'ps', 'sd', 'dv', 'yi'}
LTR_LANGUAGES = {'en', 'fr', 'de', 'es', 'it', 'pt', 'nl', 'tr', 'az', 'id', 'ms', 'vi', 'pl', 'cs', 'ru', 'uk', 'el', 'hi', 'bn', 'th', 'zh', 'ja', 'ko', 'sv', 'da', 'no', 'fi', 'sw'}


def locale_direction(locale: str) -> str | None:
    parts = locale.replace('_', '-').split('-')
    script = next((p.title() for p in parts[1:] if len(p) == 4 and p.isalpha()), None)
    if script:
        return 'rtl' if script in RTL_SCRIPTS else 'ltr' if script in LTR_SCRIPTS else None
    language = parts[0].lower()
    return 'rtl' if language in RTL_LANGUAGES else 'ltr' if language in LTR_LANGUAGES else None


def rank_schools(discovery: dict, catalog: dict) -> list[dict]:
    schools = {v['school']: {'school': v['school'], 'score': 0, 'contributions': []}
               for v in catalog['design_schools'].values() if v['school'] != 'undetermined'}

    def add(school: str, points: int, reason: str) -> None:
        schools[school]['score'] += points
        schools[school]['contributions'].append(f'{points:+d}: {reason}')

    default = catalog['design_schools'][discovery['product_type']]['school']
    if default in schools:
        add(default, 1, 'Weak product-category prior; never decisive by itself')
    outcomes = {
        'efficiency': [('task_first_enterprise', 3)],
        'comprehension': [('editorial_brand', 3), ('service_journey', 1)],
        'conversion': [('conversion', 3)],
        'learning': [('learning_progress', 3)],
        'situational_awareness': [('operations_command', 3)],
        'guided_completion': [('service_journey', 3)],
    }
    for goal in discovery.get('goal_priorities', []):
        for school, strength in outcomes[goal['outcome']]:
            add(school, strength * goal['weight'], f'Classified goal[{goal["goal_index"]}]={goal["outcome"]}')
    interactions = {
        'read': 'editorial_brand', 'browse': 'conversion', 'form': 'service_journey',
        'approval': 'task_first_enterprise', 'monitor': 'operations_command', 'kiosk_action': 'touch_kiosk'
    }
    actors = {a['id']: a for a in discovery['audiences']}
    for task in discovery['workflows']:
        school = interactions.get(task['interaction'])
        if school:
            weight = {'routine': 3, 'occasional': 2, 'one_off': 1, 'unknown': 1}[task['frequency']]
            add(school, 2 * weight, 'Workflow ' + task['id'] + ': ' + task['interaction'])
        proficiency = actors.get(task['actor_id'], {}).get('proficiency')
        if proficiency == 'novice':
            add('service_journey', 2, 'Novice actor in workflow ' + task['id'])
        elif proficiency == 'expert' and task['interaction'] in {'approval', 'monitor', 'browse'}:
            add('task_first_enterprise', 2, 'Expert repetitive-task context ' + task['id'])
    if 'kiosk' not in discovery['devices']['supported']:
        add('touch_kiosk', -100, 'No kiosk target; do not select a kiosk school')
    if not discovery['workflows'] and not discovery.get('goal_priorities') and default == 'undetermined':
        return [{'school': 'undetermined', 'score': 0, 'contributions': ['No usable discovery evidence']}]
    return sorted(schools.values(), key=lambda r: (-r['score'], r['school']))
