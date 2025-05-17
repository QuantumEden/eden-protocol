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
      <h3 style={styles.heading}>🧬 Soulbound Avatar Audit Trail</h3>
      {history.length === 0 ? (
        <p style={styles.empty}>No recorded evolution yet. Begin your journey.</p>
      ) : (
        <div style={styles.list}>
          {history.map((entry, idx) => (
            <div key={idx} style={styles.card}>
              <div style={styles.row}>
                <strong>{entry.archetype}</strong> — Level {entry.level}
              </div>
              <div style={styles.sub}>
                🕒 {formatDateTime(entry.timestamp)}
              </div>
              {entry.soulform && (
                <div style={styles.soulform}>
                  🔓 Soulform: <strong>{entry.soulform.name}</strong> ({entry.soulform.element})
                  {entry.soulform.transformed_at && (
                    <span style={styles.transformedAt}>
                      @ {formatDate(entry.soulform.transformed_at)}
                    </span>
                  )}
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

function formatDateTime(timestamp: string): string {
  try {
    return new Date(timestamp).toLocaleString();
  } catch {
    return 'Invalid Date';
  }
}

function formatDate(dateStr: string): string {
  try {
    return new Date(dateStr).toLocaleDateString();
  } catch {
    return 'Unknown';
  }
}

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    padding: '1.6rem',
    backgroundColor: '#161616',
    border: '1px solid #2c2c2c',
    borderRadius: '10px',
    marginTop: '1.5rem',
    color: '#e6faff'
  },
  heading: {
    fontSize: '1.4rem',
    marginBottom: '1rem',
    color: '#aaf2ff'
  },
  empty: {
    color: '#888',
    fontStyle: 'italic',
    fontSize: '0.95rem'
  },
  list: {
    display: 'flex',
    flexDirection: 'column',
    gap: '1rem'
  },
  card: {
    padding: '1rem',
    backgroundColor: '#1f1f1f',
    borderRadius: '6px',
    border: '1px solid #3c3c3c'
  },
  row: {
    fontSize: '1.05rem',
    fontWeight: 500,
    color: '#bdeaff'
  },
  sub: {
    fontSize: '0.85rem',
    color: '#999',
    marginTop: '0.3rem'
  },
  soulform: {
    marginTop: '0.6rem',
    fontSize: '0.9rem',
    color: '#ffc995'
  },
  transformedAt: {
    fontSize: '0.8rem',
    marginLeft: '0.4rem',
    color: '#bbb'
  }
};

export default AvatarAudit;
