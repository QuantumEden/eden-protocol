// ui/react_web_portal/pages/index.tsx
// EdenQuest Dashboard Homepage – Overview of Avatar + DAO Status

import React from 'react';
import DAOVotePanel from '../components/DAOVotePanel';
import XPChart from '../components/XPChart';
import WorldTreeMap from '../components/WorldTreeMap';
import AvatarAudit from '../components/AvatarAudit';

const mockProposals = [
  {
    id: 'prop-001',
    title: 'Sanctify the Ash Grove',
    summary: 'A ritual offering space for those who completed Shadow Quests in the past lunar cycle.',
    author: 'seer_alch_001',
    archetype: 'Strategist',
    glyph: '☯',
    meritLevel: 9
  },
  {
    id: 'prop-002',
    title: 'Open MeritCoin to Group Trials',
    summary: 'Should group-led realignment quests receive merit-based XP modifiers?',
    author: 'guardian_warden_017',
    archetype: 'Guardian',
    glyph: '🛡️',
    meritLevel: 8
  }
];

const mockWorldTree = {
  discipline: 71,
  resilience: 75,
  mindfulness: 68,
  expression: 64,
  physical_care: 61,
  emotional_regulation: 66
};

const mockAuditTrail = [
  {
    timestamp: '2025-02-01T15:00:00Z',
    archetype: 'Strategist',
    level: 7,
    soulform: {
      id: 'phoenix',
      name: 'Ashborn Phoenix',
      element: 'Fire',
      transformed_at: '2025-02-10T14:00:00Z'
    }
  },
  {
    timestamp: '2025-01-10T11:00:00Z',
    archetype: 'Strategist',
    level: 5
  }
];

const HomePage = () => {
  const userXP = 780;
  const nextLevel = 1000;
  const locked = false;

  const handleVote = (proposalId: string, vote: 'yes' | 'no') => {
    console.log(`Voted ${vote} on proposal ${proposalId}`);
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>🌱 Eden Protocol Dashboard</h1>
      <XPChart xp={userXP} nextLevel={nextLevel} locked={locked} />
      <WorldTreeMap worldTree={mockWorldTree} userCount={233} />
      <AvatarAudit history={mockAuditTrail} />
      <DAOVotePanel proposals={mockProposals} onVote={handleVote} />
    </div>
  );
};

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    padding: '2rem',
    maxWidth: '900px',
    margin: '0 auto',
    fontFamily: 'inherit',
    color: '#eee'
  },
  title: {
    fontSize: '2rem',
    marginBottom: '1.5rem',
    color: '#9ef'
  }
};

export default HomePage;
