# Self-Adaptive Cyber Defense Mesh Dashboard

## 🛡️ Student Demo Project

A React-based dashboard for demonstrating a **Self-Adaptive Cyber Defense Mesh using Cognitive AI and Blockchain** technology.

**⚠️ IMPORTANT: This is a student demonstration project with simulated dummy data only. No real attack tools or actual security systems are implemented.**

## Features

### 🎨 Dark Cybersecurity Theme
- Modern, responsive card-based UI
- Cyan/teal color scheme with gradient backgrounds
- Smooth animations and transitions

### 📊 Dashboard Pages

1. **Dashboard Overview**
   - 4 summary cards (Total/High/Medium/Low threats)
   - Live threats table with auto-refresh (10 seconds)
   - Real-time threat monitoring

2. **Live Threats Monitor**
   - Real-time threat feed
   - Auto-updating every 10 seconds
   - Displays threat type, IP, severity, and status

3. **Threat History**
   - Searchable threat history
   - Severity filter (All/High/Medium/Low)
   - Comprehensive threat log

4. **Blockchain Ledger**
   - Blockchain blocks with threat hashes
   - PBFT consensus mechanism display
   - Block verification status

5. **Nodes Monitor**
   - 3 network nodes (Bangalore, Mumbai, Delhi)
   - Real-time sync status
   - CPU and Memory metrics
   - Auto-updating sync time (5 seconds)

6. **AI Model Status**
   - 3 AI models with accuracy metrics
   - Training status and progress bars
   - Model types: CNN, Random Forest, LSTM

7. **Automated Response Logs**
   - AI-powered response actions
   - Action history with timestamps
   - Triggered threats and source IPs

## 🚀 Getting Started

### Prerequisites
- Node.js (v14 or higher)
- npm or yarn

### Installation

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Start the development server:**
   ```bash
   npm start
   ```

3. **Open your browser:**
   Navigate to `http://localhost:3000`

### Build for Production

```bash
npm run build
```

## 📁 Project Structure

```
src/
├── components/
│   ├── Header.js          # Top header with system status
│   ├── Header.css
│   ├── Sidebar.js         # Left navigation menu
│   └── Sidebar.css
├── pages/
│   ├── Dashboard.js       # Main dashboard
│   ├── LiveThreats.js     # Live threats monitor
│   ├── ThreatHistory.js   # Historical threats with filters
│   ├── BlockchainLedger.js # Blockchain blocks
│   ├── NodesMonitor.js    # Network nodes status
│   ├── AIModelStatus.js   # AI model metrics
│   ├── ResponseLogs.js    # Automated responses
│   └── [corresponding CSS files]
├── utils/
│   └── mockData.js        # Mock data generators
├── App.js                 # Main app with routing
├── App.css
├── index.js
└── index.css
```

## 🔧 Technologies Used

- **React** 18.2.0
- **React Router** 6.20.0
- **CSS3** with gradients and animations
- **JavaScript ES6+**

## 🎯 Key Features

### Auto-Refresh Mechanisms
- Header last scan time: Updates every 5 seconds
- Dashboard threats: Refreshes every 10 seconds
- Live threats page: Updates every 10 seconds
- Nodes sync time: Updates every 5 seconds

### Mock Data
All data is randomly generated for demonstration purposes:
- Random threat types (DDoS, Malware, Brute Force, Phishing)
- Random IP addresses
- Random severity levels (High, Medium, Low)
- Random blockchain hashes
- Simulated node metrics

## 🎓 Educational Purpose

This project is designed for:
- Academic presentations
- Cybersecurity concept demonstrations
- UI/UX portfolio showcase
- Learning React and modern web development

## ⚠️ Disclaimer

This is a **STUDENT DEMO** project only. It contains:
- ✅ Simulated dummy data
- ✅ No real security implementations
- ✅ No actual threat detection
- ✅ No real blockchain integration
- ✅ No real AI models

**Do not use for actual security purposes.**

## 📝 License

This project is for educational purposes only.

## 👨‍💻 Author

Created as a student project for demonstration purposes.

---

**Note:** All threat data, IP addresses, and blockchain hashes are randomly generated and do not represent real threats or systems.
