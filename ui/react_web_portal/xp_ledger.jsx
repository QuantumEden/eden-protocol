import React from 'react';

export default function XPLedger({ meritcoin }) {
  if (!meritcoin) return <div>Loading XP Ledger...</div>;

  return (
    <div style={{ padding: '24px' }}>
      <h2>📈 XP Ledger</h2>
      <p><strong>Current Level:</strong> {meritcoin.level}</p>
      <p><strong>Total XP:</strong> {meritcoin.xp}</p>
      <p><strong>Next Threshold:</strong> {meritcoin.xp_threshold}</p>
      <p><strong>XP Locked:</strong> {meritcoin.locked ? '🔒 Yes' : '✅ No'}</p>
    </div>
  );
}
