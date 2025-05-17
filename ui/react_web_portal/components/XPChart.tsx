// ui/react_web_portal/components/XPChart.tsx
// Renders symbolic XP progress and level status for Eden Protocol

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
      <h3 style={styles.title}>🧬 Soulbound XP Progress</h3>
      {locked ? (
        <p style={styles.locked}>XP Locked – Realignment Ritual Required</p>
      ) : (
        <>
          <div style={styles.barOuter}>
            <div style={{ ...styles.barInner, width: `${percent}%` }} />
          </div>
          <p style={styles.percent}>{percent}% toward next transformation</p>
        </>
      )}
    </div>
  );
};

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    marginTop: '1.5rem',
    backgroundColor: '#161616',
    padding: '1.2rem',
    borderRadius: '8px',
    border: '1px solid #2f2f2f',
    boxShadow: '0 0 6px rgba(0, 255, 255, 0.1)'
  },
  title: {
    fontSize: '1.25rem',
    color: '#cdeaff',
    marginBottom: '0.6rem'
  },
  locked: {
    color: '#ff5555',
    fontWeight: 600,
    fontSize: '0.95rem'
  },
  barOuter: {
    width: '100%',
    height: '12px',
    backgroundColor: '#333',
    borderRadius: '6px',
    overflow: 'hidden'
  },
  barInner: {
    height: '100%',
    backgroundColor: '#22eaff',
    transition: 'width 0.4s ease'
  },
  percent: {
    fontSize: '0.85rem',
    color: '#aaa',
    marginTop: '0.4rem',
    textAlign: 'right'
  }
};

export default XPChart;
