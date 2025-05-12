import React, { useState } from 'react';
import TreeHUD from './tree_hud';
import QuestJournal from './quest_journal';
import AuraRing from './aura_ring';
import DAOAlerts from './dao_alerts';

export default function NavRouter({ payload }) {
  const [screen, setScreen] = useState("tree");

  const renderScreen = () => {
    switch (screen) {
      case "tree": return <TreeHUD tree={payload.tree_of_life} />;
      case "quest": return <QuestJournal edenquest={payload.edenquest} />;
      case "aura": return <AuraRing auraColor={payload.avatar.aura_color} glyph={payload.avatar.glyph} />;
      case "dao": return <DAOAlerts dao={payload.dao} />;
      default: return <TreeHUD tree={payload.tree_of_life} />;
    }
  };

  return (
    <div>
      <nav style={{ display: 'flex', justifyContent: 'space-around', padding: '8px' }}>
        <button onClick={() => setScreen("tree")}>🌳 Tree</button>
        <button onClick={() => setScreen("quest")}>📜 Quest</button>
        <button onClick={() => setScreen("aura")}>💠 Aura</button>
        <button onClick={() => setScreen("dao")}>🗳 DAO</button>
      </nav>
      <div>{renderScreen()}</div>
    </div>
  );
}
