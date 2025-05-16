// HomeScreen.tsx – EdenQuest Mobile Entry (Soulform-Ready)

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

  const {
    archetype,
    conviction_glyph,
    tree_traits,
    xp_awarded,
    quest_unlocked,
    soulform_visuals = null // optional support for future display
  } = payload;

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <AvatarView
          archetype={archetype}
          glyph={conviction_glyph}
          soulform={soulform_visuals}
        />
        <TreeDisplay tree={tree_traits} />
        <XPBar xp={xp_awarded} />
        <QuestPrompt unlocked={quest_unlocked} />
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
