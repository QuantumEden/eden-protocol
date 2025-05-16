// QuestModal.tsx – Eden Protocol Mobile Quest Ritual Prompt
// Displays symbolic quest, reflection prompt, and ritual controls

import React from 'react';
import { View, Text, StyleSheet, Modal, Button } from 'react-native';

type Props = {
  visible: boolean;
  onAccept: () => void;
  onDecline: () => void;
  onComplete: () => void;
  questTitle: string;
  questDescription: string;
  voiceHint?: string;
};

const QuestModal: React.FC<Props> = ({
  visible,
  onAccept,
  onDecline,
  onComplete,
  questTitle,
  questDescription,
  voiceHint,
}) => {
  return (
    <Modal visible={visible} animationType="slide" transparent={true}>
      <View style={styles.overlay}>
        <View style={styles.modalBox}>
          <Text style={styles.title}>{questTitle}</Text>
          <Text style={styles.description}>{questDescription}</Text>

          {voiceHint && <Text style={styles.voiceHint}>Voice: {voiceHint}</Text>}

          <View style={styles.buttonRow}>
            <Button title="Begin Ritual" onPress={onAccept} />
            <Button title="Decline" color="#999" onPress={onDecline} />
          </View>

          <View style={styles.completeButton}>
            <Button title="Complete Reflection" color="#4CAF50" onPress={onComplete} />
          </View>
        </View>
      </View>
    </Modal>
  );
};

const styles = StyleSheet.create({
  overlay: {
    flex: 1,
    backgroundColor: 'rgba(10, 10, 10, 0.9)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  modalBox: {
    backgroundColor: '#202020',
    padding: 24,
    borderRadius: 12,
    width: '90%',
    maxWidth: 400,
  },
  title: {
    fontSize: 20,
    color: '#E0E0E0',
    marginBottom: 12,
    textAlign: 'center',
  },
  description: {
    fontSize: 16,
    color: '#AAAAAA',
    marginBottom: 16,
    textAlign: 'center',
  },
  voiceHint: {
    fontSize: 14,
    color: '#88C0D0',
    marginBottom: 16,
    textAlign: 'center',
  },
  buttonRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 16,
  },
  completeButton: {
    marginTop: 8,
  },
});

export default QuestModal;
