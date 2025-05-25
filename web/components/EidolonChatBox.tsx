/**
 * EidolonChatBox – Eden Protocol Web Component
 * 
 * Main user interface for therapeutic dialogue with Eidolon on desktop.
 * Displays messages, emotion labels, and accepts user input.
 */

import React, { useState } from 'react';

interface Message {
  role: 'user' | 'eidolon';
  content: string;
  emotion?: string;
}

const EidolonChatBox: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');

  const handleSubmit = async () => {
    if (!input.trim()) return;

    const userMessage: Message = { role: 'user', content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');

    // Mocked response
    const response = await fetch('/support/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user_id: 'alpha_test_001',
        message: input,
        metadata: {}
      })
    });
    const data = await response.json();

    const eidolonMessage: Message = {
      role: 'eidolon',
      content: data.response || '...'
    };
    setMessages((prev) => [...prev, eidolonMessage]);
  };

  return (
    <div style={styles.container}>
      <div style={styles.log}>
        {messages.map((msg, idx) => (
          <div key={idx} style={msg.role === 'user' ? styles.userMsg : styles.eidolonMsg}>
            <strong>{msg.role === 'user' ? 'You' : 'Eidolon'}:</strong> {msg.content}
          </div>
        ))}
      </div>
      <div style={styles.inputArea}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your truth..."
          style={styles.input}
        />
        <button onClick={handleSubmit} style={styles.button}>Send</button>
      </div>
    </div>
  );
};

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    backgroundColor: '#101010',
    padding: '1rem',
    borderRadius: '8px',
    color: '#eee',
    maxWidth: '700px',
    margin: '0 auto',
    fontFamily: 'system-ui'
  },
  log: {
    maxHeight: '400px',
    overflowY: 'auto',
    marginBottom: '1rem'
  },
  userMsg: {
    textAlign: 'right',
    margin: '0.25rem 0',
    color: '#6cf'
  },
  eidolonMsg: {
    textAlign: 'left',
    margin: '0.25rem 0',
    color: '#fc9'
  },
  inputArea: {
    display: 'flex',
    gap: '0.5rem'
  },
  input: {
    flex: 1,
    padding: '0.5rem',
    borderRadius: '4px',
    border: 'none',
    fontSize: '1rem'
  },
  button: {
    backgroundColor: '#3366ff',
    color: '#fff',
    padding: '0.5rem 1rem',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer'
  }
};

export default EidolonChatBox;
