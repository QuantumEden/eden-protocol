// TreeScreen.tsx – EdenQuest Internal Growth Overview

import React from 'react';
import { View, Text, StyleSheet, SafeAreaView, ScrollView } from 'react-native';
import TreeDisplay from '../components/TreeDisplay';
import XPBar from '../components/XPBar';
import AvatarView from '../components/AvatarView';
import { useEdenPayload } from '../hooks/useEdenPayload';

const TreeScreen = () => {
  const { payload, loading } = useEdenPayload(true);

  if (loading || !payload) {
    return (
      <SafeAreaView style={styles.loadingContainer}>
        <Text style={styles.loadingText}>🌿 Entering symbolic reflection mode...</Text>
      </SafeAreaView>
    );
  }

  const {
    archetype,
    conviction_glyph,
    tree_traits,
    xp_awarded,
    soulform_visuals = null
  } = payload;

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scroll}>
        <Text style={styles.title}>🌳 Tree of Life</Text>
        <Text style={styles.subtitle}>
          Archetype: <Text style={styles.highlight}>{archetype}</Text> | Glyph: {conviction_glyph}
        </Text>

        <AvatarView
          archetype={archetype}
          glyph={conviction_glyph}
          soulform={soulform_visuals}
        />

        <TreeDisplay tree={tree_traits} />
        <XPBar xp={xp_awarded} />
      </ScrollView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#111',
  },
  scroll: {
    padding: 20,
    alignItems: 'center',
  },
  title: {
    fontSize: 20,
    color: '#ffffff',
    fontWeight: '600',
    marginBottom: 6,
  },
  subtitle: {
    fontSize: 14,
    color: '#ccc',
    marginBottom: 16,
    textAlign: 'center',
  },
  highlight: {
    color: '#6cf',
    fontWeight: '600',
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#111',
  },
  loadingText: {
    color: '#888',
    fontSize: 16,
    fontStyle: 'italic',
  },
});

export default TreeScreen;
