import React, { useEffect, useState } from 'react';
import Header from '../components/Header';
import FooterNav from '../components/FooterNav';
import LeaderboardEntry from '../components/LeaderboardEntry';
import './Leaderboard.css';
import axios from 'axios';
import { useTelegram } from '../hooks/useTelegram';

const Leaderboard = () => {
  const { tg } = useTelegram();
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        const response = await axios.get('https://your-backend-api.com/leaderboard');
        setLeaderboard(response.data);
      } catch (error) {
        console.error(error);
        alert('Не удалось загрузить данные лидерборда.');
      }
    };

    fetchLeaderboard();
  }, []);

  return (
    <div className="page">
      <Header title="Referee Bot" />
      <div className="leaderboard-content">
        <h3>Лидерборд</h3>
        {leaderboard.map((entry, index) => (
          <LeaderboardEntry key={entry.userId} rank={index + 1} entry={entry} />
        ))}
      </div>
      <FooterNav />
    </div>
  );
};

export default Leaderboard;