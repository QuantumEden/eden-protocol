import React from 'react';

export default function GroupRitualMap({ group_state }) {
  if (!group_state || group_state.status === "unlinked") {
    return (
      <div style={{ padding: '24px' }}>
        <h2>🕊️ Group Ritual</h2>
        <p>You are currently walking alone. Communion is optional.</p>
      </div>
    );
  }

  return (
    <div style={{ padding: '24px' }}>
      <h2>🕊️ Group Ritual Instance</h2>
      <p><strong>Status:</strong> {group_state.status}</p>
      <p><strong>Resonance Score:</strong> {(group_state.synergy_score * 100).toFixed(1)}%</p>
      <p><strong>Ritual Instance:</strong> {group_state.ritual_instance}</p>
    </div>
  );
}
