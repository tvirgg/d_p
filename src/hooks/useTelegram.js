// import { useEffect } from 'react';

// export function useTelegram() {
//   const tg = window.Telegram.WebApp;

//   useEffect(() => {
//     tg.ready();
//   }, [tg]);

//   const onClose = () => {
//     tg.close();
//   };

//   const onToggleMainButton = () => {
//     if (tg.MainButton.isVisible) {
//       tg.MainButton.hide();
//     } else {
//       tg.MainButton.show();
//     }
//   };

//   return {
//     tg,
//     onClose,
//     onToggleMainButton,
//     user: tg.initDataUnsafe?.user,
//   };
// }
import { useEffect } from 'react';

// Проверяем, находимся ли мы в режиме разработки
const isDev = process.env.NODE_ENV === 'development';

export function useTelegram() {
  const tg = window.Telegram?.WebApp; // Проверяем наличие Telegram WebApp

  useEffect(() => {
    if (tg) {
      tg.ready();
    } else if (isDev) {
      console.warn("Работаем в режиме разработки, Telegram WebApp не найден.");
    }
  }, [tg]);

  const onClose = () => {
    if (tg) tg.close();
  };

  const onToggleMainButton = () => {
    if (tg?.MainButton) {
      if (tg.MainButton.isVisible) {
        tg.MainButton.hide();
      } else {
        tg.MainButton.show();
      }
    }
  };

  return {
    tg,
    onClose,
    onToggleMainButton,
    user: tg?.initDataUnsafe?.user || { id: "12345", username: "DevUser" }, // Фоллбэк для тестирования
  };
}
