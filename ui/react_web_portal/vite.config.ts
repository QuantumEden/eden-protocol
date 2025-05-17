// vite.config.ts – Eden Protocol React Web Portal (Vite + TypeScript)

import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    open: true,
  },
  resolve: {
    alias: {
      '@components': '/src/components',
      '@pages': '/src/pages',
      '@utils': '/src/utils',
    },
  },
  build: {
    outDir: 'dist',
    sourcemap: true,
  }
});
