# Self-Adaptive Cyber Defense Mesh - Backend API

## ⚠️ STUDENT DEMO PROJECT

This is a **pure educational demonstration** with simulated data only. 
- No real scanning, hacking, or intrusion detection tools
- All data is randomly generated for visualization purposes
- Designed for learning cybersecurity dashboard concepts

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Run the Server

```bash
python app.py
```

The API server will start on `http://localhost:5000`

## 📡 API Endpoints

### Base URL
```
http://localhost:5000
```

### Available Endpoints

#### 1. **GET** `/api/live-threats`
Returns the last 10 dummy threats with real-time simulation.

**Response:**
```json
{
  "success": true,
  "count": 10,
  "threats": [
    {
      "id": 1234,
      "type": "DDoS Attack",
      "severity": "Critical",
      "source": "External",
      "ip": "192.168.1.100",
      "timestamp": "2025-12-03T10:30:00",
      "status": "Blocked",
      "description": "Suspicious activity detected..."
    }
  ]
}
```

#### 2. **GET** `/api/threat-history`
Returns all stored dummy threats (50 historical entries).

**Response:**
```json
{
  "success": true,
  "count": 50,
  "threats": [...]
}
```

#### 3. **GET** `/api/blockchain-ledger`
Returns simulated blockchain blocks with threat verification.

**Response:**
```json
{
  "success": true,
  "totalBlocks": 15,
  "blocks": [
    {
      "blockNumber": 1,
      "threatHash": "a3b5c7d9e1f2g4h6",
      "threatType": "SQL Injection",
      "timestamp": "2025-12-03T10:25:00",
      "verificationStatus": "Verified",
      "previousHash": "0000000000000000",
      "nodeId": "Node-A"
    }
  ]
}
```

#### 4. **GET** `/api/nodes-status`
Returns status of 3 distributed nodes.

**Response:**
```json
{
  "success": true,
  "totalNodes": 3,
  "nodes": [
    {
      "nodeId": "Node-A",
      "location": "US-East",
      "status": "Active",
      "lastSyncTime": "2025-12-03T10:29:30",
      "threatsDetected": 234,
      "uptime": "99.8%",
      "latency": "45ms"
    }
  ]
}
```

#### 5. **GET** `/api/ai-status`
Returns AI model performance metrics.

**Response:**
```json
{
  "success": true,
  "aiStatus": {
    "modelType": "Cognitive Neural Network v2.1",
    "accuracy": 97.85,
    "trainingStatus": "Idle",
    "lastRetrainTime": "2025-12-03T08:00:00",
    "threatsAnalyzed": 25000,
    "falsePositiveRate": 1.2,
    "modelVersion": "2.1.4",
    "activeModels": ["DDoS Detector", "Malware Classifier", "Anomaly Detector"],
    "nextRetrainScheduled": "2025-12-03T18:00:00"
  }
}
```

#### 6. **GET** `/api/response-logs`
Returns automated response actions taken by the system.

**Response:**
```json
{
  "success": true,
  "count": 20,
  "logs": [
    {
      "id": 5678,
      "action": "IP Blocked",
      "targetIp": "10.0.0.50",
      "threatType": "Brute Force",
      "timestamp": "2025-12-03T10:28:00",
      "status": "Success",
      "nodeId": "Node-B",
      "severity": "High"
    }
  ]
}
```

## 🔧 Configuration

- **Host:** 0.0.0.0 (accessible from network)
- **Port:** 5000
- **CORS:** Enabled for all origins (development mode)
- **Debug Mode:** Enabled (disable in production)

## 🛠️ Technology Stack

- **Flask** - Python web framework
- **Flask-CORS** - Cross-Origin Resource Sharing
- **Python 3.8+** - Required Python version

## 📝 Notes for Students

This backend provides:
- ✅ RESTful API architecture
- ✅ JSON response format
- ✅ CORS configuration
- ✅ Error handling
- ✅ Simulated real-time data generation
- ✅ Randomized but realistic dummy data

Perfect for learning:
- API development
- Frontend-backend integration
- Dashboard data visualization
- Cybersecurity concepts (theoretical)

## ⚡ Integration with Frontend

Update your React frontend to fetch from:
```javascript
const API_BASE_URL = 'http://localhost:5000/api';

// Example fetch
fetch(`${API_BASE_URL}/live-threats`)
  .then(res => res.json())
  .then(data => console.log(data));
```

## 🎓 Educational Purpose Only

Remember: This is a demonstration project for learning purposes. Real cybersecurity systems require:
- Proper authentication & authorization
- Secure data handling
- Professional threat intelligence integration
- Compliance with security standards
- Production-grade infrastructure

Enjoy learning! 🚀
