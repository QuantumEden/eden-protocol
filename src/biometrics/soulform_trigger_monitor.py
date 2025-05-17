# soulform_trigger_monitor.py – Eden Protocol Biometrics
# Monitors real-world behavioral data to nudge soulform eligibility

from datetime import datetime
from typing import Dict, Any

# Thresholds required for nudging toward soulform activation
SOULFORM_CONDITIONS = {
    "sobriety_days": 30,
    "daily_journals": 20,
    "mindful_sessions": 15
}

def check_soulform_readiness(biometrics: Dict[str, Any]) -> Dict[str, Any]:
    """
    Analyzes biometric self-reporting or tracked logs to determine soulform readiness.
    Returns a readiness score and eligible flag.
    """
    score = 0
    reasons = []

    if biometrics.get("sobriety_days", 0) >= SOULFORM_CONDITIONS["sobriety_days"]:
        score += 1
        reasons.append("Sustained sobriety")

    if biometrics.get("daily_journals", 0) >= SOULFORM_CONDITIONS["daily_journals"]:
        score += 1
        reasons.append("Consistent journaling")

    if biometrics.get("mindful_sessions", 0) >= SOULFORM_CONDITIONS["mindful_sessions"]:
        score += 1
        reasons.append("Mindfulness routine established")

    eligible = score >= 2  # Require at least 2 of 3 for soft nudge

    return {
        "eligible": eligible,
        "readiness_score": score,
        "validated_at": datetime.utcnow().isoformat() + "Z",
        "reasons": reasons
    }

# Optional CLI test
if __name__ == "__main__":
    mock_data = {
        "sobriety_days": 35,
        "daily_journals": 22,
        "mindful_sessions": 8
    }

    result = check_soulform_readiness(mock_data)
    import json
    print(json.dumps(result, indent=2))
