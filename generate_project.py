import os

# Определяем содержимое файлов
file_contents = {}

file_contents["src/index.js"] = """
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './App.css';

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
"""

file_contents["src/App.jsx"] = """
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

  useEffect(() => {
    tg.ready();
  }, [tg]);

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
"""

file_contents["src/hooks/useTelegram.js"] = """
import { useEffect } from 'react';

export function useTelegram() {
  const tg = window.Telegram.WebApp;

  useEffect(() => {
    tg.ready();
  }, [tg]);

  const onClose = () => {
    tg.close();
  };

  const onToggleMainButton = () => {
    if (tg.MainButton.isVisible) {
      tg.MainButton.hide();
    } else {
      tg.MainButton.show();
    }
  };

  return {
    tg,
    onClose,
    onToggleMainButton,
    user: tg.initDataUnsafe?.user,
  };
}
"""

# Компоненты
file_contents["src/components/Header.jsx"] = """
import React from 'react';
import './Header.css';

const Header = ({ title }) => {
  const handleBack = () => {
    window.history.back();
  };

  return (
    <header className="app-header">
      <button className="back-button" onClick={handleBack}>
        &larr; Назад
      </button>
      <h1>{title}</h1>
    </header>
  );
};

export default Header;
"""

file_contents["src/components/FooterNav.jsx"] = """
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
"""

file_contents["src/components/OnboardingStep.jsx"] = """
import React from 'react';
import './OnboardingStep.css';

const OnboardingStep = ({ stepNumber, imageSrc, title, description, onNext, onBack, isLast }) => {
  return (
    <div className="onboarding-step">
      <div className="step-indicator">
        Шаг {stepNumber} из 3
      </div>
      <img src={imageSrc} alt={title} className="onboarding-image" />
      <h2>{title}</h2>
      <p>{description}</p>
      <div className="onboarding-buttons">
        {stepNumber > 1 && <button onClick={onBack}>Назад</button>}
        <button onClick={onNext}>{isLast ? 'Начать' : 'Продолжить'}</button>
      </div>
    </div>
  );
};

export default OnboardingStep;
"""

file_contents["src/components/ContestCard.jsx"] = """
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
"""

file_contents["src/components/LeaderboardEntry.jsx"] = """
import React from 'react';
import './LeaderboardEntry.css';

const LeaderboardEntry = ({ rank, entry }) => {
  return (
    <div className={\`leaderboard-entry \${entry.isCurrentUser ? 'current-user' : ''}\`}>
      <span className="rank">{rank}</span>
      <span className="username">{entry.username}</span>
      <span className="referrals">{entry.referrals} чел.</span>
    </div>
  );
};

export default LeaderboardEntry;
"""

file_contents["src/components/AchievementCard.jsx"] = """
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
"""

# Страницы
file_contents["src/pages/Onboarding.jsx"] = """
import React, { useState } from 'react';
import OnboardingStep from '../components/OnboardingStep';
import step1Image from '../assets/step1.svg'; // Замените на ваши изображения
import step2Image from '../assets/step2.svg';
import step3Image from '../assets/step3.svg';
import './Onboarding.css';

const Onboarding = () => {
  const [currentStep, setCurrentStep] = useState(1);

  const steps = [
    {
      imageSrc: step1Image,
      title: 'Создайте вашу ссылку',
      description: 'Сгенерируйте уникальную реферальную ссылку, чтобы начать приглашать друзей.',
    },
    {
      imageSrc: step2Image,
      title: 'Пригласите друзей',
      description: 'Поделитесь своей ссылкой с друзьями, чтобы зарабатывать награды.',
    },
    {
      imageSrc: step3Image,
      title: 'Выигрывайте призы',
      description: 'Зарабатывайте баллы и выигрывайте призы, когда ваши друзья присоединяются.',
    },
  ];

  const handleNext = () => {
    if (currentStep < steps.length) {
      setCurrentStep((prev) => prev + 1);
    } else {
      localStorage.setItem('onboarded', 'true');
      window.location.href = '/home';
    }
  };

  const handleBack = () => {
    if (currentStep > 1) {
      setCurrentStep((prev) => prev - 1);
    }
  };

  const { imageSrc, title, description } = steps[currentStep - 1];

  return (
    <OnboardingStep
      stepNumber={currentStep}
      imageSrc={imageSrc}
      title={title}
      description={description}
      onNext={handleNext}
      onBack={handleBack}
      isLast={currentStep === steps.length}
    />
  );
};

export default Onboarding;
"""

file_contents["src/pages/Home.jsx"] = """
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
"""

file_contents["src/pages/Leaderboard.jsx"] = """
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
"""

file_contents["src/pages/Achievements.jsx"] = """
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
"""

# CSS файлы (можете добавить больше стилей по необходимости)
file_contents["src/App.css"] = """
body {
  background-color: #121212;
  color: #ffffff;
  margin: 0;
  font-family: Arial, sans-serif;
}

.page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.app-header, .footer-nav {
  background-color: #1f1f1f;
  padding: 10px;
}

.app-header h1, .footer-nav button {
  color: #ffffff;
}

.create-link-button {
  background-color: #ff8800;
  color: #ffffff;
  padding: 10px;
  border: none;
  border-radius: 5px;
}

.contest-card {
  background-color: #1e1e1e;
  padding: 15px;
  margin: 10px 0;
  border-radius: 5px;
}
"""

# Функция для создания файлов и папок
def create_files():
    for filepath, content in file_contents.items():
        # Создаем необходимые директории
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)
        # Записываем содержимое в файл
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content.strip())

if __name__ == "__main__":
    create_files()
    print("Файлы успешно созданы.")

