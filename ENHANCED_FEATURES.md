# 🛡️ Self-Adaptive Cyber Defense Mesh v2.0 - Enhanced Edition

## 🎉 NEW FEATURES - Enhanced Version

### ✨ What's New:

1. **🚀 No Database Dependency** - Works instantly without MongoDB setup
2. **👤 User Input for Threats** - Submit custom threats for real-time monitoring
3. **📊 Advanced Analytics** - Comprehensive threat analysis and trends
4. **📄 PDF Report Generation** - Export detailed reports for each section
5. **💾 In-Memory Data Storage** - Fast, lightweight, no DB required
6. **✅ Success Popups** - Visual confirmation when submitting threats
7. **🎯 Enhanced UI** - Modern modals, forms, and animations

---

## 🚀 Quick Start (Enhanced Backend)

### Option 1: Run Enhanced Backend (No MongoDB Required)

```bash
cd backend
python3 app_enhanced.py
```

**Server will start on:** `http://localhost:5001`

###Option 2: Run Original Backend (With MongoDB)

```bash
cd backend
python3 app.py
```

**Requires:** MongoDB installed and running

---

## 📡 API Endpoints

### Standard Endpoints
- `GET /api/live-threats` - Last 10 live threats
- `GET /api/threat-history` - All historical threats
- `GET /api/blockchain-ledger` - Blockchain blocks
- `GET /api/nodes-status` - Node status (Bangalore, Mumbai, Delhi)
- `GET /api/ai-status` - AI model performance
- `GET /api/response-logs` - Automated responses

### 🆕 NEW Endpoints

#### 1. User Threat Submission
```http
POST /api/submit-threat
Content-Type: application/json

{
  "ip": "192.168.1.100",
  "threatType": "DDoS Attack",
  "severity": "High",
  "description": "Suspicious activity detected",
  "protocol": "TCP",
  "port": 80
}
```

**Response:**
```json
{
  "success": true,
  "message": "Threat submitted successfully and is now being monitored",
  "threat": {...},
  "blockNumber": 42,
  "response": "IP Blocked",
  "monitoring": {
    "status": "Active",
    "startTime": "2025-12-03T10:30:00",
    "alerts": true
  }
}
```

#### 2. Analytics Overview
```http
GET /api/analytics/overview
```

**Returns:**
- Total threats count
- User-submitted threats
- Blocked threats
- Severity distribution
- Threat type distribution
- Hourly trends (last 24h)
- Node performance metrics
- Response effectiveness rate
- Average response time

#### 3. Threat Trends
```http
GET /api/analytics/threats-trend
```

**Returns:** 7-day threat trends with severity breakdown

#### 4. PDF Report Generation
```http
POST /api/reports/generate/{section}
```

**Sections:**
- `live-threats` - Current live threats report
- `threat-history` - Historical threats report
- `blockchain` - Blockchain ledger report
- `nodes` - Node status report
- `response-logs` - Response actions report
- `analytics` - Comprehensive analytics report

**Returns:** PDF file download

---

## 🎯 Frontend Features

### 1. Live Threats Page

**New Features:**
- ✅ **Submit Threat Button** - Open form modal to submit custom threats
- ✅ **Export PDF Button** - Generate and download PDF reports
- ✅ **Success Popup** - Visual confirmation with animation
- ✅ **User Badge** - 👤 icon shows user-submitted threats
- ✅ **Enhanced Table** - More data columns (Protocol, Port, Confidence)

**How to Submit a Threat:**
1. Click "**+ Submit Threat**" button
2. Fill in the form:
   - IP Address (required)
   - Threat Type (required)
   - Severity (required)
   - Protocol, Port, Description (optional)
3. Click "**Submit & Monitor**"
4. ✅ Success popup appears
5. Threat is added to live monitoring
6. Blockchain block created automatically
7. Automated response initiated based on severity

### 2. PDF Export Feature

**Available on All Pages:**
- Click "**📄 Export PDF**" button
- PDF generated with current data
- Auto-downloads with timestamp

**PDF Includes:**
- Section title and timestamp
- Formatted data tables
- Professional styling
- Ready for presentation

### 3. Enhanced Styling

**New Visual Elements:**
- 🎨 Modern modal overlays
- ✨ Smooth animations (fade-in, slide-up, bounce)
- 🌊 Gradient buttons with hover effects
- 💫 Success popup with checkmark animation
- 🎯 User-submitted rows highlighted
- 📱 Fully responsive design

---

## 🔧 Technical Details

### Backend Architecture (Enhanced)

**Data Storage:**
```python
threat_history = []          # All threats (permanent)
live_threats = []            # Last 10 threats (rolling)
blockchain_ledger = []       # All blocks
response_logs = []           # All responses
user_submitted_threats = []  # User inputs
```

**Realistic Data Generation:**
- Random but realistic threat types
- Valid IP addresses
- Proper timestamps
- Protocol and port information
- Attack vectors and confidence scores
- Node assignment (Bangalore/Mumbai/Delhi)

**Blockchain Simulation:**
- SHA-256 hashed threat IDs
- Block chaining with previous hash
- Verification status
- Transaction tracking

**Automated Response System:**
```python
Severity Rules:
- Critical/High → Always respond
- Medium → 70% response chance
- Low → Monitoring only

Response Actions:
- Critical: IP Blocked, Firewall Rule Updated, Port Closed
- High: IP Blocked, Alert Sent
- Medium: Traffic Throttled, Rate Limit Applied
- Low: Alert Sent, Monitoring Enabled
```

