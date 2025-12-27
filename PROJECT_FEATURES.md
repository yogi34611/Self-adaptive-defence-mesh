# Project Features Documentation

## Self-Adaptive Cyber Defense Mesh Dashboard
### Cognitive AI + Blockchain Security Platform (Student Demo)

---

## 🎯 Project Overview

This is a comprehensive React-based dashboard demonstrating a **Self-Adaptive Cyber Defense Mesh** that combines:
- **Cognitive AI** for threat detection
- **Blockchain** for immutable threat logging
- **Multi-node architecture** for distributed defense

---

## 📁 Complete File Structure

```
Self adaptive defence mesh/
├── package.json
├── package-lock.json
├── .gitignore
├── README.md
├── QUICKSTART.md
├── PROJECT_FEATURES.md (this file)
│
├── public/
│   └── index.html
│
└── src/
    ├── index.js
    ├── index.css
    ├── App.js
    ├── App.css
    │
    ├── components/
    │   ├── Header.js
    │   ├── Header.css
    │   ├── Sidebar.js
    │   └── Sidebar.css
    │
    ├── pages/
    │   ├── Dashboard.js
    │   ├── Dashboard.css
    │   ├── LiveThreats.js
    │   ├── LiveThreats.css
    │   ├── ThreatHistory.js
    │   ├── ThreatHistory.css
    │   ├── BlockchainLedger.js
    │   ├── BlockchainLedger.css
    │   ├── NodesMonitor.js
    │   ├── NodesMonitor.css
    │   ├── AIModelStatus.js
    │   ├── AIModelStatus.css
    │   ├── ResponseLogs.js
    │   └── ResponseLogs.css
    │
    └── utils/
        └── mockData.js
```

---

## 🌟 Feature Breakdown

### 1. Header Component
**File:** `src/components/Header.js`

**Features:**
- Project title with shield emoji 🛡️
- Subtitle: "Cognitive AI + Blockchain Security [STUDENT DEMO]"
- 5 Status indicators:
  1. System Status: ● ONLINE (green)
  2. AI Model Status: ● RUNNING (blue)
  3. Blockchain Status: ● CONNECTED (orange)
  4. Active Nodes: 3
  5. Last Scan Time (updates every 5 seconds)

**Styling:**
- Gradient background (dark blue to darker blue)
- Cyan border glow effect
- Responsive flexbox layout
- Color-coded status indicators

---

### 2. Sidebar Navigation
**File:** `src/components/Sidebar.js`

**Features:**
- 7 navigation menu items with icons:
  - 📊 Dashboard
  - ⚠️ Live Threats
  - 📋 Threat History
  - ⛓️ Blockchain Ledger
  - 🖥️ Nodes Monitor
  - 🤖 AI Model Status
  - 📝 Automated Response Logs

**Styling:**
- Active page highlighting with cyan border
- Hover effects with background glow
- Smooth transitions
- Custom scrollbar styling

---

### 3. Dashboard Page (Main)
**File:** `src/pages/Dashboard.js`

**Features:**

#### Summary Cards (4 cards):
1. **Total Threats Today**
   - Icon: 📊
   - Dynamic count from today's threats
   - Cyan border

2. **High Severity**
   - Icon: 🔴
   - Count of high severity threats
   - Red border

3. **Medium Severity**
   - Icon: 🟡
   - Count of medium severity threats
   - Orange border

4. **Low Severity**
   - Icon: 🟢
   - Count of low severity threats
   - Green border

#### Live Threats Table:
- Columns: Time, Threat Type, IP Address, Severity, Status
- Auto-refreshes every 10 seconds
- Displays last 15 threats
- Color-coded badges for severity and status
- Hover effects on rows

**Threat Types:**
- DDoS
- Malware
- Brute Force
- Phishing

**Severity Levels:**
- High (Red badge)
- Medium (Orange badge)
- Low (Green badge)

**Status Types:**
- Blocked (Red badge)
- Isolated (Orange badge)
- Monitoring (Blue badge)

---

### 4. Live Threats Page
**File:** `src/pages/LiveThreats.js`

**Features:**
- "● LIVE UPDATES" badge with pulsing animation
- Real-time threat feed (30 most recent)
- Auto-refresh every 10 seconds
- Same table structure as Dashboard
- Full-width layout for better visibility

---

### 5. Threat History Page
**File:** `src/pages/ThreatHistory.js`

**Features:**

#### Search Functionality:
- Search input field
- Searches by IP Address or Threat Type
- Real-time filtering

#### Severity Filter:
- Dropdown with options:
  - All Severities
  - High
  - Medium
  - Low
- Instant filter application

#### Results Display:
- Shows "X of Y threats" counter
- Historical data (50 threats)
- Sortable table
- Responsive layout

---

### 6. Blockchain Ledger Page
**File:** `src/pages/BlockchainLedger.js`

**Features:**

