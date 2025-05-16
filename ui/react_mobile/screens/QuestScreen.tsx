// QuestScreen.tsx – EdenQuest Daily Ritual Screen

import React from 'react';
import { View, Text, StyleSheet, SafeAreaView, ScrollView, Button } from 'react-native';
import VoicePlayer from '../components/VoicePlayer';
import { useEdenPayload } from '../hooks/useEdenPayload';

const QuestScreen = () => {
  const { payload, loading } = useEdenPayload(true); // toggle off simulate in prod

  if (loading || !payload) {
    return (
      <SafeAreaView style={styles.loadingContainer}>
        <Text style={styles.loadingText}>🔮 Retrieving today’s symbolic challenge...</Text>
      </SafeAreaView>
    );
  }

  const { quest_unlocked, archetype } = payload;

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.content}>
        <Text style={styles.title}>🧭 Daily Ritual</Text>
        {quest_unlocked ? (
          <>
            <Text style={styles.description}>
              You have been called to a symbolic test aligned with your archetype: <Text style={styles.highlight}>{archetype}</Text>.
            </Text>

            <VoicePlayer role="mentor" uri="https://eden-audio.s3.amazonaws.com/mentor_intro.mp3" />
            <VoicePlayer role="inner" uri="https://eden-audio.s3.amazonaws.com/inner_reflect.mp3" />

            <View style={styles.buttonGroup}>
              <Button title="Begin Quest" onPress={() => {}} color="#6cf" />
              <Button title="Reflect Instead" onPress={() => {}} color="#ccc" />
              <Button title="Decline for Now" onPress={() => {}} color="#444" />
            </View>
          </>
        ) : (
          <Text style={styles.noQuest}>There is no quest today. Rest and prepare.</Text>
        )}
      </ScrollView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0d0d0d',
  },
  content: {
    padding: 20,
    alignItems: 'center',
  },
  title: {
    color: '#ffffff',
    fontSize: 20,
    fontWeight: '600',
    marginBottom: 12,
  },
  description: {
    color: '#ccc',
    fontSize: 14,
    textAlign: 'center',
    marginBottom: 16,
  },
  highlight: {
    color: '#6cf',
    fontWeight: '600',
  },
  noQuest: {
    color: '#777',
    fontStyle: 'italic',
    marginTop: 20,
    fontSize: 14,
    textAlign: 'center',
  },
  buttonGroup: {
    marginTop: 20,
    width: '100%',
    gap: 10,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#0d0d0d',
  },
  loadingText: {
    color: '#888',
    fontSize: 16,
    fontStyle: 'italic',
  },
});

export default QuestScreen;
