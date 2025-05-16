// ui/react_web_portal/App.tsx
// Root navigation + layout shell for Eden Web Portal (Next.js or SPA-compatible)

import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

import HomePage from './pages/index';
import DAOPortal from './pages/dao';
import AvatarPage from './pages/avatar';
import WorldTreePage from './pages/worldtree';

const App: React.FC = () => {
  return (
    <Router>
      <div style={styles.shell}>
        <nav style={styles.nav}>
          <Link style={styles.link} to="/">🌱 Home</Link>
          <Link style={styles.link} to="/avatar">🧬 Avatar</Link>
          <Link style={styles.link} to="/dao">🗳️ DAO</Link>
          <Link style={styles.link} to="/worldtree">🌍 World Tree</Link>
        </nav>
        <main style={styles.main}>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/avatar" element={<AvatarPage />} />
            <Route path="/dao" element={<DAOPortal />} />
            <Route path="/worldtree" element={<WorldTreePage />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
};

const styles: { [key: string]: React.CSSProperties } = {
  shell: {
    minHeight: '100vh',
    backgroundColor: '#0d0d0d',
    fontFamily: 'inherit',
    color: '#eee'
  },
  nav: {
    display: 'flex',
    justifyContent: 'center',
    gap: '2rem',
    padding: '1rem 0',
    borderBottom: '1px solid #333',
    backgroundColor: '#111'
  },
  link: {
    color: '#9ef',
    textDecoration: 'none',
    fontWeight: 'bold'
  },
  main: {
    padding: '2rem',
    maxWidth: '1000px',
    margin: '0 auto'
  }
};

export default App;
