// ui/react_web_portal/components/WorldTreeMap.tsx
// Renders global aggregate of Tree of Life metrics (system resonance pulse)

import React from 'react';

type TraitMap = {
  discipline: number;
  resilience: number;
  mindfulness: number;
  expression: number;
  physical_care: number;
  emotional_regulation: number;
};

type Props = {
  worldTree: TraitMap;
  userCount: number;
};

const WorldTreeMap: React.FC<Props> = ({ worldTree, userCount }) => {
  return (
    <div style={styles.container}>
      <h2 style={styles.heading}>🌍 Collective Resonance — World Tree</h2>
      <p style={styles.meta}>
        Mirroring <strong>{userCount}</strong> symbolic identities across the Eden system.
      </p>
      <div style={styles.traitList}>
        {Object.entries(worldTree).map(([trait, value]) => (
          <div key={trait} style={styles.traitBlock}>
            <div style={styles.labelRow}>
              <span style={styles.traitName}>{formatTrait(trait)}</span>
              <span style={styles.traitValue}>{value}</span>
            </div>
            <div style={styles.barOuter}>
              <div style={{ ...styles.barInner, width: `${value}%` }} />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

// Helper to cleanly format trait names
function formatTrait(trait: string): string {
  return trait.replace(/_/g, ' ').replace(/\b\w/g, (l) => l.toUpperCase());
}

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    padding: '1.8rem',
    backgroundColor: '#121212',
    borderRadius: '10px',
    border: '1px solid #2c2c2c',
    boxShadow: '0 0 10px rgba(0,255,255,0.05)',
    marginTop: '1.5rem',
    color: '#e6faff'
  },
  heading: {
    fontSize: '1.5rem',
    marginBottom: '0.6rem',
    color: '#aaf2ff'
  },
  meta: {
    fontSize: '0.88rem',
    color: '#9a9a9a',
    marginBottom: '1rem'
  },
  traitList: {
    display: 'grid',
    gridTemplateColumns: '1fr',
    gap: '1rem'
  },
  traitBlock: {
    display: 'flex',
    flexDirection: 'column'
  },
  labelRow: {
    display: 'flex',
    justifyContent: 'space-between',
    marginBottom: '0.2rem',
    fontSize: '0.92rem'
  },
  traitName: {
    fontWeight: 500,
    color: '#cceeff'
  },
  traitValue: {
    fontSize: '0.8rem',
    color: '#aaa'
  },
  barOuter: {
    width: '100%',
    height: '10px',
    backgroundColor: '#222',
    borderRadius: '5px',
    overflow: 'hidden'
  },
  barInner: {
    height: '100%',
    backgroundColor: '#22eaff',
    transition: 'width 0.4s ease'
  }
};

export default WorldTreeMap;
