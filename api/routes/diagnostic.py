"""
Diagnostic Route – Eden Protocol API

Provides endpoints for triggering session diagnostics, generating reports,
and retrieving user outcome evaluations for DAO oversight or therapist review.
"""

from fastapi import APIRouter
from src.ai.diagnostic.daemon import run_diagnostic_daemon
from src.ai.diagnostic.report_generator import generate_diagnostic_report
from src.ai.diagnostic.outcome_analyzer import analyze_user_outcome

router = APIRouter()

@router.get("/diagnostic/run/{user_id}")
async def run_diagnostics(user_id: str):
    """
    Executes the full diagnostic sweep for a user.
    """
    flags = run_diagnostic_daemon(user_id)
    return {"user_id": user_id, "flags": flags}

@router.get("/diagnostic/report/{user_id}/{session_id}")
async def get_diagnostic_report(user_id: str, session_id: str):
    """
    Retrieves a symbolic diagnostic report for a specific session.
    """
    report = generate_diagnostic_report(user_id, session_id)
    return report

@router.get("/diagnostic/outcome/{user_id}")
async def evaluate_outcome(user_id: str):
    """
    Returns a symbolic transformation outcome for the user.
    """
    outcome = analyze_user_outcome(user_id)
    return outcome
