// ui/react_web_portal/components/DisclosureLog.tsx
// Visualizes symbolic disclosures and their impact on Tree of Life growth

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
      <h3 style={styles.heading}>🔐 Disclosure Impact Timeline</h3>
      {logs.length === 0 ? (
        <p style={styles.empty}>No symbolic disclosures recorded yet.</p>
      ) : (
        logs.map((event, idx) => (
          <div key={idx} style={styles.card}>
            <div style={styles.header}>
              <span>🕒 {formatTimestamp(event.timestamp)}</span>
              {event.service_connected && <span style={styles.flag}>⚔️ Service Connected</span>}
            </div>

            <div style={styles.tags}>
              {event.tags.map((tag, i) => (
                <span key={i} style={styles.tag}>#{tag}</span>
              ))}
            </div>

            {event.diagnosis && event.diagnosis.length > 0 && (
              <div style={styles.diagnosis}>
                <strong>Diagnosis:</strong> {event.diagnosis.join(', ')}
              </div>
            )}

            <div style={styles.impact}>
              {Object.entries(event.impact).map(([trait, change], i) => (
                <div key={i} style={styles.traitChange}>
                  🌿 {formatTrait(trait)}: <span style={change >= 0 ? styles.pos : styles.neg}>
                    {change >= 0 ? `+${change}` : `${change}`}
                  </span>
                </div>
              ))}
            </div>
          </div>
        ))
      )}
    </div>
  );
};

function formatTimestamp(ts: string): string {
  try {
    return new Date(ts).toLocaleString();
  } catch {
    return 'Invalid Date';
  }
}

function formatTrait(trait: string): string {
  return trait.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
}

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    padding: '1.5rem',
    backgroundColor: '#151515',
    border: '1px solid #333',
    borderRadius: '10px',
    marginTop: '1rem',
    color: '#e0f7ff'
  },
  heading: {
    fontSize: '1.4rem',
    marginBottom: '1rem',
    color: '#aaf2ff'
  },
  empty: {
    fontSize: '0.9rem',
    fontStyle: 'italic',
    color: '#888'
  },
  card: {
    backgroundColor: '#1f1f1f',
    padding: '1rem',
    marginBottom: '1rem',
    borderRadius: '8px',
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
    color: '#f77',
    fontWeight: 'bold'
  },
  tags: {
    display: 'flex',
    flexWrap: 'wrap',
    gap: '0.4rem',
    marginBottom: '0.5rem'
  },
  tag: {
    backgroundColor: '#2c2c2c',
    padding: '0.3rem 0.6rem',
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
    marginTop: '0.6rem'
  },
  traitChange: {
    marginTop: '0.25rem'
  },
  pos: {
    color: '#6f6',
    fontWeight: 'bold'
  },
  neg: {
    color: '#f66',
    fontWeight: 'bold'
  }
};

export default DisclosureLog;
