Eden Protocol – Interface Contract (Phase III Finalization)

This document defines the data input and output structure between the Eden Protocol backend and any user-facing interface (mobile app, desktop app, web, XR/VR client, or DAO-integrated platform).

⸻

INPUT STRUCTURE

All inputs are passed to the generate_eden_payload() function via the user_profile dictionary.

Input JSON Schema (Optional: /schemas/user_profile.schema.json)

{
  "mbti": "INTJ",
  "iq": 140,
  "eq": 120,
  "moral": "care"
}

Accepted Fields:

Field	Type	Description
mbti	string	16-type Myers-Briggs personality code
iq	integer	Abstract intelligence score (e.g., from Raven’s Matrices)
eq	integer	Emotional intelligence quotient (e.g., MSCEIT)
moral	string	User’s dominant moral foundation (e.g., care, liberty, loyalty)


⸻

OUTPUT STRUCTURE

Endpoint: generate_eden_payload(user_id, profile_dict, secret_key)

Returns a bundled dictionary structured as:

{
  "avatar": {...},
  "token": "...",
  "tree_of_life": {...},
  "meritcoin": {...},
  "edenquest": {...},
  "dao": {...},
  "world_tree": {...}
}

Output Components and Their Matching Schemas:

1. avatar – /schemas/avatar.schema.json
	•	MBTI type
	•	EdenQuest archetype (Builder, Guardian, Healer, Strategist)
	•	Element (Air, Earth, Fire, Water)
	•	Aura and glyphs

2. token
	•	Signed identity verification string from the Secure Enclave (currently placeholder)

3. tree_of_life – /schemas/tree_of_life.schema.json
	•	Trait values (0–100 scale)
	•	Holistic health score

4. meritcoin – /schemas/xp_meritcoin.schema.json
	•	Current level
	•	XP amount and next-level threshold
	•	Lock state (true/false)

5. edenquest – /schemas/edenquest.schema.json
	•	Assigned symbolic quest object
	•	Title, theme, moral metaphor, growth target

6. dao – /schemas/dao.schema.json
	•	Last proposal metadata
	•	Vote tally
	•	Status and outcome

7. world_tree – /schemas/world_tree.schema.json
	•	Global Eden health index
	•	User count
	•	Symbolic system state

⸻

INTERFACE DESIGN NOTES
	•	All outputs can be rendered independently or as a unified dashboard.
	•	Real-time feedback loops may be visualized symbolically (aura flicker, tree bloom/decay).
	•	Zero-Knowledge Tokens will eventually allow world_tree and XP verification without exposing raw user data.

⸻

NEXT STEPS
	•	Finalize /docs/interface_blueprint.md for visual and UX design alignment
	•	Begin symbolic UI integration using the validated schemas above
