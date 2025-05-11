# 📡 Eden Disclosure API Contract

This document outlines the technical structure and flow for voluntary trauma or diagnostic disclosure submissions within EdenQuest. All data is opt-in, encrypted, schema-validated, and symbolically processed.

---

## 📥 Submission Endpoint

### `POST /api/disclosure/upload`

Accepts a user’s disclosure payload and optional attachments.

**Headers:**
- `Authorization`: Bearer Token
- `Content-Type`: application/json

**Body (JSON):**
```json
{
  "diagnosis": ["PTSD", "TBI"],
  "trauma_tags": ["combat", "insomnia"],
  "service_connected": true,
  "narrative": "I haven't slept through the night since the deployment.",
  "attachments": [
    "https://eden.quest/uploads/records/va_file_2789.pdf"
  ]
}
