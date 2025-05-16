// TreeDisplay.tsx – EdenQuest Trait Visualization (Tree of Life HUD)

import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const traitLabels = {
  discipline: "Discipline",
  resilience: "Resilience",
  mindfulness: "Mindfulness",
  expression: "Expression",
  physical_care: "Physical Care",
  emotional_regulation: "Emotional Regulation"
};

const TraitBar = ({ label, value }: { label: string; value: number }) => (
  <View style={styles.traitContainer}>
    <Text style={styles.label}>{label}</Text>
    <View style={styles.barBackground}>
      <View style={[styles.barFill, { width: `${value}%` }]} />
    </View>
    <Text style={styles.value}>{value}</Text>
  </View>
);

const TreeDisplay = ({ tree }: { tree: Record<string, number> }) => {
  if (!tree) return null;

  return (
    <View style={styles.container}>
      <Text style={styles.title}>🌳 Tree of Life</Text>
      {Object.keys(traitLabels).map((traitKey) => (
        <TraitBar
          key={traitKey}
          label={traitLabels[traitKey]}
          value={tree[traitKey] || 0}
        />
      ))}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    width: '100%',
    marginTop: 20,
    paddingHorizontal: 10,
  },
  title: {
    fontSize: 18,
    color: '#fff',
    fontWeight: '600',
    marginBottom: 10,
    textAlign: 'center',
  },
  traitContainer: {
    marginVertical: 6,
  },
  label: {
    color: '#ccc',
    fontSize: 14,
    marginBottom: 2,
  },
  barBackground: {
    width: '100%',
    height: 10,
    backgroundColor: '#333',
    borderRadius: 5,
    overflow: 'hidden',
  },
  barFill: {
    height: '100%',
    backgroundColor: '#6cf',
    borderRadius: 5,
  },
  value: {
    fontSize: 12,
    color: '#888',
    marginTop: 2,
    textAlign: 'right',
  },
});

export default TreeDisplay;
