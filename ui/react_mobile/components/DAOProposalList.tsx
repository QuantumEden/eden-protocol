// DAOProposalList.tsx – Symbolic Proposal Viewer for EdenQuest DAO (Mobile)

import React from 'react';
import { View, Text, FlatList, StyleSheet, TouchableOpacity } from 'react-native';

type Proposal = {
  id: string;
  title: string;
  description: string;
  proposer_glyph: string;
  merit_score: number;
};

interface DAOProposalListProps {
  proposals: Proposal[];
  onSelect: (id: string) => void;
}

const DAOProposalList: React.FC<DAOProposalListProps> = ({ proposals, onSelect }) => {
  const renderItem = ({ item }: { item: Proposal }) => (
    <TouchableOpacity style={styles.card} onPress={() => onSelect(item.id)}>
      <Text style={styles.title}>{item.title}</Text>
      <Text style={styles.description} numberOfLines={2}>
        {item.description}
      </Text>
      <View style={styles.footer}>
        <Text style={styles.glyph}>{item.proposer_glyph}</Text>
        <Text style={styles.merit}>Merit: {item.merit_score}</Text>
      </View>
    </TouchableOpacity>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.header}>🗳️ Symbolic Proposals</Text>
      <FlatList
        data={proposals}
        keyExtractor={(item) => item.id}
        renderItem={renderItem}
        ListEmptyComponent={<Text style={styles.empty}>No active proposals.</Text>}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    paddingHorizontal: 12,
    paddingVertical: 10,
  },
  header: {
    fontSize: 18,
    color: '#fff',
    fontWeight: '600',
    marginBottom: 8,
    textAlign: 'center',
  },
  card: {
    backgroundColor: '#222',
    borderRadius: 8,
    padding: 12,
    marginBottom: 10,
    shadowColor: '#000',
    shadowOpacity: 0.2,
    shadowOffset: { width: 0, height: 1 },
  },
  title: {
    color: '#fff',
    fontWeight: '600',
    fontSize: 16,
  },
  description: {
    color: '#aaa',
    marginTop: 4,
    fontSize: 13,
  },
  footer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginTop: 10,
  },
  glyph: {
    fontSize: 20,
  },
  merit: {
    fontSize: 13,
    color: '#6cf',
  },
  empty: {
    color: '#777',
    textAlign: 'center',
    marginTop: 16,
    fontStyle: 'italic',
  },
});

export default DAOProposalList;
