// HomeScreen.tsx – EdenQuest Mobile Entry

import React, { useEffect, useState } from 'react';
import { View, StyleSheet, ScrollView, SafeAreaView, Text } from 'react-native';
import TreeDisplay from '../components/TreeDisplay';
import XPBar from '../components/XPBar';
import QuestPrompt from '../components/QuestPrompt';
import AvatarView from '../components/AvatarView';
import useEdenPayload from '../hooks/useEdenPayload';

const HomeScreen = () => {
  const { payload, loading } = useEdenPayload();

  if (loading) {
    return (
      <SafeAreaView style={styles.loadingContainer}>
        <Text style={styles.loadingText}>🌱 Syncing with Eden...</Text>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <AvatarView archetype={payload.archetype} glyph={payload.conviction_glyph} />
        <TreeDisplay tree={payload.tree_traits} />
        <XPBar xp={payload.xp_awarded} />
        <QuestPrompt unlocked={payload.quest_unlocked} />
      </ScrollView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0d0d0d',
  },
  scrollContent: {
    padding: 20,
    alignItems: 'center',
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#0d0d0d',
  },
  loadingText: {
    color: '#cccccc',
    fontSize: 18,
    fontStyle: 'italic',
  },
});

export default HomeScreen;
