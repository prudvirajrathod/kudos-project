import React, { useState, useEffect } from 'react';
import api from '../api/api';

function KudosReceivedList() {
  const [kudos, setKudos] = useState([]);

  useEffect(() => {
    api.get('kudos/received/').then(res => setKudos(res.data));
  }, []);

  return (
    <div>
      <h3>Kudos You Received</h3>
      {kudos.length === 0 && <div>No kudos received yet.</div>}
      <ul>
        {kudos.map(k => (
          <li key={k.id}>
            <strong>{k.giver.username}</strong> ({new Date(k.created_at).toLocaleString()}):<br />
            <em>{k.message}</em>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default KudosReceivedList;