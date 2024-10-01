```markdown
# Telegram Referral Mini App

## Table of Contents
1. [Project Structure](#project-structure)
2. [Getting Started](#getting-started)
3. [APIs & Backend Requirements](#apis--backend-requirements)

## Project Structure
```
src/
├── components/
│   ├── Header.jsx
│   ├── FooterNav.jsx
│   ├── OnboardingStep.jsx
│   ├── ContestCard.jsx
│   ├── LeaderboardEntry.jsx
│   ├── AchievementCard.jsx
├── pages/
│   ├── Onboarding.jsx
│   ├── Home.jsx
│   ├── Leaderboard.jsx
│   ├── Achievements.jsx
├── hooks/
│   └── useTelegram.js
├── App.jsx
├── index.js
├── styles/
│   ├── Header.css
│   ├── FooterNav.css
│   ├── OnboardingStep.css
│   ├── ContestCard.css
│   ├── LeaderboardEntry.css
│   ├── AchievementCard.css
│   ├── Onboarding.css
│   ├── Home.css
│   ├── Leaderboard.css
│   ├── Achievements.css
├── assets/
│   ├── step1.svg
│   ├── step2.svg
│   ├── step3.svg
```

## Getting Started

### Prerequisites
- [Node.js](https://nodejs.org/)
- [npm](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install the dependencies:
   ```bash
   npm install
   ```
   or
   ```bash
   yarn install
   ```

### Running the Development Server
```bash
npm start
```
or
```bash
yarn start
```
This will start the development server on [http://localhost:3000](http://localhost:3000).

### Building the Project for Production
```bash
npm run build
```
or
```bash
yarn build
```
This will create an optimized build of the app in the `build` folder.

## APIs & Backend Requirements
The frontend relies on several API endpoints for its features. Below are the endpoints and the data format expected:

1. **Referral Link Generation**
   - **Endpoint:** `POST /generate-link`
   - **Body:** `{ "userId": "<telegram_user_id>" }`
   - **Response:** `{ "link": "<generated_referral_link>" }`

2. **Leaderboard Data**
   - **Endpoint:** `GET /leaderboard`
   - **Response Format:**
     ```json
     [
       { "userId": "1", "username": "user1", "referrals": 10 },
       { "userId": "2", "username": "user2", "referrals": 8 }
     ]
     ```

3. **Achievements Data**
   - **Endpoint:** `GET /achievements`
   - **Response Format:**
     ```json
     [
       { "id": "1", "reward": "Reward Name", "title": "Achievement Title", "description": "Achievement Description" }
     ]
     ```

4. **Contest Data**
   - **Endpoint:** Embedded in frontend state; must be provided to `Home.jsx`.

## Debugging
When debugging this project, it must be tested in the context of Telegram to access the `window.Telegram.WebApp` object. You can use these options:
- [Android Debugging](https://developers.chrome.com/docs/devtools/remote-debugging/)
- [Telegram Desktop Beta](https://desktop.telegram.org/)
```
