// ui/react_web_portal/components/WorldTreeMap.tsx
// Renders global aggregate of Tree of Life metrics (world state pulse)

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
      <h2 style={styles.heading}>🌍 World Tree State</h2>
      <p style={styles.meta}>Reflecting {userCount} symbolic users</p>
      <div style={styles.traitList}>
        {Object.entries(worldTree).map(([trait, value]) => (
          <div key={trait} style={styles.traitBlock}>
            <span style={styles.traitName}>{trait.replace('_', ' ')}</span>
            <div style={styles.barOuter}>
              <div style={{ ...styles.barInner, width: `${value}%` }} />
            </div>
            <span style={styles.traitValue}>{value}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    padding: '1.5rem',
    backgroundColor: '#111',
    border: '1px solid #333',
    borderRadius: '8px',
    marginTop: '1rem',
    color: '#ddd'
  },
  heading: {
    fontSize: '1.5rem',
    marginBottom: '0.4rem'
  },
  meta: {
    fontSize: '0.85rem',
    color: '#888',
    marginBottom: '1rem'
  },
  traitList: {
    display: 'grid',
    gridTemplateColumns: '1fr',
    gap: '0.8rem'
  },
  traitBlock: {
    display: 'flex',
    flexDirection: 'column'
  },
  traitName: {
    fontSize: '0.95rem',
    marginBottom: '0.2rem',
    textTransform: 'capitalize'
  },
  barOuter: {
    width: '100%',
    height: '8px',
    backgroundColor: '#333',
    borderRadius: '4px',
    overflow: 'hidden'
  },
  barInner: {
    height: '100%',
    backgroundColor: '#6cf',
    transition: 'width 0.4s ease'
  },
  traitValue: {
    fontSize: '0.75rem',
    textAlign: 'right',
    marginTop: '0.2rem',
    color: '#aaa'
  }
};

export default WorldTreeMap;
