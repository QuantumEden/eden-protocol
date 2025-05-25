/**
 * SymbolicWorld – Eden Protocol Web Component
 * 
 * Visual renderer for symbolic world environments.
 * Displays terrain, tone, objectives, and soulform-emblem alignment.
 */

import React from 'react';

interface WorldData {
  world_id: string;
  name: string;
  terrain: string;
  climate: string;
  tone: string;
  emblem: string;
  objectives: string[];
}

interface SymbolicWorldProps {
  data: WorldData;
}

const SymbolicWorld: React.FC<SymbolicWorldProps> = ({ data }) => {
  return (
    <div style={styles.container}>
      <h2 style={styles.title}>{data.name}</h2>
      <p style={styles.meta}>🗺️ Terrain: {data.terrain}</p>
      <p style={styles.meta}>☁️ Climate: {data.climate}</p>
      <p style={styles.meta}>🎼 Tone: {data.tone}</p>
      <p style={styles.meta}>🜁 Emblem: {data.emblem}</p>
      <div>
        <p style={styles.subtitle}>🎯 Objectives:</p>
        <ul>
          {data.objectives.map((goal, idx) => (
            <li key={idx} style={styles.objective}>{goal}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    backgroundColor: '#121212',
    padding: '1.5rem',
    borderRadius: '12px',
    color: '#eee',
    fontFamily: 'system-ui',
    boxShadow: '0 0 12px rgba(0,0,0,0.4)',
    maxWidth: '600px',
    margin: '2rem auto'
  },
  title: {
    fontSize: '1.6rem',
    fontWeight: 'bold',
    marginBottom: '0.75rem',
    color: '#7ee0ff'
  },
  meta: {
    fontSize: '0.95rem',
    margin: '0.2rem 0',
    color: '#ccc'
  },
  subtitle: {
    marginTop: '1rem',
    fontSize: '1.1rem',
    fontWeight: '600',
    color: '#ffd479'
  },
  objective: {
    margin: '0.25rem 0',
    fontSize: '0.95rem',
    color: '#ddd'
  }
};

export default SymbolicWorld;
