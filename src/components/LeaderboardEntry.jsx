import React from 'react';
import './LeaderboardEntry.css';

const LeaderboardEntry = ({ rank, entry }) => {
  return (
    <div className={`leaderboard-entry ${entry.isCurrentUser ? 'current-user' : ''}`}>
      <span className="rank">{rank}</span>
      <span className="username">{entry.username}</span>
      <span className="referrals">{entry.referrals} чел.</span>
    </div>
  );
};

export default LeaderboardEntry;