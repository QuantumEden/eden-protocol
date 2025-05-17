// ui/react_web_portal/main.tsx
// Entry point for Eden Protocol React Web Portal (Vite + React + TypeScript)

import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import HomePage from './pages/index';
import DAOPortal from './pages/dao';
import AvatarPage from './pages/avatar';
import WorldTreePage from './pages/worldtree';

import './styles/global.css';

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);

root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/dao" element={<DAOPortal />} />
        <Route path="/avatar" element={<AvatarPage />} />
        <Route path="/worldtree" element={<WorldTreePage />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
