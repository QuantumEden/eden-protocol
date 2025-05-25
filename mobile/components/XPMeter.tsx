/**
 * XPMeter – Eden Protocol Mobile Component
 * 
 * Renders XP progress bar and soulform metadata for mobile users.
 */

import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

interface XPMeterProps {
  currentXP: number;
  level: number;
  soulform: string;
  threshold: number;
}

const XPMeter: React.FC<XPMeterProps> = ({ currentXP, level, soulform, threshold }) => {
  const progress = Math.min(100, Math.round((currentXP / threshold) * 100));

  return (
    <View style={styles.container}>
      <Text style={styles.label}>🧬 Soulform: {soulform}</Text>
      <Text style={styles.label}>🎚️ Level: {level}</Text>
      <View style={styles.barBackground}>
        <View style={[styles.barFill, { width: `${progress}%` }]} />
      </View>
      <Text style={styles.progressText}>{currentXP} / {threshold} XP</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#222',
    padding: 16,
    borderRadius: 8,
    marginBottom: 20
  },
  label: {
    color: '#ccc',
    fontSize: 14,
    marginBottom: 4
  },
  barBackground: {
    backgroundColor: '#444',
    height: 14,
    borderRadius: 7,
    overflow: 'hidden',
    marginVertical: 6
  },
  barFill: {
    backgroundColor: '#6cf',
    height: '100%'
  },
  progressText: {
    color: '#aaa',
    fontSize: 12,
    textAlign: 'center'
  }
});

export default XPMeter;
