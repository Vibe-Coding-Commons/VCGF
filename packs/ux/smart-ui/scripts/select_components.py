#!/usr/bin/env python3
"""Backward-compatible entry point. Prefer select_smart_ui.py in v1.0.0."""
import runpy
runpy.run_path(__file__.replace('select_components.py','select_smart_ui.py'),run_name='__main__')
