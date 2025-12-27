import React, { useState, useEffect } from 'react';
import './Header.css';

const Header = () => {
  const [lastScanTime, setLastScanTime] = useState(new Date().toLocaleTimeString());

  useEffect(() => {
    const interval = setInterval(() => {
      setLastScanTime(new Date().toLocaleTimeString());
    }, 5000); // Update every 5 seconds

    return () => clearInterval(interval);
  }, []);

  return (
    <header className="header">
      <div className="header-title">
        <h1>🛡️ Self-Adaptive Cyber Defense Mesh</h1>
        <p className="header-subtitle">Cognitive AI + Blockchain Security [STUDENT DEMO]</p>
      </div>
      <div className="header-status">
        <div className="status-item">
          <span className="status-label">System Status:</span>
          <span className="status-value online">● ONLINE</span>
        </div>
        <div className="status-item">
          <span className="status-label">AI Model:</span>
          <span className="status-value running">● RUNNING</span>
        </div>
        <div className="status-item">
          <span className="status-label">Blockchain:</span>
          <span className="status-value connected">● CONNECTED</span>
        </div>
        <div className="status-item">
          <span className="status-label">Active Nodes:</span>
          <span className="status-value">3</span>
        </div>
        <div className="status-item">
          <span className="status-label">Last Scan:</span>
          <span className="status-value">{lastScanTime}</span>
        </div>
      </div>
    </header>
  );
};

export default Header;