#### Consensus Information Cards (3 cards):
1. **Consensus Mechanism**
   - Display: "PBFT (Practical Byzantine Fault Tolerance)"
   - Orange border

2. **Total Blocks**
   - Dynamic count of blockchain blocks
   - Orange accent

3. **Network Nodes**
   - Display: "3 Active"
   - Orange highlight

#### Blockchain Table:
- Columns:
  1. Block # (numbered, cyan color)
  2. Threat Hash (64-character hex string)
  3. Threat Type
  4. Timestamp
  5. Verified (✅ badge in green)

**Features:**
- 20 initial blocks
- Each block has unique hash
- All blocks show "✅ Verified"
- Monospace font for hashes
- Hover effects

---

### 7. Nodes Monitor Page
**File:** `src/pages/NodesMonitor.js`

**Features:**

#### Sync Information:
- "Last Sync Time" display
- Updates every 5 seconds
- Blue accent card

#### Node Cards (3 nodes):

**Node 1 - Bangalore**
- Status: ● Online (green)
- Node ID: NODE-001
- Location: Bangalore
- Connection: Secure (TLS 1.3)
- Uptime: 99.9%
- CPU metric with progress bar
- Memory metric with progress bar

**Node 2 - Mumbai**
- Status: ● Online (green)
- Node ID: NODE-002
- Location: Mumbai
- Same metrics as Node 1

**Node 3 - Delhi**
- Status: ● Online (green)
- Node ID: NODE-003
- Location: Delhi
- Same metrics as Node 1

**Visual Features:**
- Gradient progress bars (cyan to green)
- Random CPU/Memory percentages (45-65%, 60-75%)
- Hover lift effect on cards
- Responsive grid layout

---

### 8. AI Model Status Page
**File:** `src/pages/AIModelStatus.js`

**Features:**

#### Overview Cards (3 cards):
1. **Active Models**: 3
2. **Average Accuracy**: 91.5%
3. **Models Training**: 1

#### AI Model Details (3 models):

**Model 1: Threat Detection Model**
- Type: Deep Learning (CNN)
- Accuracy: 93.5%
- Status: ✅ Completed (green badge)
- Training Dataset: 50,000 threat samples
- Last Retrain: 2025-12-01 14:30:00
- Visual progress bar showing 93.5%

**Model 2: Anomaly Detection Model**
- Type: Random Forest
- Accuracy: 89.2%
- Status: ✅ Completed (green badge)
- Training Dataset: 75,000 network logs
- Last Retrain: 2025-11-28 10:15:00
- Visual progress bar showing 89.2%

**Model 3: Behavioral Analysis Model**
- Type: LSTM Neural Network
- Accuracy: 91.8%
- Status: ⚠️ Training (orange badge, pulsing)
- Training Dataset: 100,000 behavior patterns
- Last Retrain: 2025-12-03 08:00:00
- Visual progress bar showing 91.8%

**Visual Features:**
- Gradient progress bars (blue to green)
- Percentage display within progress bars
- Detailed model information
- Hover effects on cards

---

### 9. Automated Response Logs Page
**File:** `src/pages/ResponseLogs.js`

**Features:**

#### Header Info:
- Total Logs counter
- "🤖 AI-Powered Responses" badge (blue)

#### Response Actions Table:
- Columns:
  1. Time (full timestamp)
  2. Action Taken
  3. Triggered By (threat type badge)
  4. Source IP

**Sample Actions:**
- IP Address Blocked
- Traffic Isolated to Quarantine
- Firewall Rule Updated
- Alert Sent to Administrator
- Connection Terminated
- Port Closed
- Access Denied

**Features:**
- 30 historical log entries
- Green-highlighted action text
- Red badges for threat types
- Monospace font for IPs
- Full timestamp display

---

## 🎨 Design System

### Color Palette:
```css
Primary Background: #0a0e27 (dark navy)
Secondary Background: #1a1f3a (lighter navy)
Card Background: #0f1229 (medium navy)

Primary Accent: #00ffff (cyan)
Success: #00ff88 (green)
Warning: #ffaa00 (orange)
Danger: #ff4444 (red)
Info: #00ccff (light blue)

Text Primary: #ffffff (white)
Text Secondary: #aaaaaa (gray)
```

### Typography:
- Font: System fonts (San Francisco, Segoe UI, Roboto)
- Headings: Bold, cyan color with glow effect
- Body: Regular, white/gray text
- Monospace: 'Courier New' for IPs and hashes

### Card Design:
- Gradient backgrounds
- 2px colored borders
- 10px border radius
- Box shadows with color glow
- Hover effects (lift + enhanced shadow)

### Badges:
- Rounded corners (5px)
- Colored borders matching background
- 20% opacity backgrounds
- Bold text

### Tables:
- Full width
- Collapsed borders
- Header with colored background (10% opacity)
- 2px colored bottom border on headers
- Row hover effects (5% opacity background)
- 1px separator lines between rows

