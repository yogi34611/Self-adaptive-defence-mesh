import React, { useState, useEffect } from 'react';
import './LiveThreats.css';

const API_BASE = 'http://localhost:5001/api';

const LiveThreats = () => {
  const [threats, setThreats] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [showSuccess, setShowSuccess] = useState(false);
  const [formData, setFormData] = useState({
    ip: '',
    threatType: 'DDoS Attack',
    severity: 'High',
    description: '',
    protocol: 'TCP',
    port: '80'
  });

  // Fetch threats from backend
  const fetchThreats = async () => {
    try {
      const response = await fetch(`${API_BASE}/live-threats`);
      const data = await response.json();
      if (data.success) {
        setThreats(data.threats);
      }
      setLoading(false);
    } catch (error) {
      console.error('Error fetching threats:', error);
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchThreats();
    // Auto-refresh every 5 seconds
    const interval = setInterval(fetchThreats, 5000);
    return () => clearInterval(interval);
  }, []);

  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      const response = await fetch(`${API_BASE}/submit-threat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
      });

      const data = await response.json();
      
      if (data.success) {
        setShowSuccess(true);
        setShowForm(false);
        setFormData({
          ip: '',
          threatType: 'DDoS Attack',
          severity: 'High',
          description: '',
          protocol: 'TCP',
          port: '80'
        });
        
        // Hide success popup after 4 seconds
        setTimeout(() => setShowSuccess(false), 4000);
        
        // Refresh threats
        fetchThreats();
      }
    } catch (error) {
      console.error('Error submitting threat:', error);
      alert('Failed to submit threat. Please try again.');
    }
  };

  const generateReport = async () => {
    try {
      const response = await fetch(`${API_BASE}/reports/generate/live-threats`, {
        method: 'POST'
      });
      
      if (response.ok) {
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `live_threats_report_${new Date().getTime()}.pdf`;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
      }
    } catch (error) {
      console.error('Error generating report:', error);
      alert('Failed to generate report');
    }
  };

  const getSeverityClass = (severity) => {
    switch(severity) {
      case 'Critical': return 'severity-critical';
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
      case 'Mitigated': return 'status-mitigated';
      default: return '';
    }
  };

  return (
    <div className="live-threats">
      <div className="page-header">
        <h2 className="page-title">Live Threats Monitor</h2>
        <div className="header-actions">
          <span className="live-badge">● LIVE</span>
          <button className="btn-submit-threat" onClick={() => setShowForm(true)}>
            + Submit Threat
          </button>
          <button className="btn-generate-report" onClick={generateReport}>
            📄 Export PDF
          </button>
        </div>
      </div>

      {/* Success Popup */}
      {showSuccess && (
        <div className="success-popup">
          <div className="success-content">
            <div className="success-icon">✅</div>
            <h3>Threat Submitted Successfully!</h3>
            <p>Your threat is now being monitored by the system.</p>
            <p className="success-detail">Blockchain block created & response initiated</p>
          </div>
        </div>
      )}

      {/* Threat Submission Form Modal */}
      {showForm && (
        <div className="modal-overlay" onClick={() => setShowForm(false)}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <div className="modal-header">
              <h3>Submit New Threat for Monitoring</h3>
              <button className="modal-close" onClick={() => setShowForm(false)}>×</button>
            </div>
            
            <form onSubmit={handleSubmit} className="threat-form">
              <div className="form-group">
                <label>IP Address *</label>
                <input
                  type="text"
                  name="ip"
                  value={formData.ip}
                  onChange={handleInputChange}
                  placeholder="e.g., 192.168.1.100"
                  pattern="^(\d{1,3}\.){3}\d{1,3}$"
                  required
                />
              </div>

              <div className="form-group">
                <label>Threat Type *</label>
                <select name="threatType" value={formData.threatType} onChange={handleInputChange} required>
                  <option value="DDoS Attack">DDoS Attack</option>
                  <option value="SQL Injection">SQL Injection</option>
                  <option value="XSS Attack">XSS Attack</option>
                  <option value="Brute Force">Brute Force</option>
                  <option value="Malware Detection">Malware Detection</option>
                  <option value="Port Scanning">Port Scanning</option>
                  <option value="Phishing Attempt">Phishing Attempt</option>
                  <option value="Ransomware">Ransomware</option>
                  <option value="Data Exfiltration">Data Exfiltration</option>
                </select>
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label>Severity *</label>
                  <select name="severity" value={formData.severity} onChange={handleInputChange} required>
                    <option value="Critical">Critical</option>
                    <option value="High">High</option>
                    <option value="Medium">Medium</option>
                    <option value="Low">Low</option>
                  </select>
                </div>

                <div className="form-group">
                  <label>Protocol</label>
                  <select name="protocol" value={formData.protocol} onChange={handleInputChange}>
                    <option value="TCP">TCP</option>
                    <option value="UDP">UDP</option>
                    <option value="HTTP">HTTP</option>
                    <option value="HTTPS">HTTPS</option>
                  </select>
                </div>

                <div className="form-group">
                  <label>Port</label>
                  <input
                    type="number"
                    name="port"
                    value={formData.port}
                    onChange={handleInputChange}
                    min="1"
                    max="65535"
                  />
                </div>
              </div>

              <div className="form-group">
                <label>Description</label>
                <textarea
                  name="description"
                  value={formData.description}
                  onChange={handleInputChange}
                  placeholder="Additional details about the threat..."
                  rows="3"
                />
              </div>

              <div className="form-actions">
                <button type="button" className="btn-cancel" onClick={() => setShowForm(false)}>
                  Cancel
                </button>
                <button type="submit" className="btn-submit">
                  Submit & Monitor
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
      
      <div className="content-card">
        {loading ? (
          <div className="loading">Loading threats...</div>
        ) : (
          <div className="table-container">
            <table className="threats-table">
              <thead>
                <tr>
                  <th>Threat ID</th>
                  <th>Type</th>
                  <th>Severity</th>
                  <th>Source IP</th>
                  <th>Protocol</th>
                  <th>Node</th>
                  <th>Status</th>
                  <th>Timestamp</th>
                </tr>
              </thead>
              <tbody>
                {threats.map((threat, index) => (
                  <tr key={index} className={threat.userSubmitted ? 'user-submitted' : ''}>
                    <td>
                      {threat.threatId}
                      {threat.userSubmitted && <span className="user-badge">👤</span>}
                    </td>
                    <td>{threat.type}</td>
                    <td><span className={`badge ${getSeverityClass(threat.severity)}`}>{threat.severity}</span></td>
                    <td className="ip-address">{threat.ip}</td>
                    <td>{threat.protocol}</td>
                    <td>{threat.nodeId}</td>
                    <td><span className={`badge ${getStatusClass(threat.status)}`}>{threat.status}</span></td>
                    <td className="timestamp-cell">{new Date(threat.timestamp).toLocaleString()}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
};

export default LiveThreats;
