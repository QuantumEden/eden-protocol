// ui/react_web_portal/pages/avatar.tsx
// Avatar & Soulform Progression Log – Eden Protocol User History

import React from 'react';
import AvatarAudit from '../components/AvatarAudit';

const mockAuditTrail = [
  {
    timestamp: '2025-05-10T16:00:00Z',
    archetype: 'Strategist',
    level: 12,
    soulform: {
      id: 'wyrm',
      name: 'Chrono Wyrm',
      element: 'Air',
      transformed_at: '2025-05-06T18:10:00Z'
    }
  },
  {
    timestamp: '2025-04-14T12:15:00Z',
    archetype: 'Strategist',
    level: 9,
    soulform: {
      id: 'phoenix',
      name: 'Ashborn Phoenix',
      element: 'Fire',
      transformed_at: '2025-04-12T07:40:00Z'
    }
  },
  {
    timestamp: '2025-03-08T10:05:00Z',
    archetype: 'Strategist',
    level: 5
  }
];

const AvatarPage = () => {
  return (
    <div style={styles.container}>
      <h1 style={styles.title}>🧠 Avatar & Soulform History</h1>
      <p style={styles.subtitle}>
        This is the symbolic audit trail of your transformation. It tracks every archetype, soulform, and milestone.
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
    color: '#eeeeee'
  },
  title: {
    fontSize: '1.8rem',
    color: '#aee2ff',
    marginBottom: '0.5rem'
  },
  subtitle: {
    fontSize: '1rem',
    color: '#aaa',
    marginBottom: '1.5rem'
  }
};

export default AvatarPage;
