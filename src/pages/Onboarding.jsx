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