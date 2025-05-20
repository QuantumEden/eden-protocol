# api/services/xp_service.py
# Eden Protocol – XP + MeritCoin Service Layer

from datetime import datetime
from infra.xp.meritcoin_ledger import log_commit
from infra.xp.zkxp_commit_checker import generate_zkxp_stub_hash
from infra.voice_response_stub import speak

from api.models.xp import XPCommit, XPDisclosure, XPModGrant


class XPService:

    def commit(self, user_id: str, payload: XPCommit) -> dict:
        zk_hash = generate_zkxp_stub_hash(user_id, payload.xp, payload.level)

        commit = log_commit(
            user_id=user_id,
            level=payload.level,
            xp=payload.xp,
            reason=payload.reason,
            traits_snapshot=payload.traits_snapshot,
            verified_by=zk_hash
        )

        speak("xp_commit")
        return {
            "message": "XP committed successfully",
            "commit": commit
        }

    def apply_disclosure_reward(self, user_id: str, payload: XPDisclosure) -> dict:
        xp_award = int((payload.truth + payload.vulnerability) * 0.5)

        commit = log_commit(
            user_id=user_id,
            level=payload.level,
            xp=xp_award,
            reason="Sacred disclosure",
            traits_snapshot=payload.traits_snapshot
        )

        speak("disclosure_awarded")
        return {
            "xp_awarded": xp_award,
            "commit": commit
        }

    def mod_grant(self, user_id: str, payload: XPModGrant, mod_id: str) -> dict:
        commit = log_commit(
            user_id=user_id,
            level=payload.level,
            xp=payload.xp,
            reason=f"Granted by moderator {mod_id}",
            traits_snapshot=payload.traits_snapshot,
            verified_by=f"mod:{mod_id}"
        )

        speak("mod_grant")
        return {
            "message": "Moderator XP granted",
            "commit": commit
        }
