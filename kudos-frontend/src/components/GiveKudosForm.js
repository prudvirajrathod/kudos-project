import React, { useState, useEffect } from 'react';
import api from '../api/api';

function GiveKudosForm({ onKudoGiven }) {
  const [users, setUsers] = useState([]);
  const [receiverId, setReceiverId] = useState('');
  const [message, setMessage] = useState('');
  const [remaining, setRemaining] = useState(0);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  useEffect(() => {
    api.get('users/').then(res => setUsers(res.data));
    api.get('kudos/remaining/').then(res => setRemaining(res.data.remaining));
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');
    if (!receiverId || !message) {
      setError('Please select a recipient and enter a message.');
      return;
    }
    try {
      await api.post('kudos/give/', { receiver_id: receiverId, message });
      setSuccess('Kudo sent!');
      setMessage('');
      setReceiverId('');
      api.get('kudos/remaining/').then(res => setRemaining(res.data.remaining));
      if (onKudoGiven) onKudoGiven();
    } catch (err) {
      setError(err.response?.data?.error || 'Error sending kudo.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h3>Give Kudos ({remaining} left this week)</h3>
      {error && <div style={{color: 'red'}}>{error}</div>}
      {success && <div style={{color: 'green'}}>{success}</div>}
      <select value={receiverId} onChange={e => setReceiverId(e.target.value)}>
        <option value="">Select recipient</option>
        {users.map(u => (
          <option key={u.id} value={u.id}>{u.username}</option>
        ))}
      </select>
      <br />
      <textarea
        placeholder="Why are you giving kudos?"
        value={message}
        onChange={e => setMessage(e.target.value)}
      />
      <br />
      <button type="submit" disabled={remaining === 0}>Send Kudos</button>
    </form>
  );
}

export default GiveKudosForm;