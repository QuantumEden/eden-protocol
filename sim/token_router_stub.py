# sim/token_router_stub.py
# Simulation stub for EdenQuest payload injection

from datetime import datetime

def inject_soulform_payload(user_id: str, soulform_data: dict) -> dict:
    """
    Simulates injecting a soulform payload into a user's token stream.
    For use in integration tests and isolated payload simulations.

    Args:
        user_id (str): The user’s identifier
        soulform_data (dict): Dictionary containing soulform metadata

    Returns:
        dict: Simulated success payload
    """
    return {
        "user_id": user_id,
        "soulform": soulform_data,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "success": True,
        "status": "🧬 Soulform payload injected successfully (stub)."
    }
