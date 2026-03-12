import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import Header from './Header';
import Footer from './Footer';
import { useTheme } from '../context/ThemeContext';
import './Chat.css';

const COMMANDS = [
  '/start <requirements>',
  '/show user_stories',
  '/show design',
  '/show code_generated',
  '/show test_results',
  '/rerun ba',
  '/rerun design',
  '/rerun dev',
  '/run_tests',
  '/status'
];

const Chat = () => {
  const { darkMode } = useTheme();
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [suggestions, setSuggestions] = useState([]);
  const messagesEndRef = useRef(null);
  const inputRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(scrollToBottom, [messages]);

  const handleInputChange = (e) => {
    const value = e.target.value;
    setInput(value);
    if (value.startsWith('/')) {
      const filtered = COMMANDS.filter(cmd => cmd.startsWith(value));
      setSuggestions(filtered);
    } else {
      setSuggestions([]);
    }
  };

  const sendMessage = async (msg = input) => {
    if (!msg.trim()) return;
    const userMsg = { 
      role: 'user', 
      content: msg, 
      timestamp: new Date().toLocaleTimeString() 
    };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setSuggestions([]);
    setLoading(true);

    try {
      const response = await axios.post('/api/chat', { message: msg });
      const botMsg = { 
        role: 'bot', 
        content: response.data.response, 
        timestamp: new Date().toLocaleTimeString(),
        isJson: response.data.response.includes('```json')
      };
      setMessages(prev => [...prev, botMsg]);
    } catch (error) {
      console.error('Error:', error);
      const errorMsg = { 
        role: 'bot', 
        content: '❌ Sorry, something went wrong.', 
        timestamp: new Date().toLocaleTimeString() 
      };
      setMessages(prev => [...prev, errorMsg]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const selectSuggestion = (cmd) => {
    setInput(cmd);
    setSuggestions([]);
    inputRef.current?.focus();
  };

  const formatMessage = (content) => {
    if (content.includes('```json')) {
      const parts = content.split('```json');
      return parts.map((part, i) => {
        if (i % 2 === 1) {
          const jsonPart = part.split('```')[0];
          try {
            const formatted = JSON.stringify(JSON.parse(jsonPart), null, 2);
            return <pre key={i} className="json-block">{formatted}</pre>;
          } catch {
            return <pre key={i} className="json-block">{jsonPart}</pre>;
          }
        } else {
          return <span key={i}>{part}</span>;
        }
      });
    }
    return content;
  };

  return (
    <div className={`chat-app ${darkMode ? 'dark' : 'light'}`}>
      <Header />
      <main className="chat-main">
        <div className="messages-container">
          {messages.map((msg, idx) => (
            <div key={idx} className={`message ${msg.role}`}>
              <div className="message-header">
                <span className="role">
                  {msg.role === 'user' ? '👤 You' : '🤖 SAMVIDA'}
                </span>
                <span className="time">{msg.timestamp}</span>
              </div>
              <div className="message-content">
                {formatMessage(msg.content)}
              </div>
            </div>
          ))}
          {loading && (
            <div className="message bot loading">
              <div className="message-header">
                <span className="role">🤖 SAMVIDA</span>
              </div>
              <div className="message-content">
                <div className="typing-indicator">
                  <span></span><span></span><span></span>
                </div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>
        {suggestions.length > 0 && (
          <div className="suggestions">
            {suggestions.map((cmd, i) => (
              <button key={i} onClick={() => selectSuggestion(cmd)} className="suggestion-chip">
                {cmd}
              </button>
            ))}
          </div>
        )}
        <div className="input-area">
          <textarea
            ref={inputRef}
            value={input}
            onChange={handleInputChange}
            onKeyPress={handleKeyPress}
            placeholder="Type a command (e.g., /start Build a task manager)"
            rows={1}
          />
          <button 
            onClick={() => sendMessage()} 
            disabled={loading || !input.trim()}
          >
            Send
          </button>
        </div>
      </main>
      <Footer />
    </div>
  );
};

export default Chat;