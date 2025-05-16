// ui/react_web_portal/pages/worldtree.tsx
// Collective World Tree View – Eden System Resonance Pulse

import React from 'react';
import WorldTreeMap from '../components/WorldTreeMap';

const mockWorldTree = {
  discipline: 69,
  resilience: 73,
  mindfulness: 65,
  expression: 62,
  physical_care: 58,
  emotional_regulation: 70
};

const WorldTreePage = () => {
  return (
    <div style={styles.container}>
      <h1 style={styles.title}>🌍 World Tree Resonance</h1>
      <p style={styles.subtitle}>
        The World Tree mirrors the state of our shared growth. Every act of reflection, discipline, and disclosure nurtures its branches.
      </p>
      <WorldTreeMap worldTree={mockWorldTree} userCount={241} />
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
    color: '#cdeaff',
    marginBottom: '0.5rem'
  },
  subtitle: {
    fontSize: '0.95rem',
    color: '#aaa',
    marginBottom: '1.2rem'
  }
};

export default WorldTreePage;
