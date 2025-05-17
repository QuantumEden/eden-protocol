// ui/react_web_portal/components/DAOVotePanel.tsx
// Renders active proposals with symbolic metadata and truth-weighted vote actions

import React from 'react';

type Proposal = {
  id: string;
  title: string;
  summary: string;
  author: string;
  archetype: string;
  glyph: string;
  meritLevel: number;
};

type Props = {
  proposals: Proposal[];
  onVote: (proposalId: string, vote: 'yes' | 'no') => void;
};

const DAOVotePanel: React.FC<Props> = ({ proposals, onVote }) => {
  return (
    <section style={styles.container}>
      <h2 style={styles.heading}>🗳️ Symbolic Proposal Gallery</h2>
      {proposals.map((p) => (
        <div key={p.id} style={styles.card}>
          <div style={styles.header}>
            <span style={styles.title}>{p.title}</span>
            <span style={styles.glyph}>{p.glyph}</span>
          </div>
          <p style={styles.summary}>{p.summary}</p>
          <div style={styles.meta}>
            By <strong>{p.author}</strong> [{p.archetype} | Merit {p.meritLevel}]
          </div>
          <div style={styles.buttons}>
            <button onClick={() => onVote(p.id, 'yes')} style={styles.yes}>✅ Affirm</button>
            <button onClick={() => onVote(p.id, 'no')} style={styles.no}>❌ Reject</button>
          </div>
        </div>
      ))}
    </section>
  );
};

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    padding: '2rem',
    fontFamily: 'inherit',
    color: '#eeeeee'
  },
  heading: {
    fontSize: '1.6rem',
    marginBottom: '1.4rem',
    color: '#cdeaff'
  },
  card: {
    backgroundColor: '#1b1b1b',
    border: '1px solid #333',
    borderRadius: '8px',
    padding: '1.2rem',
    marginBottom: '1.6rem'
  },
  header: {
    display: 'flex',
    justifyContent: 'space-between',
    marginBottom: '0.6rem'
  },
  title: {
    fontWeight: 'bold',
    fontSize: '1.1rem'
  },
  glyph: {
    fontSize: '1.4rem'
  },
  summary: {
    fontSize: '0.95rem',
    color: '#cccccc',
    marginBottom: '0.5rem'
  },
  meta: {
    fontSize: '0.85rem',
    color: '#aaaaaa'
  },
  buttons: {
    marginTop: '0.9rem',
    display: 'flex',
    gap: '0.75rem'
  },
  yes: {
    padding: '0.4rem 1.1rem',
    backgroundColor: '#117744',
    color: '#ffffff',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer'
  },
  no: {
    padding: '0.4rem 1.1rem',
    backgroundColor: '#aa2222',
    color: '#ffffff',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer'
  }
};

export default DAOVotePanel;
