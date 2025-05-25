/**
 * VoicePlayer – Eden Protocol Web Component
 * 
 * Renders and plays synthesized therapeutic voice responses.
 * Accepts audio URL and displays symbolic agent context.
 */

import React, { useState } from 'react';

interface VoicePlayerProps {
  audioUrl: string;
  voiceId: string;
  agentRole: string;
  text: string;
}

const VoicePlayer: React.FC<VoicePlayerProps> = ({ audioUrl, voiceId, agentRole, text }) => {
  const [playing, setPlaying] = useState(false);
  const audio = new Audio(audioUrl);

  const handlePlay = () => {
    setPlaying(true);
    audio.play();
    audio.onended = () => setPlaying(false);
  };

  return (
    <div style={styles.container}>
      <p style={styles.meta}><strong>{agentRole.toUpperCase()}</strong> voice: <em>{voiceId}</em></p>
      <p style={styles.quote}>🗣️ “{text}”</p>
      <button onClick={handlePlay} disabled={playing} style={styles.button}>
        {playing ? "Playing..." : "🔊 Play Response"}
      </button>
    </div>
  );
};

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    padding: '1rem',
    backgroundColor: '#1c1c1c',
    borderRadius: '8px',
    marginBottom: '1rem',
    color: '#eee',
    fontFamily: 'system-ui',
  },
  meta: {
    fontSize: '0.85rem',
    color: '#aaa',
    marginBottom: '0.4rem'
  },
  quote: {
    fontSize: '1rem',
    fontStyle: 'italic',
    marginBottom: '0.6rem'
  },
  button: {
    padding: '0.5rem 1rem',
    backgroundColor: '#2288dd',
    color: '#fff',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer'
  }
};

export default VoicePlayer;