### Frontend Architecture

**State Management:**
```javascript
- threats (array) - From API
- loading (boolean) - Loading state
- showForm (boolean) - Modal visibility
- showSuccess (boolean) - Success popup
- formData (object) - Form inputs
```

**Auto-Refresh:**
```javascript
useEffect(() => {
  fetchThreats();
  const interval = setInterval(fetchThreats, 5000); // Every 5 seconds
  return () => clearInterval(interval);
}, []);
```

**API Integration:**
```javascript
const API_BASE = 'http://localhost:5001/api';

// Fetch
fetch(`${API_BASE}/live-threats`)

// Submit
fetch(`${API_BASE}/submit-threat`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(formData)
})

// Download PDF
fetch(`${API_BASE}/reports/generate/live-threats`, { method: 'POST' })
  .then(res => res.blob())
  .then(blob => downloadFile(blob))
```

---

## 📊 Sample Data

### Initial Data Set:
- **30 historical threats** - Pre-generated with random timestamps
- **10 live threats** - Most recent
- **30 blockchain blocks** - One per threat
- **20+ response logs** - Automated actions
- **3 nodes** - Bangalore, Mumbai, Delhi (always online)
- **AI model** - 93.5% accuracy, actively training

### User Submissions:
- Instantly added to all collections
- Marked with `userSubmitted: true` flag
- Shows 👤 badge in UI
- Creates blockchain block
- Triggers automated response
- Updates analytics immediately

---

## 🎓 Perfect for Demonstrations

### Why This Project Rocks:

1. **✅ No Complex Setup** - Works immediately without database
2. **✅ Real-Time Features** - Auto-refresh, live monitoring
3. **✅ Interactive** - User can submit threats and see results
4. **✅ Professional UI** - Modern, animated, responsive
5. **✅ PDF Reports** - Exportable documentation
6. **✅ Analytics** - Charts, trends, statistics
7. **✅ Blockchain** - Demonstrates understanding of distributed ledger
8. **✅ AI Integration** - Shows ML model tracking
9. **✅ Automated Responses** - Rule-based security actions
10. **✅ Educational** - Clearly marked as demo/simulation

### Demo Flow:

1. **Start Backend** - `python3 app_enhanced.py`
2. **Start Frontend** - `npm start`
3. **Show Dashboard** - Live metrics updating
4. **Submit Threat** - Use the form, show popup
5. **Check Blockchain** - New block created
6. **View Response** - Automated action logged
7. **Export Report** - Generate PDF
8. **Show Analytics** - Trends and statistics

---

## ⚙️ Configuration

Edit `app_enhanced.py` to customize:

```python
# Threat types
THREAT_TYPES = ['DDoS Attack', 'SQL Injection', ...]

# Severities
THREAT_SEVERITIES = ['Critical', 'High', 'Medium', 'Low']

# Node locations
nodes_status = [
  {'nodeId': 'Node-A', 'location': 'Bangalore'},
  {'nodeId': 'Node-B', 'location': 'Mumbai'},
  {'nodeId': 'Node-C', 'location': 'Delhi'}
]

# AI model accuracy
ai_status = {'accuracy': 93.5, ...}
```

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
lsof -ti:5001 | xargs kill -9
```

### PDF Generation Fails
```bash
pip3 install reportlab
```

### CORS Issues
- Check backend is running on port 5001
- Check frontend API_BASE URL matches backend port
- CORS is enabled by default in Flask

### Form Validation
- IP Address must match pattern: `xxx.xxx.xxx.xxx`
- Port must be between 1-65535
- All required fields must be filled

---

## 📈 Future Enhancements (Ideas)

- 🔐 Add user authentication
- 📱 Mobile app integration
- 🔔 Email/SMS alerts
- 📊 More visualization charts
- 🌐 WebSocket for real-time push
- 🤖 ML model predictions
- 🔒 Encryption for blockchain
- 📸 Screenshots in PDF reports
- 🎨 Theme customization
- 🌍 Multi-language support

---

## ⚠️ Important Disclaimers

- **Educational Purpose Only** - This is a demonstration project
- **No Real Security Tools** - All threats are simulated
- **Not Production-Ready** - Missing authentication, rate limiting, etc.
- **Dummy Data** - All information is randomly generated
- **Demo Quality** - Designed for learning and presentation

Real cybersecurity systems require professional-grade tools, compliance standards, and expert implementation.

---

## 📝 Dependencies

```bash
# Backend
Flask==3.0.0
flask-cors==4.0.0
reportlab==4.0.7

# Frontend
React
React Router DOM
CSS3 (with animations)
```

---

## 🎉 Success Criteria

### Your Project Demonstrates:

✅ Full-stack development (React + Flask)  
✅ RESTful API design  
✅ User input handling and validation  
✅ Real-time data updates  
✅ PDF report generation  
✅ Blockchain concepts  
✅ Automated response systems  
✅ Analytics and data visualization  
✅ Modern UI/UX design  
✅ Professional documentation  

---

## 🚀 Run Everything

```bash
# Terminal 1 - Backend
cd backend
python3 app_enhanced.py

# Terminal 2 - Frontend
cd ..
npm start

# Open browser
http://localhost:3000
```

---

**Created for Final Year Project Demonstration**  
**Self-Adaptive Cyber Defense Mesh v2.0 - Enhanced Edition**  
**🛡️ Protecting the Future with AI & Blockchain 🛡️**

---

Enjoy your enhanced cybersecurity dashboard! 🎊
