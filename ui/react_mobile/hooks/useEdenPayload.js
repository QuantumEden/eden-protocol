// useEdenPayload.js – Eden Protocol Data Hook for Mobile App
// Handles payload fetch + parsing into modular component-ready format

import { useEffect, useState } from 'react';

export function useEdenPayload(simulate = false) {
  const [payload, setPayload] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchPayload() {
      try {
        if (simulate) {
          const mockModule = await import('../../../../sim/eden_payload_viewer');
          const allPayloads = mockModule.get_all_mock_payloads?.();
          const selected = Array.isArray(allPayloads) ? allPayloads[0] : null;
          setPayload(selected);
        } else {
          const response = await fetch('https://eden-api.yourdomain.com/payload');
          const data = await response.json();
          setPayload(data);
        }
      } catch (err) {
        console.error('Failed to load Eden payload:', err);
        setPayload(null);
      } finally {
        setLoading(false);
      }
    }

    fetchPayload();
  }, [simulate]);

  return { payload, loading };
}
