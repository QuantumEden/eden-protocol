// WorldTree.tsx – Eden Protocol System Health Dashboard (Web Portal)

import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ProgressBarAndroid, ScrollView } from 'react-native';

// Simulated world tree data (output of world_tree_sync.py)
const worldTreeSnapshot = {
  world_tree: {
    discipline: 62,
    resilience: 68,
    mindfulness: 59,
    expression: 55,
    physical_care: 51,
    emotional_regulation: 64
  },
  user_count: 3
};

const traitColors: Record<string, string> = {
  discipline: '#FFD700',
  resilience: '#4CAF50',
  mindfulness: '#03A9F4',
  expression: '#FF5722',
  physical_care: '#9C27B0',
  emotional_regulation: '#00BCD4'
};

const WorldTree = () => {
  const [data, setData] = useState(worldTreeSnapshot);

  // Future: fetch from backend or file
  useEffect(() => {
    setData(worldTreeSnapshot);
  }, []);

  const renderTrait = (trait: string, value: number) => (
    <View key={trait} style={styles.traitBlock}>
      <Text style={styles.traitName}>{trait.toUpperCase()}</Text>
      <ProgressBarAndroid
        styleAttr="Horizontal"
        indeterminate={false}
        progress={value / 100}
        color={traitColors[trait]}
      />
      <Text style={styles.traitValue}>{value} / 100</Text>
    </View>
  );

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.header}>World Tree: Collective Health</Text>
      <Text style={styles.meta}>Synced Users: {data.user_count}</Text>

      {Object.entries(data.world_tree).map(([trait, value]) =>
        renderTrait(trait, value)
      )}
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 20,
    backgroundColor: '#0D0D0D',
  },
  header: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#A5D6A7',
    marginBottom: 12,
    textAlign: 'center',
  },
  meta: {
    color: '#888',
    fontSize: 12,
    marginBottom: 24,
    textAlign: 'center',
  },
  traitBlock: {
    marginBottom: 20,
  },
  traitName: {
    color: '#F5F5F5',
    fontSize: 14,
    marginBottom: 4,
  },
  traitValue: {
    fontSize: 12,
    color: '#BBBBBB',
    marginTop: 4,
    textAlign: 'right',
  }
});

export default WorldTree;
