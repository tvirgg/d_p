import React, { useState } from 'react';
import Header from '../components/Header';
import FooterNav from '../components/FooterNav';
import ContestCard from '../components/ContestCard';
import './Home.css';
import { useTelegram } from '../hooks/useTelegram';
import axios from 'axios';

const Home = () => {
  const { tg } = useTelegram();
  const [contests, setContests] = useState([
    {
      id: 1,
      name: 'Конкурс 1',
      participants: 914,
      timeRemaining: '2 дня',
    },
    // Добавьте больше конкурсов по мере необходимости
  ]);

  const handleCreateLink = async () => {
    try {
      const response = await axios.post('https://your-backend-api.com/generate-link', {
        userId: tg.initDataUnsafe?.user?.id,
      });
      const referralLink = response.data.link;
      tg.sendData(JSON.stringify({ action: 'create_link', link: referralLink }));
      alert('Ваша реферальная ссылка сгенерирована и отправлена боту.');
    } catch (error) {
      console.error(error);
      alert('Не удалось сгенерировать реферальную ссылку.');
    }
  };

  return (
    <div className="page">
      <Header title="Referee Bot" />
      <div className="home-content">
        <h2>Привет! 👋</h2>
        <button className="create-link-button" onClick={handleCreateLink}>
          Создать ссылку
        </button>
        <h3>Активные Конкурсы</h3>
        {contests.map((contest) => (
          <ContestCard key={contest.id} contest={contest} />
        ))}
      </div>
      <FooterNav />
    </div>
  );
};

export default Home;