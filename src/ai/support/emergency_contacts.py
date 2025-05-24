"""
Emergency Contacts – Eidolon Guardian Escalation Interface

Provides emergency response contact data and symbolic guardian linkage
for at-risk users during crisis escalation events.
"""

from typing import Dict, Optional

# Mock emergency contacts by region or organization
EMERGENCY_CONTACTS = {
    "us": {
        "crisis_line": "988",
        "text": "741741",
        "organization": "National Suicide Prevention Lifeline",
        "guardian": "Sentinel One"
    },
    "global": {
        "website": "https://www.befrienders.org/",
        "description": "International directory of emotional support centers",
        "guardian": "Global Watcher"
    }
}

def get_emergency_contact(region_code: str = "us") -> Dict[str, str]:
    """
    Retrieves emergency contact information for the specified region.
    """
    return EMERGENCY_CONTACTS.get(region_code, EMERGENCY_CONTACTS["global"])

def get_guardian_name(region_code: str = "us") -> str:
    """
    Returns symbolic guardian label for user in that region.
    """
    return EMERGENCY_CONTACTS.get(region_code, EMERGENCY_CONTACTS["global"]).get("guardian", "Guardian Unknown")

# Example
if __name__ == "__main__":
    print("📞 Emergency:", get_emergency_contact("us"))
    print("🛡️ Guardian:", get_guardian_name("us"))
