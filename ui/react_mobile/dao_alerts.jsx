import React from 'react';

export default function DAOAlerts({ dao }) {
  if (!dao) return <div>Checking DAO status...</div>;

  return (
    <div style={{ padding: '16px' }}>
      <h2>🗳️ DAO Alerts</h2>
      <p><strong>Last Proposal:</strong> {dao.last_proposal}</p>
      <p><strong>Vote Status:</strong> {dao.status === 'eligible' ? '✅ Eligible to Vote' : '❌ Not Eligible'}</p>
      <p><strong>Vote Weight:</strong> {dao.vote_weight || '1'}</p>
    </div>
  );
}
