// VoicePlayer.tsx – EdenQuest Voice Playback Component (Mentor, Echo, Inner Voice)

import React, { useEffect, useState } from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import { Audio } from 'expo-av';

// Supported voice types for playback
type VoiceRole = 'mentor' | 'echo' | 'inner';

interface VoicePlayerProps {
  role: VoiceRole;
  uri: string; // audio file URL or local path
}

const roleLabels: Record<VoiceRole, string> = {
  mentor: 'Mentor Voice',
  echo: 'Echo Voice',
  inner: 'Inner Voice',
};

const VoicePlayer: React.FC<VoicePlayerProps> = ({ role, uri }) => {
  const [sound, setSound] = useState<Audio.Sound | null>(null);
  const [playing, setPlaying] = useState(false);

  async function playSound() {
    if (playing) return;

    const { sound } = await Audio.Sound.createAsync({ uri });
    setSound(sound);
    setPlaying(true);

    await sound.playAsync();

    sound.setOnPlaybackStatusUpdate((status) => {
      if (!status.isLoaded || status.didJustFinish) {
        setPlaying(false);
        sound.unloadAsync();
      }
    });
  }

  useEffect(() => {
    return sound
      ? () => {
          sound.unloadAsync();
        }
      : undefined;
  }, [sound]);

  return (
    <View style={styles.container}>
      <Text style={styles.label}>{roleLabels[role]}</Text>
      <Button
        title={playing ? 'Playing...' : 'Play'}
        onPress={playSound}
        color={playing ? '#aaa' : '#6cf'}
        disabled={playing}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    marginVertical: 10,
    paddingHorizontal: 16,
    alignItems: 'center',
  },
  label: {
    fontSize: 14,
    color: '#ccc',
    marginBottom: 6,
  },
});

export default VoicePlayer;
