import React, { useState, useEffect } from 'react';
import { generateRandomThreat } from '../utils/mockData';
import './Dashboard.css';

const Dashboard = () => {
  const [threats, setThreats] = useState([]);
  const [stats, setStats] = useState({
    total: 0,
    high: 0,
    medium: 0,
    low: 0
  });

  useEffect(() => {
    // Initialize with some threats
    const initialThreats = Array.from({ length: 10 }, generateRandomThreat);
    setThreats(initialThreats);
    updateStats(initialThreats);

    // Auto-refresh every 10 seconds
    const interval = setInterval(() => {
      const newThreat = generateRandomThreat();
      setThreats(prev => [newThreat, ...prev].slice(0, 15)); // Keep last 15 threats
    }, 10000);

    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    updateStats(threats);
  }, [threats]);

  const updateStats = (threatList) => {
    const today = new Date().toDateString();
    const todayThreats = threatList.filter(t => 
      new Date(t.timestamp).toDateString() === today
    );

    setStats({
      total: todayThreats.length,
      high: todayThreats.filter(t => t.severity === 'High').length,
      medium: todayThreats.filter(t => t.severity === 'Medium').length,
      low: todayThreats.filter(t => t.severity === 'Low').length
    });
  };

  const getSeverityClass = (severity) => {
    switch(severity) {
      case 'High': return 'severity-high';
      case 'Medium': return 'severity-medium';
      case 'Low': return 'severity-low';
      default: return '';
    }
  };

  const getStatusClass = (status) => {
    switch(status) {
      case 'Blocked': return 'status-blocked';
      case 'Isolated': return 'status-isolated';
      case 'Monitoring': return 'status-monitoring';
      default: return '';
    }
  };

  return (
    <div className="dashboard">
      <h2 className="page-title">Dashboard Overview</h2>
      
      <div className="stats-grid">
        <div className="stat-card total">
          <div className="stat-icon">📊</div>
          <div className="stat-content">
            <h3>Total Threats Today</h3>
            <p className="stat-value">{stats.total}</p>
          </div>
        </div>
        <div className="stat-card high">
          <div className="stat-icon">🔴</div>
          <div className="stat-content">
            <h3>High Severity</h3>
            <p className="stat-value">{stats.high}</p>
          </div>
        </div>
        <div className="stat-card medium">
          <div className="stat-icon">🟡</div>
          <div className="stat-content">
            <h3>Medium Severity</h3>
            <p className="stat-value">{stats.medium}</p>
          </div>
        </div>
        <div className="stat-card low">
          <div className="stat-icon">🟢</div>
          <div className="stat-content">
            <h3>Low Severity</h3>
            <p className="stat-value">{stats.low}</p>
          </div>
        </div>
      </div>

      <div className="threats-section">
        <h3 className="section-title">
          Live Threats Monitor 
          <span className="live-indicator">● LIVE</span>
        </h3>
        <div className="table-container">
          <table className="threats-table">
            <thead>
              <tr>
                <th>Time</th>
                <th>Threat Type</th>
                <th>IP Address</th>
                <th>Severity</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {threats.map((threat) => (
                <tr key={threat.id}>
                  <td>{threat.time}</td>
                  <td>{threat.threatType}</td>
                  <td className="ip-address">{threat.ipAddress}</td>
                  <td>
                    <span className={`badge ${getSeverityClass(threat.severity)}`}>
                      {threat.severity}
                    </span>
                  </td>
                  <td>
                    <span className={`badge ${getStatusClass(threat.status)}`}>
                      {threat.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
