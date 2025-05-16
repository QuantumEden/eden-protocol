// ui/react_web_portal/utils/sessionParser.ts
// Parses Eden payload and session data into modular frontend-safe formats

type RawPayload = {
  archetype: string;
  conviction_glyph: string;
  tree_traits: Record<string, number>;
  xp_awarded: number;
  quest_unlocked: boolean;
  disclosure_adjustment: Record<string, number>;
  soulform?: {
    id: string;
    name: string;
    element: string;
    transformed_at?: string;
  };
  level?: number;
  next_level?: number;
  locked?: boolean;
};

export function parseSession(payload: RawPayload) {
  return {
    avatar: {
      archetype: payload.archetype,
      glyph: payload.conviction_glyph,
      soulform: payload.soulform || null
    },
    tree: payload.tree_traits,
    xp: {
      current: payload.xp_awarded,
      level: payload.level || 1,
      nextLevel: payload.next_level || 1000,
      locked: payload.locked || false
    },
    disclosure: payload.disclosure_adjustment || {},
    questReady: payload.quest_unlocked
  };
}
