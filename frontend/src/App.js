import React from 'react';
import LoginForm from './components/LoginForm';
import RegistrationForm from './components/RegistrationForm';
import './App.css';

function App() {
  return (
    <div className="App">
      <h1>Welcome to Your Game Stats Application</h1>
      <LoginForm />
      <RegistrationForm />
    </div>
  );
}

export default App;
