import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import LiveThreats from './pages/LiveThreats';
import ThreatHistory from './pages/ThreatHistory';
import BlockchainLedger from './pages/BlockchainLedger';
import NodesMonitor from './pages/NodesMonitor';
import AIModelStatus from './pages/AIModelStatus';
import ResponseLogs from './pages/ResponseLogs';
import './App.css';

function App() {
  return (
    <Router>
      <div className="app">
        <Header />
        <div className="app-body">
          <Sidebar />
          <main className="main-content">
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/live-threats" element={<LiveThreats />} />
              <Route path="/threat-history" element={<ThreatHistory />} />
              <Route path="/blockchain-ledger" element={<BlockchainLedger />} />
              <Route path="/nodes-monitor" element={<NodesMonitor />} />
              <Route path="/ai-model-status" element={<AIModelStatus />} />
              <Route path="/response-logs" element={<ResponseLogs />} />
            </Routes>
          </main>
        </div>
      </div>
    </Router>
  );
}

export default App;
