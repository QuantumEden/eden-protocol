// ui/react_web_portal/pages/avatar.tsx
// User Avatar Profile View – Archetype, Soulform, History

import React from 'react';
import AvatarAudit from '../components/AvatarAudit';

const mockAuditTrail = [
  {
    timestamp: '2025-02-01T15:00:00Z',
    archetype: 'Strategist',
    level: 10,
    soulform: {
      id: 'seraph',
      name: 'Wings of Conviction',
      element: 'Air',
      transformed_at: '2025-02-14T14:30:00Z'
    }
  },
  {
    timestamp: '2025-01-11T09:45:00Z',
    archetype: 'Strategist',
    level: 6
  },
  {
    timestamp: '2024-12-30T13:10:00Z',
    archetype: 'Strategist',
    level: 3
  }
];

const AvatarPage = () => {
  return (
    <div style={styles.container}>
      <h1 style={styles.title}>🧠 Avatar & Soulform History</h1>
      <p style={styles.subtitle}>
        Your journey is more than XP — it is who you’ve become through ritual, reflection, and myth.
      </p>
      <AvatarAudit history={mockAuditTrail} />
    </div>
  );
};

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    padding: '2rem',
    maxWidth: '800px',
    margin: '0 auto',
    fontFamily: 'inherit',
    color: '#eee'
  },
  title: {
    fontSize: '1.7rem',
    color: '#9ef',
    marginBottom: '0.4rem'
  },
  subtitle: {
    fontSize: '0.95rem',
    color: '#aaa',
    marginBottom: '1.4rem'
  }
};

export default AvatarPage;
