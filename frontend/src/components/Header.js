import React from 'react';
import ThemeToggle from './ThemeToggle';
import './Header.css';

const Header = () => {
  return (
    <header className="app-header">
      <div className="logo-container">
        <img src="/samvida-logo.png" alt="SAMVIDA" className="logo" /> 
        {/* or use an emoji fallback: <span className="logo-emoji">🤖</span> */}
        <h1>SAMVIDA</h1>
      </div>
      <ThemeToggle />
    </header>
  );
};

export default Header;