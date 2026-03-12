import React from 'react';
import { ThemeProvider } from './context/ThemeContext';
import Chat from './components/Chat';
import './App.css';

function App() {
  return (
    <ThemeProvider>
      <Chat />
    </ThemeProvider>
  );
}

export default App;