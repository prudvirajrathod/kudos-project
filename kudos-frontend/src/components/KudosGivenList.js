import React, { useState, useEffect } from 'react';
import api from '../api/api';

function KudosGivenList() {
  const [kudos, setKudos] = useState([]);

  useEffect(() => {
    api.get('kudos/given/').then(res => setKudos(res.data));
  }, []);

  return (
    <div>
      <h3>Kudos You Gave</h3>
      {kudos.length === 0 && <div>No kudos given yet.</div>}
      <ul>
        {kudos.map(k => (
          <li key={k.id}>
            <strong>{k.receiver.username}</strong> ({new Date(k.created_at).toLocaleString()}):<br />
            <em>{k.message}</em>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default KudosGivenList;