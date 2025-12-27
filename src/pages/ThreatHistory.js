import React, { useState, useEffect } from 'react';
import { generateRandomThreat } from '../utils/mockData';
import './ThreatHistory.css';

const ThreatHistory = () => {
  const [threats, setThreats] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [severityFilter, setSeverityFilter] = useState('All');

  useEffect(() => {
    // Generate historical threats
    const historicalThreats = Array.from({ length: 50 }, generateRandomThreat);
    setThreats(historicalThreats);
  }, []);

  const filteredThreats = threats.filter(threat => {
    const matchesSearch = 
      threat.ipAddress.toLowerCase().includes(searchTerm.toLowerCase()) ||
      threat.threatType.toLowerCase().includes(searchTerm.toLowerCase());
    
    const matchesSeverity = severityFilter === 'All' || threat.severity === severityFilter;
    
    return matchesSearch && matchesSeverity;
  });

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
    <div className="threat-history">
      <h2 className="page-title">Threat History</h2>
      
      <div className="content-card">
        <div className="filters">
          <input
            type="text"
            placeholder="Search by IP or Threat Type..."
            className="search-input"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
          <select
            className="severity-filter"
            value={severityFilter}
            onChange={(e) => setSeverityFilter(e.target.value)}
          >
            <option value="All">All Severities</option>
            <option value="High">High</option>
            <option value="Medium">Medium</option>
            <option value="Low">Low</option>
          </select>
        </div>

        <div className="results-info">
          Showing {filteredThreats.length} of {threats.length} threats
        </div>

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
              {filteredThreats.map((threat) => (
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

export default ThreatHistory;
