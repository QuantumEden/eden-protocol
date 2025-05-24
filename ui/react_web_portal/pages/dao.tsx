// ui/react_web_portal/pages/dao.tsx
// DAO Proposal Browser and Voting Interface (Ritual-Aware)

import React from 'react';
import DAOVotePanel from '../components/DAOVotePanel';

const mockProposals = [
  {
    id: 'prop-003',
    title: 'Add Lunar Shadow Quests',
    summary: 'Propose inclusion of moon-phase based Shadow quests tied to disclosure windows.',
    author: 'healer_echo_022',
    archetype: 'Healer',
    glyph: '💧',
    meritLevel: 6,
    ritualVerified: true,
    soulformStage: 'Initiate',
    zkxpHash: 'zkxp-shadow-moon'
  },
  {
    id: 'prop-004',
    title: 'Abolish Experience Lockouts',
    summary: 'Should EdenQuest soften XP punishment systems for failing ritual alignment?',
    author: 'rogue_path_019',
    archetype: 'Builder',
    glyph: '🛠️',
    meritLevel: 7,
    ritualVerified: false,
    soulformStage: 'Ascendant',
    zkxpHash: 'zkxp-lock-null'
  }
];

const DAOPortal = () => {
  const handleVote = (proposalId: string, vote: 'yes' | 'no') => {
    console.log(`[DAO] ${vote.toUpperCase()} cast on proposal ${proposalId}`);
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.header}>🗳️ Decentralized Autonomous Oracle</h1>
      <p style={styles.description}>
        This is Eden’s governance ritual — each proposal is a mirror for your truth.
        Vote with integrity. Shape the myth.
      </p>
      <DAOVotePanel proposals={mockProposals} onVote={handleVote} />
    </div>
  );
};

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    padding: '2rem',
    maxWidth: '800px',
    margin: '0 auto',
    color: '#eeeeee',
    fontFamily: 'system-ui, sans-serif',
    backgroundColor: '#0c0c0c',
    borderRadius: '10px',
    boxShadow: '0 0 20px rgba(255, 255, 255, 0.05)'
  },
  header: {
    fontSize: '1.8rem',
    marginBottom: '1rem',
    color: '#bfeeff',
    textAlign: 'center'
  },
  description: {
    fontSize: '0.95rem',
    marginBottom: '1.5rem',
    color: '#bbbbbb',
    textAlign: 'center'
  }
};

export default DAOPortal;