---

## 🔄 Auto-Refresh Mechanisms

### Implementation Details:

1. **Header Last Scan Time**
   ```javascript
   useEffect(() => {
     const interval = setInterval(() => {
       setLastScanTime(new Date().toLocaleTimeString());
     }, 5000); // 5 seconds
     return () => clearInterval(interval);
   }, []);
   ```

2. **Dashboard Threats**
   ```javascript
   const interval = setInterval(() => {
     const newThreat = generateRandomThreat();
     setThreats(prev => [newThreat, ...prev].slice(0, 15));
   }, 10000); // 10 seconds
   ```

3. **Nodes Sync Time**
   ```javascript
   const interval = setInterval(() => {
     setLastSyncTime(new Date().toLocaleString());
   }, 5000); // 5 seconds
   ```

---

## 📊 Mock Data Generation

### Location: `src/utils/mockData.js`

**Functions:**

1. `generateRandomIP()` - Creates random IP addresses
2. `generateThreatHash()` - Creates 64-char hex strings
3. `generateRandomThreat()` - Creates threat objects
4. `generateBlockchainBlock()` - Creates blockchain blocks
5. `generateResponseLog()` - Creates response log entries

**Constants:**
- `threatTypes`: ['DDoS', 'Malware', 'Brute Force', 'Phishing']
- `severities`: ['High', 'Medium', 'Low']
- `statuses`: ['Blocked', 'Isolated', 'Monitoring']
- `nodes`: Array of 3 node objects (Bangalore, Mumbai, Delhi)

---

## 🚀 Technologies & Libraries

### Core:
- **React** 18.2.0 - UI framework
- **React Router** 6.20.0 - Navigation
- **React Scripts** 5.0.1 - Build tools

### Development:
- **Webpack** - Module bundler (via react-scripts)
- **Babel** - JavaScript compiler (via react-scripts)
- **ESLint** - Code linting (via react-scripts)

### Styling:
- **CSS3** - Custom styles
- **CSS Grid** - Layout system
- **Flexbox** - Component alignment
- **CSS Animations** - Pulsing effects, transitions

---

## 📱 Responsive Breakpoints

```css
Desktop (default): 1024px+
Tablet: 768px - 1023px
Mobile: 320px - 767px
```

### Responsive Features:
- Flexible grid layouts
- Collapsible sidebar on mobile
- Stacked cards on small screens
- Adjusted font sizes
- Touch-friendly button sizes
- Horizontal scrolling tables

---

## ⚡ Performance Optimizations

1. **Component-level state management** - No global state overhead
2. **Cleanup functions** - All intervals cleared on unmount
3. **Slice operations** - Limited array sizes (15-30 items)
4. **CSS transforms** - Hardware-accelerated animations
5. **Lazy data generation** - On-demand mock data creation

---

## 🔐 Security Notes (For Student Demo)

**This project includes:**
- ✅ Simulated threat data only
- ✅ No actual network scanning
- ✅ No real blockchain integration
- ✅ No AI model execution
- ✅ No backend server
- ✅ No data persistence
- ✅ No external API calls

**Clear disclaimers in:**
- README.md
- QUICKSTART.md
- Header subtitle: "[STUDENT DEMO]"

---

## 📝 Usage Instructions

### For Development:
```bash
npm install        # Install dependencies
npm start          # Start dev server (port 3000)
npm run build      # Build for production
npm test           # Run tests
```

### For Presentation:
1. Start server: `npm start`
2. Navigate through all 7 pages
3. Demonstrate search/filter features
4. Show auto-refresh capabilities
5. Highlight responsive design
6. Explain mock data generation

---

## 🎓 Learning Outcomes

This project demonstrates:
1. **React Fundamentals** - Components, hooks, state management
2. **React Router** - Multi-page navigation
3. **CSS Skills** - Modern layouts, animations, responsive design
4. **JavaScript** - Array operations, timers, data manipulation
5. **UI/UX Design** - Dashboard layouts, data visualization
6. **Project Structure** - Component organization, file management

---

## 📊 Project Statistics

- **Total Files**: 25+
- **Components**: 2 (Header, Sidebar)
- **Pages**: 7 (Dashboard, Live Threats, History, Blockchain, Nodes, AI, Logs)
- **Lines of Code**: ~2,500+
- **Mock Data Functions**: 5
- **Auto-refresh Timers**: 4
- **Color Schemes**: 8
- **Responsive Breakpoints**: 3

---

## 🏆 Project Highlights

✅ Fully functional React application
✅ 7 unique pages with distinct features
✅ Real-time data simulation
✅ Professional cybersecurity theme
✅ Responsive design for all devices
✅ Clean, organized code structure
✅ Comprehensive documentation
✅ No external dependencies (except React ecosystem)
✅ Ready for demonstration/presentation

---

**End of Documentation**

For quick start instructions, see `QUICKSTART.md`
For general information, see `README.md`
