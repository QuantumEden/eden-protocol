import React from 'react';

export default function QuestJournal({ edenquest }) {
  if (!edenquest) return <div>Loading quest...</div>;

  return (
    <div style={{ padding: '16px' }}>
      <h2>🧙 EdenQuest Journal</h2>
      <p><strong>Title:</strong> {edenquest.title}</p>
      <p><strong>Theme:</strong> {edenquest.theme}</p>
      <p><strong>Metaphor:</strong> {edenquest.metaphor}</p>
      <p><strong>Growth Target:</strong> {edenquest.growth_target}</p>
    </div>
  );
}
