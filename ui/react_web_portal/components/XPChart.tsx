// ui/react_web_portal/components/XPChart.tsx
// Renders symbolic XP progress and level status

import React from 'react';

type Props = {
  xp: number;
  nextLevel: number;
  locked: boolean;
};

const XPChart: React.FC<Props> = ({ xp, nextLevel, locked }) => {
  const percent = Math.min(Math.round((xp / nextLevel) * 100), 100);

  return (
    <div style={styles.container}>
      <h3 style={styles.title}>🧬 Experience Progress</h3>
      {locked ? (
        <p style={styles.locked}>XP is locked — Realignment Required</p>
      ) : (
        <>
          <div style={styles.barOuter}>
            <div style={{ ...styles.barInner, width: `${percent}%` }} />
          </div>
          <p style={styles.percent}>{percent}% to next level</p>
        </>
      )}
    </div>
  );
};

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    marginTop: '1rem',
    backgroundColor: '#1c1c1c',
    padding: '1rem',
    borderRadius: '6px',
    border: '1px solid #333'
  },
  title: {
    fontSize: '1.2rem',
    marginBottom: '0.5rem',
    color: '#ccc'
  },
  locked: {
    color: '#f55',
    fontWeight: 'bold'
  },
  barOuter: {
    width: '100%',
    height: '10px',
    backgroundColor: '#333',
    borderRadius: '5px',
    overflow: 'hidden'
  },
  barInner: {
    height: '100%',
    backgroundColor: '#0cf',
    transition: 'width 0.4s ease'
  },
  percent: {
    fontSize: '0.9rem',
    color: '#aaa',
    marginTop: '0.4rem',
    textAlign: 'right'
  }
};

export default XPChart;
