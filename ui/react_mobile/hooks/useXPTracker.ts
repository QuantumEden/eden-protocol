// ui/react_mobile/hooks/useXPTracker.ts
// Optional hook for tracking XP state transitions and sync behavior

import { useState, useEffect } from 'react';

interface XPTrackerOptions {
  xp: number;
  locked: boolean;
  threshold: number;
}

interface XPTrackerState {
  status: 'idle' | 'level_up' | 'locked' | 'ready';
  message: string;
  percent: number;
}

export function useXPTracker({ xp, locked, threshold }: XPTrackerOptions): XPTrackerState {
  const [status, setStatus] = useState<'idle' | 'level_up' | 'locked' | 'ready'>('idle');
  const [message, setMessage] = useState<string>('Awaiting sync...');
  const [percent, setPercent] = useState<number>(0);

  useEffect(() => {
    if (locked) {
      setStatus('locked');
      setMessage('XP is locked – Realignment Required');
      setPercent(0);
      return;
    }

    const progress = Math.min(Math.round((xp / threshold) * 100), 100);
    setPercent(progress);

    if (progress >= 100) {
      setStatus('level_up');
      setMessage('Level Up Available');
    } else if (progress > 0) {
      setStatus('ready');
      setMessage(`${progress}% toward next level`);
    } else {
      setStatus('idle');
      setMessage('No XP earned yet');
    }
  }, [xp, locked, threshold]);

  return { status, message, percent };
}
