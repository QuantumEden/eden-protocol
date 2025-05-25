"""
Suspension Service – Eden Protocol DAO Access Enforcement

Handles suspension, reinstatement, and status queries for DAO members
based on Ritual Safeguard violations, tribunal decisions, or risk triggers.
"""

from datetime import datetime
from typing import Dict
from api.models.suspension import SuspensionRecord

# In-memory suspension registry
SUSPENDED_USERS: Dict[str, SuspensionRecord] = {}

def suspend_user(user_id: str, reason: str) -> bool:
    """
    Adds a user to the suspension list if not already suspended.
    """
    if user_id in SUSPENDED_USERS and not SUSPENDED_USERS[user_id].reinstated:
        return False

    SUSPENDED_USERS[user_id] = SuspensionRecord(
        user_id=user_id,
        reason=reason,
        timestamp=datetime.utcnow(),
        reinstated=False
    )
    return True

def reinstate_user(user_id: str) -> bool:
    """
    Reinstates a previously suspended user.
    """
    record = SUSPENDED_USERS.get(user_id)
    if not record or record.reinstated:
        return False

    record.reinstated = True
    record.reinstated_at = datetime.utcnow()
    return True

def get_suspension_status(user_id: str) -> str:
    """
    Returns the current suspension status of a user.
    """
    record = SUSPENDED_USERS.get(user_id)
    if not record:
        return "active"
    return "reinstated" if record.reinstated else "suspended"
