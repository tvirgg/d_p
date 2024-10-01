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