# src/ai/council/registry.py

"""
Council Registry – Voice Index for Eden Protocol

Maps available therapeutic and psychoanalytic perspectives to their
interpretation functions. Used by Eidelon to summon insights from
various modalities as facets of a unified internal council.
"""

from .cbt import interpret as cbt_perspective
from .dbt import interpret as dbt_perspective
from .jungian import interpret as jung_perspective
from .logotherapy import interpret as logotherapy_perspective
from .freudian import interpret as freudian_perspective
from .psychiatrist import triage as psychiatrist_overview  # meta-perspective

COUNCIL_REGISTRY = {
    "CBT": cbt_perspective,
    "DBT": dbt_perspective,
    "Jung": jung_perspective,
    "Logotherapy": logotherapy_perspective,
    "Freud": freudian_perspective,
    "Psychiatrist": psychiatrist_overview
}
