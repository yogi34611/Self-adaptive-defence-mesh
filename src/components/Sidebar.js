import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import './Sidebar.css';

const Sidebar = () => {
  const location = useLocation();

  const menuItems = [
    { path: '/', label: 'Dashboard', icon: '📊' },
    { path: '/live-threats', label: 'Live Threats', icon: '⚠️' },
    { path: '/threat-history', label: 'Threat History', icon: '📋' },
    { path: '/blockchain-ledger', label: 'Blockchain Ledger', icon: '⛓️' },
    { path: '/nodes-monitor', label: 'Nodes Monitor', icon: '🖥️' },
    { path: '/ai-model-status', label: 'AI Model Status', icon: '🤖' },
    { path: '/response-logs', label: 'Automated Response Logs', icon: '📝' }
  ];

  return (
    <aside className="sidebar">
      <nav className="sidebar-nav">
        {menuItems.map((item) => (
          <Link
            key={item.path}
            to={item.path}
            className={`sidebar-item ${location.pathname === item.path ? 'active' : ''}`}
          >
            <span className="sidebar-icon">{item.icon}</span>
            <span className="sidebar-label">{item.label}</span>
          </Link>
        ))}
      </nav>
    </aside>
  );
};

export default Sidebar;
