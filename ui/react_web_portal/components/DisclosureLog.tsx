// ui/react_web_portal/components/DisclosureLog.tsx
// Visualizes symbolic disclosures and the impact they had on the Tree of Life

import React from 'react';

type DisclosureEvent = {
  timestamp: string;
  tags: string[];
  diagnosis?: string[];
  service_connected?: boolean;
  impact: {
    [trait: string]: number;
  };
};

type Props = {
  logs: DisclosureEvent[];
};

const DisclosureLog: React.FC<Props> = ({ logs }) => {
  return (
    <div style={styles.container}>
      <h3 style={styles.heading}>🔐 Disclosure Timeline</h3>
      {logs.map((event, idx) => (
        <div key={idx} style={styles.card}>
          <div style={styles.header}>
            <span>🕒 {new Date(event.timestamp).toLocaleString()}</span>
            {event.service_connected && <span style={styles.flag}>⚔️ Service Connected</span>}
          </div>
          <div style={styles.tags}>
            {event.tags.map((tag, i) => (
              <span key={i} style={styles.tag}>#{tag}</span>
            ))}
          </div>
          {event.diagnosis && (
            <div style={styles.diagnosis}>
              <strong>Diagnosis:</strong> {event.diagnosis.join(', ')}
            </div>
          )}
          <div style={styles.impact}>
            {Object.entries(event.impact).map(([trait, change], i) => (
              <div key={i} style={styles.traitChange}>
                🌿 {trait.replace('_', ' ')}: <span style={change >= 0 ? styles.pos : styles.neg}>
                  {change >= 0 ? `+${change}` : change}
                </span>
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
};

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    padding: '1.5rem',
    backgroundColor: '#141414',
    border: '1px solid #333',
    borderRadius: '8px',
    marginTop: '1rem',
    color: '#eee'
  },
  heading: {
    fontSize: '1.4rem',
    marginBottom: '1rem'
  },
  card: {
    backgroundColor: '#1f1f1f',
    padding: '1rem',
    marginBottom: '1rem',
    borderRadius: '6px',
    border: '1px solid #444'
  },
  header: {
    display: 'flex',
    justifyContent: 'space-between',
    fontSize: '0.85rem',
    color: '#aaa',
    marginBottom: '0.5rem'
  },
  flag: {
    color: '#f77'
  },
  tags: {
    display: 'flex',
    flexWrap: 'wrap',
    gap: '0.4rem',
    marginBottom: '0.4rem'
  },
  tag: {
    backgroundColor: '#333',
    padding: '0.2rem 0.5rem',
    borderRadius: '4px',
    fontSize: '0.75rem',
    color: '#9ef'
  },
  diagnosis: {
    fontSize: '0.85rem',
    color: '#ccc',
    marginBottom: '0.4rem'
  },
  impact: {
    fontSize: '0.85rem',
    color: '#ccc',
    marginTop: '0.5rem'
  },
  traitChange: {
    marginTop: '0.2rem'
  },
  pos: {
    color: '#6f6'
  },
  neg: {
    color: '#f66'
  }
};

export default DisclosureLog;
