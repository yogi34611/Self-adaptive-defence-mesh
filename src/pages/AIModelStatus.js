import React from 'react';
import './AIModelStatus.css';

const AIModelStatus = () => {
  const models = [
    {
      id: 1,
      name: 'Threat Detection Model',
      type: 'Deep Learning (CNN)',
      accuracy: 93.5,
      trainingStatus: 'Completed',
      lastRetrain: '2025-12-01 14:30:00',
      dataset: '50,000 threat samples'
    },
    {
      id: 2,
      name: 'Anomaly Detection Model',
      type: 'Random Forest',
      accuracy: 89.2,
      trainingStatus: 'Completed',
      lastRetrain: '2025-11-28 10:15:00',
      dataset: '75,000 network logs'
    },
    {
      id: 3,
      name: 'Behavioral Analysis Model',
      type: 'LSTM Neural Network',
      accuracy: 91.8,
      trainingStatus: 'Training',
      lastRetrain: '2025-12-03 08:00:00',
      dataset: '100,000 behavior patterns'
    }
  ];

  const getStatusClass = (status) => {
    return status === 'Completed' ? 'status-completed' : 'status-training';
  };

  return (
    <div className="ai-model-status">
      <h2 className="page-title">AI Model Status</h2>
      
      <div className="overview-cards">
        <div className="overview-card">
          <div className="overview-icon">🤖</div>
          <div className="overview-content">
            <h3>Active Models</h3>
            <p className="overview-value">3</p>
          </div>
        </div>
        <div className="overview-card">
          <div className="overview-icon">📈</div>
          <div className="overview-content">
            <h3>Average Accuracy</h3>
            <p className="overview-value">91.5%</p>
          </div>
        </div>
        <div className="overview-card">
          <div className="overview-icon">🔄</div>
          <div className="overview-content">
            <h3>Models Training</h3>
            <p className="overview-value">1</p>
          </div>
        </div>
      </div>

      <div className="models-container">
        {models.map((model) => (
          <div key={model.id} className="model-card">
            <div className="model-header">
              <h3>{model.name}</h3>
              <span className={`status-badge ${getStatusClass(model.trainingStatus)}`}>
                {model.trainingStatus}
              </span>
            </div>
            
            <div className="model-details">
              <div className="model-row">
                <span className="model-label">Model Type:</span>
                <span className="model-value">{model.type}</span>
              </div>
              <div className="model-row">
                <span className="model-label">Accuracy:</span>
                <span className="model-value accuracy">{model.accuracy}%</span>
              </div>
              <div className="model-row">
                <span className="model-label">Training Dataset:</span>
                <span className="model-value">{model.dataset}</span>
              </div>
              <div className="model-row">
                <span className="model-label">Last Retrain:</span>
                <span className="model-value">{model.lastRetrain}</span>
              </div>
            </div>

            <div className="accuracy-bar">
              <div className="accuracy-label">Accuracy Progress</div>
              <div className="progress-bar">
                <div 
                  className="progress-fill" 
                  style={{width: `${model.accuracy}%`}}
                >
                  <span className="progress-text">{model.accuracy}%</span>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default AIModelStatus;
