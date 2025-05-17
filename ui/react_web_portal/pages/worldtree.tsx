// ui/react_web_portal/pages/worldtree.tsx
// World Tree Resonance Dashboard – Collective Trait Harmony View

import React from 'react';
import WorldTreeMap from '../components/WorldTreeMap';

const mockWorldTree = {
  discipline: 74,
  resilience: 78,
  mindfulness: 71,
  expression: 67,
  physical_care: 63,
  emotional_regulation: 72
};

const WorldTreePage = () => {
  return (
    <div style={styles.container}>
      <h1 style={styles.title}>🌍 World Tree Resonance Pulse</h1>
      <p style={styles.subtitle}>
        This is the living map of Eden’s collective psyche.  
        Each branch reflects the aggregated growth of all participants.  
        As one heals, all ascend.
      </p>
      <WorldTreeMap worldTree={mockWorldTree} userCount={256} />
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
    color: '#b6f0ff',
    marginBottom: '0.4rem'
  },
  subtitle: {
    fontSize: '1rem',
    color: '#aaaaaa',
    marginBottom: '1.6rem',
    lineHeight: '1.4rem'
  }
};

export default WorldTreePage;
