/**
 * XPMeter – Eden Protocol Web Component
 * 
 * Displays symbolic XP progress bar and soulform evolution status.
 */

import React from 'react';

interface XPMeterProps {
  currentXP: number;
  level: number;
  soulform: string;
  threshold: number;
}

const XPMeter: React.FC<XPMeterProps> = ({ currentXP, level, soulform, threshold }) => {
  const progress = Math.min(100, Math.round((currentXP / threshold) * 100));

  return (
    <div style={styles.container}>
      <p style={styles.label}>🧬 Soulform: <strong>{soulform}</strong></p>
      <p style={styles.label}>🎚️ Merit Level: <strong>{level}</strong></p>
      <div style={styles.meterBackground}>
        <div style={{ ...styles.meterFill, width: `${progress}%` }} />
      </div>
      <p style={styles.progressText}>{currentXP} / {threshold} XP</p>
    </div>
  );
};

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    backgroundColor: '#1a1a1a',
    padding: '1rem',
    borderRadius: '8px',
    color: '#eee',
    fontFamily: 'system-ui',
    textAlign: 'center',
    maxWidth: '400px',
    margin: '0 auto'
  },
  label: {
    marginBottom: '0.5rem',
    fontSize: '0.95rem'
  },
  meterBackground: {
    backgroundColor: '#333',
    borderRadius: '10px',
    height: '16px',
    overflow: 'hidden',
    marginBottom: '0.5rem'
  },
  meterFill: {
    height: '100%',
    backgroundColor: '#6cf',
    transition: 'width 0.5s ease'
  },
  progressText: {
    fontSize: '0.85rem',
    color: '#aaa'
  }
};

export default XPMeter;
