// ui/react_mobile/App.tsx
// Entry point for the EdenQuest Mobile App

import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import HomeScreen from './screens/HomeScreen';
import QuestScreen from './screens/QuestScreen';
import TreeScreen from './screens/TreeScreen';
import DAOScreen from './screens/DAOScreen';

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator
        initialRouteName="Home"
        screenOptions={{
          headerShown: false,
          animation: 'fade',
        }}
      >
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Quest" component={QuestScreen} />
        <Stack.Screen name="Tree" component={TreeScreen} />
        <Stack.Screen name="DAO" component={DAOScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
