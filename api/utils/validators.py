# api/utils/validators.py
# Eden Protocol – Custom Field Validators

from fastapi import HTTPException


VALID_ELEMENTS = {"Fire", "Water", "Air", "Earth", "Void"}
VALID_ARCHETYPES = {"Visionary", "Guardian", "Rebel", "Scholar", "Oracle"}
VALID_PATHS = {"Transhumanism", "Technognostic", "Animist", "Ascetic", "Voidborne"}


def validate_element(value: str):
    if value not in VALID_ELEMENTS:
        raise HTTPException(status_code=400, detail=f"Invalid element: {value}")


def validate_archetype(value: str):
    if value not in VALID_ARCHETYPES:
        raise HTTPException(status_code=400, detail=f"Invalid archetype: {value}")


def validate_sacred_path(value: str):
    if value not in VALID_PATHS:
        raise HTTPException(status_code=400, detail=f"Invalid sacred path: {value}")
