import React from 'react';

export default function WorldTreeDashboard({ world_tree }) {
  if (!world_tree) return <div>Loading World Tree...</div>;

  return (
    <div style={{ padding: '24px' }}>
      <h2>🌐 World Tree Dashboard</h2>
      <p><strong>Symbolic State:</strong> {world_tree.symbolic_state}</p>
      <p><strong>Global Eden Health Index:</strong> {(world_tree.eden_health * 100).toFixed(1)}%</p>
      <p><strong>Active DAO Users:</strong> {world_tree.active_dao_users}</p>
    </div>
  );
}
