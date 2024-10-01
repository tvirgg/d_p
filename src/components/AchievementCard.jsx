import React from 'react';
import './AchievementCard.css';

const AchievementCard = ({ achievement }) => {
  return (
    <div className="achievement-card">
      <div className="reward">{achievement.reward}</div>
      <div className="achievement-info">
        <h4>{achievement.title}</h4>
        <p>{achievement.description}</p>
      </div>
    </div>
  );
};

export default AchievementCard;