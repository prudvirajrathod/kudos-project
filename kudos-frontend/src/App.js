import React, { useState, useEffect } from 'react';
import api from './api/api';
import LoginForm from './components/LoginForm';
import UserInfo from './components/UserInfo';
import GiveKudosForm from './components/GiveKudosForm';
import KudosReceivedList from './components/KudosReceivedList';
import KudosGivenList from './components/KudosGivenList';
import LogoutButton from './components/LogoutButton';

function App() {
  const [user, setUser] = useState(null);

  const fetchMe = async () => {
    try {
      const res = await api.get('me/');
      setUser(res.data);
    } catch {
      setUser(null);
    }
  };

  // useEffect(() => {
  //   fetchMe();
  // }, []);

  if (!user) {
    return <LoginForm onLogin={fetchMe} />;
  }

  return (
    <div>
      <UserInfo user={user} />
      <LogoutButton onLogout={() => setUser(null)} />
      <GiveKudosForm />
      <KudosReceivedList />
      <KudosGivenList />
    </div>
  );
}

export default App;