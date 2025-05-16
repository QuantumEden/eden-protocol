// TreeScreen.tsx – Eden Protocol Mobile HUD
// Displays trait health from Tree of Life and transformation overlay (if any)

import React from 'react';
import { View, Text, StyleSheet, ProgressBarAndroid, ScrollView } from 'react-native';

type TreeTraits = {
  discipline: number;
  resilience: number;
  mindfulness: number;
  expression: number;
  physical_care: number;
  emotional_regulation: number;
};

type SoulformVisuals = {
  id: string;
  name: string;
  elemental_affinity: string;
  aura_effect: string;
  body_shader: string;
  animation_override: string;
};

type Props = {
  tree_traits: TreeTraits;
  soulform_visuals?: SoulformVisuals;
};

const TreeScreen: React.FC<Props> = ({ tree_traits, soulform_visuals }) => {
  const renderTrait = (label: string, value: number) => (
    <View style={styles.traitBlock} key={label}>
      <Text style={styles.label}>{label}</Text>
      <ProgressBarAndroid styleAttr="Horizontal" indeterminate={false} progress={value / 100} />
      <Text style={styles.value}>{value}/100</Text>
    </View>
  );

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.header}>Tree of Life</Text>
      {Object.entries(tree_traits).map(([label, value]) =>
        renderTrait(label.replace('_', ' '), value)
      )}

      {soulform_visuals && (
        <View style={styles.overlayBox}>
          <Text style={styles.soulformTitle}>Active Transformation</Text>
          <Text style={styles.soulformName}>{soulform_visuals.name}</Text>
          <Text style={styles.soulformDetail}>Element: {soulform_visuals.elemental_affinity}</Text>
          <Text style={styles.soulformDetail}>Effect: {soulform_visuals.aura_effect}</Text>
        </View>
      )}
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 20,
    backgroundColor: '#121212',
    flexGrow: 1,
  },
  header: {
    fontSize: 24,
    color: '#E0E0E0',
    marginBottom: 16,
    textAlign: 'center',
  },
  traitBlock: {
    marginVertical: 8,
  },
  label: {
    color: '#BBBBBB',
    fontSize: 16,
  },
  value: {
    color: '#999999',
    fontSize: 14,
    textAlign: 'right',
  },
  overlayBox: {
    marginTop: 32,
    padding: 16,
    backgroundColor: '#1E1E1E',
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#333',
  },
  soulformTitle: {
    color: '#AAAAFF',
    fontSize: 18,
    marginBottom: 4,
  },
  soulformName: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: 'bold',
  },
  soulformDetail: {
    color: '#CCCCCC',
    fontSize: 14,
  },
});

export default TreeScreen;
