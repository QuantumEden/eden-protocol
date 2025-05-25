/**
 * VoicePlayer – Eden Protocol Mobile Component
 * 
 * Plays synthesized therapeutic audio with simplified controls
 * for mobile environments. Uses React Native Audio for playback.
 */

import React, { useState } from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import { Audio } from 'expo-av';

interface VoicePlayerProps {
  audioUrl: string;
  voiceId: string;
  agentRole: string;
  text: string;
}

const VoicePlayer: React.FC<VoicePlayerProps> = ({ audioUrl, voiceId, agentRole, text }) => {
  const [playing, setPlaying] = useState(false);
  const [sound, setSound] = useState<Audio.Sound | null>(null);

  const playSound = async () => {
    try {
      setPlaying(true);
      const { sound: loadedSound } = await Audio.Sound.createAsync({ uri: audioUrl });
      setSound(loadedSound);
      await loadedSound.playAsync();
      loadedSound.setOnPlaybackStatusUpdate((status) => {
        if (!status.isPlaying) setPlaying(false);
      });
    } catch (error) {
      console.warn('Audio playback error:', error);
      setPlaying(false);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.meta}>{agentRole.toUpperCase()} • Voice: {voiceId}</Text>
      <Text style={styles.text}>🗣️ “{text}”</Text>
      <Button title={playing ? "Playing..." : "Play Voice"} onPress={playSound} disabled={playing} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 16,
    backgroundColor: '#202020',
    borderRadius: 10,
    marginBottom: 20,
  },
  meta: {
    color: '#aaa',
    marginBottom: 6,
    fontSize: 12,
  },
  text: {
    color: '#fff',
    fontStyle: 'italic',
    marginBottom: 10,
    fontSize: 14,
  }
});

export default VoicePlayer;
