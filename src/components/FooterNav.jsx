import React from 'react';
import { useNavigate } from 'react-router-dom';
import './FooterNav.css';

const FooterNav = () => {
  const navigate = useNavigate();

  return (
    <nav className="footer-nav">
      <button onClick={() => navigate('/home')}>Главная</button>
      <button onClick={() => navigate('/leaderboard')}>Лидерборд</button>
      <button onClick={() => navigate('/achievements')}>Достижения</button>
    </nav>
  );
};

export default FooterNav;