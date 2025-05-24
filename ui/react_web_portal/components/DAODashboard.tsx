// DAODashboard.tsx – Eden Protocol DAO Interface (Web Portal)

import React, { useState } from 'react';
import { View, Text, StyleSheet, Button, FlatList } from 'react-native';

// 🧠 Mock DAO proposals
const mockProposals = [
  {
    id: 'prop-001',
    title: 'Initiate Verdant Ritual of Renewal',
    summary: 'Symbolic mass realignment quest to restore global resilience.',
    requiredLevel: 7,
    proposer: 'seer_011',
    soulbound: true,
    ritual_verified: true,
    zkxp_hash: 'zkxp-prop-001'
  },
  {
    id: 'prop-002',
    title: 'Open Soulform Submission Mod Registry',
    summary: 'Allow new forms from modders with lore and XP verification.',
    requiredLevel: 9,
    proposer: 'healer_022',
    soulbound: true,
    ritual_verified: false,
    zkxp_hash: 'zkxp-prop-002'
  }
];

// 🪙 Simulated voter payload (would be fetched in real use)
const userMerit = {
  user_id: 'warrior_033',
  level: 8,
  soulform: 'dragon',
  conviction_glyph: '🜁'
};

const DAODashboard = () => {
  const [voted, setVoted] = useState<string[]>([]);

  const handleVote = (id: string) => {
    if (!voted.includes(id)) {
      setVoted([...voted, id]);
    }
  };

  const renderProposal = ({ item }: { item: typeof mockProposals[0] }) => {
    const eligible = userMerit.level >= item.requiredLevel;
    const alreadyVoted = voted.includes(item.id);

    return (
      <View style={styles.card}>
        <Text style={styles.title}>{item.title}</Text>
        <Text style={styles.summary}>{item.summary}</Text>
        <Text style={styles.meta}>
          Proposed by: {item.proposer} {item.soulbound ? '🧬' : ''}
        </Text>
        <Text style={styles.meta}>Required Level: {item.requiredLevel}</Text>
        <Text style={styles.meta}>
          Ritual Verified: {item.ritual_verified ? '🕊️ Yes' : '⚠️ No'}
        </Text>
        <Text style={styles.meta}>zkXP Hash: {item.zkxp_hash}</Text>

        {eligible ? (
          alreadyVoted ? (
            <Text style={styles.voted}>Vote cast. 🗳️</Text>
          ) : (
            <Button title="Cast Vote" onPress={() => handleVote(item.id)} />
          )
        ) : (
          <Text style={styles.locked}>Insufficient Merit Level</Text>
        )}
      </View>
    );
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>DAO Proposal Chamber</Text>
      <FlatList
        data={mockProposals}
        renderItem={renderProposal}
        keyExtractor={(item) => item.id}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 24,
    backgroundColor: '#111',
    height: '100%',
  },
  header: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#F0F0F0',
    marginBottom: 16,
    textAlign: 'center',
  },
  card: {
    backgroundColor: '#1E1E1E',
    padding: 16,
    borderRadius: 10,
    marginBottom: 18,
  },
  title: {
    fontSize: 18,
    fontWeight: '600',
    color: '#FFEB3B',
    marginBottom: 6,
  },
  summary: {
    fontSize: 14,
    color: '#CCCCCC',
    marginBottom: 6,
  },
  meta: {
    fontSize: 12,
    color: '#888888',
  },
  voted: {
    marginTop: 8,
    color: '#66BB6A',
    fontWeight: '600',
  },
  locked: {
    marginTop: 8,
    color: '#FF7043',
    fontWeight: '600',
  }
});

export default DAODashboard;
