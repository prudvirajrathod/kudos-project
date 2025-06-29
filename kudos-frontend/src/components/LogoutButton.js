import React from 'react';
import api from '../api/api';

function LogoutButton({ onLogout }) {
  const handleLogout = async () => {
    await api.post('logout/');
    if (onLogout) onLogout();
  };

  return (
    <button onClick={handleLogout}>Logout</button>
  );
}

export default LogoutButton;