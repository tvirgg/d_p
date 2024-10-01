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