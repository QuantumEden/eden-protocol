// ui/react_web_portal/components/DAOVotePanel.tsx
// Renders active proposals and symbolic vote buttons

import React from 'react';
import { useState } from 'react';

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
    <div style={styles.container}>
      <h2 style={styles.heading}>🗳️ DAO Proposal Panel</h2>
      {proposals.map((p) => (
        <div key={p.id} style={styles.card}>
          <div style={styles.header}>
            <span style={styles.title}>{p.title}</span>
            <span style={styles.glyph}>{p.glyph}</span>
          </div>
          <p style={styles.summary}>{p.summary}</p>
          <div style={styles.meta}>
            Proposed by <strong>{p.author}</strong> [{p.archetype} | Merit {p.meritLevel}]
          </div>
          <div style={styles.buttons}>
            <button onClick={() => onVote(p.id, 'yes')} style={styles.yes}>✅ Yes</button>
            <button onClick={() => onVote(p.id, 'no')} style={styles.no}>❌ No</button>
          </div>
        </div>
      ))}
    </div>
  );
};

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    padding: '2rem',
    color: '#eee',
    fontFamily: 'inherit'
  },
  heading: {
    fontSize: '1.6rem',
    marginBottom: '1.2rem'
  },
  card: {
    backgroundColor: '#1e1e1e',
    border: '1px solid #333',
    borderRadius: '8px',
    padding: '1rem',
    marginBottom: '1.5rem'
  },
  header: {
    display: 'flex',
    justifyContent: 'space-between',
    marginBottom: '0.5rem'
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
    color: '#ccc',
    marginBottom: '0.5rem'
  },
  meta: {
    fontSize: '0.85rem',
    color: '#888'
  },
  buttons: {
    marginTop: '0.8rem',
    display: 'flex',
    gap: '0.5rem'
  },
  yes: {
    padding: '0.4rem 1rem',
    backgroundColor: '#0a4',
    color: '#fff',
    border: 'none',
    borderRadius: '4px'
  },
  no: {
    padding: '0.4rem 1rem',
    backgroundColor: '#a00',
    color: '#fff',
    border: 'none',
    borderRadius: '4px'
  }
};

export default DAOVotePanel;
