import React from 'react';

function UserInfo({ user }) {
  if (!user) return null;
  return (
    <div>
      <strong>Logged in as:</strong> {user.username} <br />
      <strong>Organization:</strong> {user.organization.name}
    </div>
  );
}

export default UserInfo;