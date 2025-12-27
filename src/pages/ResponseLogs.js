import React, { useState, useEffect } from 'react';
import { generateResponseLog } from '../utils/mockData';
import './ResponseLogs.css';

const ResponseLogs = () => {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    // Initialize logs
    const initialLogs = Array.from({ length: 30 }, generateResponseLog);
    setLogs(initialLogs);
  }, []);

  return (
    <div className="response-logs">
      <h2 className="page-title">Automated Response Logs</h2>
      
      <div className="content-card">
        <div className="logs-info">
          <span className="logs-count">Total Logs: {logs.length}</span>
          <span className="logs-status">🤖 AI-Powered Responses</span>
        </div>

        <div className="table-container">
          <table className="logs-table">
            <thead>
              <tr>
                <th>Time</th>
                <th>Action Taken</th>
                <th>Triggered By</th>
                <th>Source IP</th>
              </tr>
            </thead>
            <tbody>
              {logs.map((log) => (
                <tr key={log.id}>
                  <td>{log.time}</td>
                  <td className="action-cell">{log.action}</td>
                  <td>
                    <span className="threat-badge">{log.triggeredBy}</span>
                  </td>
                  <td className="ip-address">{log.ipAddress}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default ResponseLogs;
