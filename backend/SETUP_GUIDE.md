# Self-Adaptive Cyber Defense Mesh - MongoDB + Flask Backend

## ⚠️ STUDENT DEMO PROJECT - AUTOMATED SIMULATION

This is a **fully automated educational demonstration** with:
- ✅ Automated dummy threat generation every 10 seconds
- ✅ Blockchain simulation for each threat
- ✅ Automated response system based on threat severity
- ✅ Real-time node status updates
- ✅ MongoDB persistent storage
- ✅ Background services running continuously

**No real cyber attacks or scanning tools - purely simulated for learning!**

---

## 🗄️ Database Architecture

### MongoDB Collections:

1. **live_threats** - Last 10 recent threats (rolling window)
2. **threat_history** - All historical threats (permanent storage)
3. **blockchain_ledger** - Blockchain blocks with threat verification
4. **response_logs** - Automated response actions taken
5. **nodes_status** - Status of 3 distributed nodes
6. **ai_status** - AI model performance metrics

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- MongoDB installed and running locally

### 1. Install MongoDB

**macOS:**
```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
```

**Ubuntu/Linux:**
```bash
sudo apt-get install mongodb
sudo systemctl start mongodb
```

**Windows:**
Download from [MongoDB Official Site](https://www.mongodb.com/try/download/community)

### 2. Verify MongoDB is Running
```bash
mongosh
# Should connect successfully
```

### 3. Install Python Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 4. Run the Backend
```bash
python app.py
```

**Expected Output:**
```
🔌 Connecting to MongoDB...
✅ Connected to MongoDB: cyber_defense_mesh
📦 Created collection: live_threats
📦 Created collection: threat_history
📦 Created collection: blockchain_ledger
📦 Created collection: response_logs
📦 Created collection: nodes_status
📦 Created collection: ai_status
🤖 Initialized AI Status
🌐 Initialized Nodes Status
✅ Database initialized successfully

🔄 Started: Threat Generator (every 10s)
🔄 Started: Node Status Updater (every 5s)
✅ All background services started

============================================================
🛡️  Self-Adaptive Cyber Defense Mesh API Server
============================================================
⚠️  STUDENT DEMO PROJECT - SIMULATED DATA ONLY
📍 Server running on: http://localhost:5000
============================================================
```

---

## 🤖 Automated Background Services

### 1. **Threat Generator** (Every 10 seconds)
Generates realistic dummy threats with:
- Random threat type (DDoS, Malware, Brute Force, etc.)
- Random IP address
- Severity levels (Critical, High, Medium, Low)
- Status (Blocked, Isolated, Monitoring)
- Timestamp

**Example Console Output:**
```
🚨 Generated Threat: [High] DDoS Attack from 192.168.1.100
   ⛓️  Block #15 created | Hash: a3b5c7d9e1f2g4h6
   🛡️  Response: IP Blocked for 192.168.1.100
```

### 2. **Blockchain Simulator** (Triggered by each threat)
For every threat generated:
- Creates a new blockchain block
- Generates unique threat hash (SHA-256 truncated)
- Links to previous block hash
- Marks as ✅ Verified
- Stores in `blockchain_ledger` collection

### 3. **Automated Response System** (Severity-based)
**Critical/High Severity:**
- ✅ IP Blocked
- ✅ Firewall Rule Updated
- ✅ Port Closed
- ✅ Session Terminated

**Medium Severity:**
- ✅ Traffic Throttled
- ✅ Rate Limit Applied
- ✅ Alert Sent

**Low Severity:**
- ✅ Alert Sent
- ✅ Monitoring Enabled

### 4. **Node Status Updater** (Every 5 seconds)
Updates real-time status for:
- **Node-A** - Bangalore - Online
- **Node-B** - Mumbai - Online
- **Node-C** - Delhi - Online

Updates: Last Sync Time, Latency, Uptime percentage

---

## 📡 API Endpoints

### Base URL
```
http://localhost:5000
```

### 1. GET `/api/live-threats`
Returns last 10 real-time threats from MongoDB.

**Response:**
```json
{
  "success": true,
  "count": 10,
  "threats": [
    {
      "threatId": "THR-5432",
      "type": "DDoS Attack",
      "severity": "High",
      "source": "External",
      "ip": "203.45.67.89",
      "timestamp": "2025-12-03T14:25:30",
      "status": "Blocked",
      "description": "Suspicious ddos attack activity detected...",
      "nodeId": "Node-A"
    }
  ]
}
```

### 2. GET `/api/threat-history`
Returns all historical threats (last 100).

### 3. GET `/api/blockchain-ledger`
Returns blockchain blocks with verification.

**Response:**
```json
{
  "success": true,
  "totalBlocks": 50,
  "blocks": [
    {
      "blockNumber": 15,
      "threatHash": "a3b5c7d9e1f2g4h6",
      "currentHash": "9f8e7d6c5b4a3210",
      "previousHash": "1234567890abcdef",
      "threatType": "SQL Injection",
      "threatId": "THR-8765",
      "timestamp": "2025-12-03T14:20:15",
      "verificationStatus": "✅ Verified",
      "nodeId": "Node-B",
      "severity": "High"
    }
  ]
}
```

### 4. GET `/api/nodes-status`
Returns status of 3 distributed nodes.

**Response:**
```json
{
  "success": true,
  "totalNodes": 3,
  "nodes": [
    {
      "nodeId": "Node-A",
      "location": "Bangalore",
      "status": "Online",
      "lastSyncTime": "2025-12-03T14:30:05",
      "threatsDetected": 234,
      "uptime": "99.8%",
      "latency": "25ms"
    }
  ]
}
```

### 5. GET `/api/ai-status`
Returns AI model performance.

**Response:**
```json
{
  "success": true,
  "aiStatus": {
    "modelType": "Anomaly Detection Neural Network",
    "accuracy": 93.0,
    "trainingStatus": "Completed",
    "lastRetrainTime": "2025-12-01T10:00:00",
    "modelVersion": "2.1.4",
    "activeModels": ["DDoS Detector", "Malware Classifier", "Anomaly Detector"],
    "threatsAnalyzed": 1543,
    "falsePositiveRate": 1.5,
    "nextRetrainScheduled": "2025-12-04T02:00:00"
  }
}
```

### 6. GET `/api/response-logs`
Returns automated response actions (last 50).

**Response:**
```json
{
  "success": true,
  "count": 50,
  "logs": [
    {
      "logId": "LOG-6789",
      "action": "IP Blocked",
      "targetIp": "10.0.0.50",
      "threatType": "Brute Force",
      "threatId": "THR-4321",
      "timestamp": "2025-12-03T14:28:00",
      "status": "Success",
      "nodeId": "Node-B",
      "severity": "High"
    }
  ]
}
```

---

## 🔧 Configuration

Edit `config.py` to customize:

```python
# Timing intervals
THREAT_GENERATION_INTERVAL = 10  # seconds
NODE_SYNC_INTERVAL = 5  # seconds

# Data limits
LIVE_THREATS_LIMIT = 10  # Keep only last 10

# MongoDB connection
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "cyber_defense_mesh"
```

---

## 📊 View Database in MongoDB Compass

1. Download [MongoDB Compass](https://www.mongodb.com/products/compass)
2. Connect to: `mongodb://localhost:27017`
3. Select database: `cyber_defense_mesh`
4. Explore collections in real-time!

---

## 🛠️ Technology Stack

- **Flask** - Python web framework
- **Flask-CORS** - Cross-Origin Resource Sharing
- **PyMongo** - MongoDB driver for Python
- **MongoDB** - NoSQL database for persistent storage
- **Threading** - Background automation services

---

## 🎓 Educational Features

### What You'll Learn:
✅ RESTful API design  
✅ MongoDB database integration  
✅ Background task automation  
✅ Blockchain concepts (simplified)  
✅ Real-time data streaming  
✅ Automated response systems  
✅ Threat severity classification  
✅ Multi-node architecture simulation  

### Perfect for Final Year Projects:
- Demonstrates full-stack capabilities
- Shows database design skills
- Automated background processing
- Real-time data generation
- Professional API documentation

---

## 🔍 Troubleshooting

### MongoDB Connection Issues
```bash
# Check if MongoDB is running
mongosh

# Restart MongoDB
brew services restart mongodb-community  # macOS
sudo systemctl restart mongodb  # Linux
```

### Port Already in Use
```bash
# Kill process on port 5000
lsof -ti:5000 | xargs kill -9
```

### Clear Database (Fresh Start)
```bash
mongosh
use cyber_defense_mesh
db.dropDatabase()
# Restart app.py to reinitialize
```

---

## ⚡ Frontend Integration

Update your React frontend:

```javascript
const API_BASE_URL = 'http://localhost:5000/api';

// Fetch live threats
const fetchThreats = async () => {
  const response = await fetch(`${API_BASE_URL}/live-threats`);
  const data = await response.json();
  console.log(data.threats);
};

// Poll every 5 seconds for real-time updates
useEffect(() => {
  const interval = setInterval(fetchThreats, 5000);
  return () => clearInterval(interval);
}, []);
```

---

## 🎯 Demo Presentation Tips

1. **Show MongoDB Compass** - Live database updates
2. **Console Output** - Real-time threat generation logs
3. **API Testing** - Use Postman/Thunder Client
4. **Frontend Dashboard** - React visualization
5. **Explain Automation** - Background services concept

---

## ⚠️ Important Disclaimers

- **No Real Cybersecurity Tools**: This uses zero actual intrusion detection systems
- **Dummy Data Only**: All threats are randomly generated
- **Educational Purpose**: Designed for learning and demonstration
- **Not Production-Ready**: Missing authentication, rate limiting, etc.
- **Local Development**: Not configured for deployment

Real cybersecurity systems require professional-grade tools, compliance standards, and expert implementation.

---

## 📝 Future Enhancements (Ideas)

- Add user authentication (JWT)
- WebSocket for real-time push updates
- Export threat reports to PDF
- Email alerts for critical threats
- Dashboard analytics and charts
- Multi-tenancy support
- Docker containerization

---

## 🎉 Enjoy Your Demo!

Your automated cyber defense mesh is now running! Watch as threats are generated, blockchain blocks are created, and responses are automated - all in real-time.

Perfect for impressing your project evaluators! 🚀

---

**Created for educational purposes | Final Year Project Demo**
