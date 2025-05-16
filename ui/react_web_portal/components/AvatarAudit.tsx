// ui/react_web_portal/components/AvatarAudit.tsx
// Renders soulbound avatar evolution log and archetype milestones

import React from 'react';

type AuditEntry = {
  timestamp: string;
  archetype: string;
  level: number;
  soulform?: {
    id: string;
    name: string;
    element: string;
    transformed_at?: string;
  };
};

type Props = {
  history: AuditEntry[];
};

const AvatarAudit: React.FC<Props> = ({ history }) => {
  return (
    <div style={styles.container}>
      <h3 style={styles.heading}>🧬 Avatar Audit Trail</h3>
      <div style={styles.list}>
        {history.map((entry, idx) => (
          <div key={idx} style={styles.card}>
            <div style={styles.row}>
              <strong>{entry.archetype}</strong> — Level {entry.level}
            </div>
            <div style={styles.sub}>
              🕒 {new Date(entry.timestamp).toLocaleString()}
            </div>
            {entry.soulform && (
              <div style={styles.soulform}>
                🔓 Transformed: <strong>{entry.soulform.name}</strong> ({entry.soulform.element})
                {entry.soulform.transformed_at && (
                  <span style={styles.transformedAt}>
                    @ {new Date(entry.soulform.transformed_at).toLocaleDateString()}
                  </span>
                )}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    padding: '1.5rem',
    backgroundColor: '#181818',
    border: '1px solid #333',
    borderRadius: '8px',
    marginTop: '1rem',
    color: '#eee'
  },
  heading: {
    fontSize: '1.4rem',
    marginBottom: '1rem'
  },
  list: {
    display: 'flex',
    flexDirection: 'column',
    gap: '1rem'
  },
  card: {
    padding: '1rem',
    backgroundColor: '#222',
    borderRadius: '6px',
    border: '1px solid #444'
  },
  row: {
    fontSize: '1.1rem',
    color: '#bdf'
  },
  sub: {
    fontSize: '0.85rem',
    color: '#888',
    marginTop: '0.3rem'
  },
  soulform: {
    marginTop: '0.6rem',
    fontSize: '0.9rem',
    color: '#fc9'
  },
  transformedAt: {
    fontSize: '0.8rem',
    marginLeft: '0.5rem',
    color: '#999'
  }
};

export default AvatarAudit;
