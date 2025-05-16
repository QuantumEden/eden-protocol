// payloadParser.ts – Utility to extract relevant fields from Eden payload

type TreeTraits = {
  discipline: number;
  resilience: number;
  mindfulness: number;
  expression: number;
  physical_care: number;
  emotional_regulation: number;
};

type EdenPayload = {
  archetype: string;
  conviction_glyph: string;
  tree_traits: TreeTraits;
  xp_awarded: number;
  quest_unlocked: boolean;
};

export function parseTreeTraits(payload: EdenPayload): TreeTraits {
  return {
    discipline: payload.tree_traits?.discipline ?? 0,
    resilience: payload.tree_traits?.resilience ?? 0,
    mindfulness: payload.tree_traits?.mindfulness ?? 0,
    expression: payload.tree_traits?.expression ?? 0,
    physical_care: payload.tree_traits?.physical_care ?? 0,
    emotional_regulation: payload.tree_traits?.emotional_regulation ?? 0,
  };
}

export function getArchetypeGlyph(payload: EdenPayload): {
  archetype: string;
  glyph: string;
} {
  return {
    archetype: payload.archetype,
    glyph: payload.conviction_glyph,
  };
}

export function isQuestAvailable(payload: EdenPayload): boolean {
  return payload.quest_unlocked ?? false;
}
