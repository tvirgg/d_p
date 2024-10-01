import React from 'react';
import './ContestCard.css';

const ContestCard = ({ contest }) => {
  const handleCopyLink = () => {
    navigator.clipboard.writeText('https://t.me/yourbot?start=referralCode');
    alert('Ссылка скопирована в буфер обмена!');
  };

  return (
    <div className="contest-card">
      <div className="contest-info">
        <h4>{contest.name}</h4>
        <p>{contest.participants} чел.</p>
        <p>Осталось: {contest.timeRemaining}</p>
      </div>
      <button onClick={handleCopyLink}>Копировать ссылку</button>
    </div>
  );
};

export default ContestCard;