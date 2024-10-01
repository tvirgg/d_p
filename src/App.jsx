import React, { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Onboarding from './pages/Onboarding';
import Home from './pages/Home';
import Leaderboard from './pages/Leaderboard';
import Achievements from './pages/Achievements';
import { useTelegram } from './hooks/useTelegram';

const App = () => {
  const { tg } = useTelegram();
  const isOnboarded = localStorage.getItem('onboarded');

  // useEffect(() => {
  //   tg.ready();
  // }, [tg]);

  return (
    <Router>
      <Routes>
        {!isOnboarded && (
          <Route path="/" element={<Onboarding />} />
        )}
        <Route path="/home" element={<Home />} />
        <Route path="/leaderboard" element={<Leaderboard />} />
        <Route path="/achievements" element={<Achievements />} />
        <Route path="*" element={<Navigate to={isOnboarded ? "/home" : "/"} />} />
      </Routes>
    </Router>
  );
};

export default App;