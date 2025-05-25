/**
 * SupportChatScreen – Eden Protocol Mobile Screen
 * 
 * Mobile UI for user dialogue with Eidolon AI.
 * Displays chat bubbles, handles emotional tone feedback.
 */

import React, { useState } from 'react';
import { View, Text, TextInput, Button, ScrollView, StyleSheet } from 'react-native';

type Message = {
  role: 'user' | 'eidolon';
  content: string;
  emotion?: string;
};

const SupportChatScreen: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');

  const handleSubmit = async () => {
    if (!input.trim()) return;

    const userMessage: Message = { role: 'user', content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');

    // Mock API call
    const response = await fetch('https://api.edenprotocol.ai/support/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user_id: 'mobile_user_001',
        message: input,
        metadata: {}
      })
    });
    const data = await response.json();

    const aiMessage: Message = {
      role: 'eidolon',
      content: data.response || '...'
    };
    setMessages((prev) => [...prev, aiMessage]);
  };

  return (
    <View style={styles.container}>
      <ScrollView style={styles.chatLog}>
        {messages.map((msg, idx) => (
          <Text
            key={idx}
            style={msg.role === 'user' ? styles.userBubble : styles.eidolonBubble}
          >
            {msg.role === 'user' ? 'You: ' : 'Eidolon: '}
            {msg.content}
          </Text>
        ))}
      </ScrollView>
      <View style={styles.inputRow}>
        <TextInput
          value={input}
          onChangeText={setInput}
          placeholder="Type your reflection..."
          style={styles.input}
        />
        <Button title="Send" onPress={handleSubmit} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#181818',
    padding: 16
  },
  chatLog: {
    flex: 1,
    marginBottom: 10
  },
  userBubble: {
    color: '#6cf',
    alignSelf: 'flex-end',
    marginBottom: 6,
    fontSize: 16
  },
  eidolonBubble: {
    color: '#fc9',
    alignSelf: 'flex-start',
    marginBottom: 6,
    fontSize: 16
  },
  inputRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8
  },
  input: {
    flex: 1,
    backgroundColor: '#2a2a2a',
    padding: 10,
    color: '#fff',
    borderRadius: 6
  }
});

export default SupportChatScreen;
