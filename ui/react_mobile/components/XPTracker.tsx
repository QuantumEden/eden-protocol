// XPTracker.tsx – Eden Protocol Mobile XP Component
// Displays current level, XP progress, and lockout state

import React from 'react';
import { View, Text, StyleSheet, ProgressBarAndroid } from 'react-native';

type Props = {
  level: number;
  xp: number;
  next_level: number;
  locked: boolean;
};

const XPTracker: React.FC<Props> = ({ level, xp, next_level, locked }) => {
  const progress = Math.min(xp / next_level, 1);

  return (
    <View style={styles.container}>
      <Text style={styles.levelText}>Level {level}</Text>
      {locked ? (
        <Text style={styles.locked}>XP Locked – Realignment Required</Text>
      ) : (
        <View>
          <ProgressBarAndroid
            styleAttr="Horizontal"
            indeterminate={false}
            progress={progress}
            color="#00BFA5"
          />
          <Text style={styles.xpText}>{xp} / {next_level} XP</Text>
        </View>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    marginTop: 16,
    paddingHorizontal: 20,
    paddingVertical: 10,
    backgroundColor: '#1A1A1A',
    borderRadius: 8,
  },
  levelText: {
    fontSize: 18,
    color: '#FAFAFA',
    marginBottom: 8,
    textAlign: 'center',
  },
  xpText: {
    fontSize: 14,
    color: '#CCCCCC',
    textAlign: 'center',
    marginTop: 4,
  },
  locked: {
    fontSize: 14,
    color: '#FF5252',
    textAlign: 'center',
  },
});

export default XPTracker;
