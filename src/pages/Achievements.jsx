import React, { useEffect, useState } from 'react';
import Header from '../components/Header';
import FooterNav from '../components/FooterNav';
import AchievementCard from '../components/AchievementCard';
import './Achievements.css';
import axios from 'axios';
import { useTelegram } from '../hooks/useTelegram';

const Achievements = () => {
  const { tg } = useTelegram();
  const [achievements, setAchievements] = useState([]);

  useEffect(() => {
    const fetchAchievements = async () => {
      try {
        const response = await axios.get('https://your-backend-api.com/achievements', {
          params: { userId: tg.initDataUnsafe?.user?.id }
        });
        setAchievements(response.data);
      } catch (error) {
        console.error(error);
        alert('Не удалось загрузить данные о достижениях.');
      }
    };

    fetchAchievements();
  }, []);

  return (
    <div className="page">
      <Header title="Referee Bot" />
      <div className="achievements-content">
        <h3>Достижения</h3>
        {achievements.map((achievement) => (
          <AchievementCard key={achievement.id} achievement={achievement} />
        ))}
      </div>
      <FooterNav />
    </div>
  );
};

export default Achievements;