import React, { useState, useEffect } from 'react';
import { nodes } from '../utils/mockData';
import './NodesMonitor.css';

const NodesMonitor = () => {
  const [lastSyncTime, setLastSyncTime] = useState(new Date().toLocaleString());

  useEffect(() => {
    const interval = setInterval(() => {
      setLastSyncTime(new Date().toLocaleString());
    }, 5000); // Update every 5 seconds

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="nodes-monitor">
      <h2 className="page-title">Nodes Monitor</h2>
      
      <div className="sync-info">
        <span className="sync-label">Last Sync Time:</span>
        <span className="sync-value">{lastSyncTime}</span>
      </div>

      <div className="nodes-grid">
        {nodes.map((node) => (
          <div key={node.id} className="node-card">
            <div className="node-header">
              <h3>{node.name}</h3>
              <span className={`node-status ${node.status.toLowerCase()}`}>
                ● {node.status}
              </span>
            </div>
            <div className="node-details">
              <div className="node-detail">
                <span className="detail-label">Location:</span>
                <span className="detail-value">{node.location}</span>
              </div>
              <div className="node-detail">
                <span className="detail-label">Node ID:</span>
                <span className="detail-value">NODE-{node.id.toString().padStart(3, '0')}</span>
              </div>
              <div className="node-detail">
                <span className="detail-label">Connection:</span>
                <span className="detail-value">Secure (TLS 1.3)</span>
              </div>
              <div className="node-detail">
                <span className="detail-label">Uptime:</span>
                <span className="detail-value">99.9%</span>
              </div>
            </div>
            <div className="node-metrics">
              <div className="metric">
                <span className="metric-label">CPU</span>
                <div className="metric-bar">
                  <div className="metric-fill" style={{width: `${45 + Math.random() * 20}%`}}></div>
                </div>
              </div>
              <div className="metric">
                <span className="metric-label">Memory</span>
                <div className="metric-bar">
                  <div className="metric-fill" style={{width: `${60 + Math.random() * 15}%`}}></div>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default NodesMonitor;
