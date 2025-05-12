import React from 'react';

export default function TreeHUD({ tree }) {
  if (!tree) return <div>Loading Tree...</div>;

  const traits = [
    "discipline",
    "resilience",
    "mindfulness",
    "expression",
    "physical_care",
    "emotional_regulation"
  ];

  return (
    <div style={{ padding: '16px' }}>
      <h2>🌳 Tree of Life</h2>
      <ul>
        {traits.map(trait => (
          <li key={trait}>
            <strong>{trait.replace('_', ' ')}:</strong> {tree[trait]}
          </li>
        ))}
      </ul>
      <hr />
      <p><strong>Health Index:</strong> {tree.health_index}</p>
    </div>
  );
}
