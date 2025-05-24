import React from 'react';

export default function DAOAlerts({ dao }) {
  if (!dao) return <div>Checking DAO status...</div>;

  const {
    last_proposal,
    status,
    vote_weight,
    ritual_verified,
    zkxp_commit_hash,
    suspension_state,
    soulform_stage
  } = dao;

  const statusDisplay = () => {
    if (suspension_state === 'banned') return '🚫 Banned from DAO';
    if (suspension_state === 'suspended') return '⏸️ Temporarily Suspended';
    return status === 'eligible' ? '✅ Eligible to Vote' : '❌ Not Eligible';
  };

  return (
    <div style={{ padding: '16px' }}>
      <h2>🗳️ DAO Alerts</h2>
      <p><strong>Last Proposal:</strong> {last_proposal || 'None submitted'}</p>
      <p><strong>Status:</strong> {statusDisplay()}</p>
      <p><strong>Vote Weight:</strong> {vote_weight || '1'}</p>
      <p><strong>Soulform Stage:</strong> {soulform_stage || 'Unknown'}</p>
      <p><strong>Ritual Verified:</strong> {ritual_verified ? '🕊️ Yes' : '⚠️ No'}</p>
      <p><strong>zkXP Commit:</strong> {zkxp_commit_hash || 'Not recorded'}</p>
    </div>
  );
}
