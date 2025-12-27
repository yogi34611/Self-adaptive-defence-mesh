import React, { useState, useEffect } from 'react';
import { generateBlockchainBlock } from '../utils/mockData';
import './BlockchainLedger.css';

const BlockchainLedger = () => {
  const [blocks, setBlocks] = useState([]);

  useEffect(() => {
    // Initialize blockchain blocks
    const initialBlocks = Array.from({ length: 20 }, (_, i) => 
      generateBlockchainBlock(i + 1)
    );
    setBlocks(initialBlocks);
  }, []);

  return (
    <div className="blockchain-ledger">
      <h2 className="page-title">Blockchain Ledger</h2>
      
      <div className="consensus-info">
        <div className="consensus-card">
          <span className="consensus-label">Consensus Mechanism:</span>
          <span className="consensus-value">PBFT (Practical Byzantine Fault Tolerance)</span>
        </div>
        <div className="consensus-card">
          <span className="consensus-label">Total Blocks:</span>
          <span className="consensus-value">{blocks.length}</span>
        </div>
        <div className="consensus-card">
          <span className="consensus-label">Network Nodes:</span>
          <span className="consensus-value">3 Active</span>
        </div>
      </div>

      <div className="content-card">
        <div className="table-container">
          <table className="blockchain-table">
            <thead>
              <tr>
                <th>Block #</th>
                <th>Threat Hash</th>
                <th>Threat Type</th>
                <th>Timestamp</th>
                <th>Verified</th>
              </tr>
            </thead>
            <tbody>
              {blocks.map((block) => (
                <tr key={block.blockNumber}>
                  <td className="block-number">#{block.blockNumber}</td>
                  <td className="threat-hash">{block.threatHash}</td>
                  <td>{block.threatType}</td>
                  <td>{block.timestamp}</td>
                  <td>
                    <span className="verified-badge">✅ Verified</span>
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

export default BlockchainLedger;
