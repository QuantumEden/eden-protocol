/**
 * ExperienceScreen – Eden Protocol Mobile Screen
 * 
 * Displays symbolic world environment and objectives
 * tailored to the user's current soulform and progression.
 */

import React from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';

type WorldData = {
  world_id: string;
  name: string;
  terrain: string;
  climate: string;
  tone: string;
  emblem: string;
  objectives: string[];
};

interface ExperienceScreenProps {
  world: WorldData;
}

const ExperienceScreen: React.FC<ExperienceScreenProps> = ({ world }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>{world.name}</Text>
      <Text style={styles.meta}>🌍 Terrain: {world.terrain}</Text>
      <Text style={styles.meta}>☁️ Climate: {world.climate}</Text>
      <Text style={styles.meta}>🎼 Tone: {world.tone}</Text>
      <Text style={styles.meta}>🜁 Emblem: {world.emblem}</Text>

      <Text style={styles.objectiveHeader}>🎯 Objectives</Text>
      <FlatList
        data={world.objectives}
        keyExtractor={(item, index) => `objective-${index}`}
        renderItem={({ item }) => <Text style={styles.objectiveItem}>• {item}</Text>}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#111',
    padding: 20
  },
  title: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#6cf',
    marginBottom: 12
  },
  meta: {
    fontSize: 14,
    color: '#ccc',
    marginBottom: 4
  },
  objectiveHeader: {
    marginTop: 20,
    fontSize: 18,
    fontWeight: '600',
    color: '#fca'
  },
  objectiveItem: {
    fontSize: 15,
    color: '#ddd',
    marginTop: 6
  }
});

export default ExperienceScreen;
