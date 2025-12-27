// Mock data generation utilities
export const generateRandomIP = () => {
  return `${Math.floor(Math.random() * 255)}.${Math.floor(Math.random() * 255)}.${Math.floor(Math.random() * 255)}.${Math.floor(Math.random() * 255)}`;
};

export const threatTypes = ['DDoS', 'Malware', 'Brute Force', 'Phishing'];
export const severities = ['High', 'Medium', 'Low'];
export const statuses = ['Blocked', 'Isolated', 'Monitoring'];

export const generateThreatHash = () => {
  return '0x' + Array.from({ length: 64 }, () => 
    Math.floor(Math.random() * 16).toString(16)
  ).join('');
};

export const generateRandomThreat = () => {
  const now = new Date();
  return {
    id: Math.random().toString(36).substr(2, 9),
    time: now.toLocaleTimeString(),
    threatType: threatTypes[Math.floor(Math.random() * threatTypes.length)],
    ipAddress: generateRandomIP(),
    severity: severities[Math.floor(Math.random() * severities.length)],
    status: statuses[Math.floor(Math.random() * statuses.length)],
    timestamp: now.getTime()
  };
};

export const generateBlockchainBlock = (blockNumber) => {
  const now = new Date();
  return {
    blockNumber,
    threatHash: generateThreatHash(),
    threatType: threatTypes[Math.floor(Math.random() * threatTypes.length)],
    timestamp: now.toLocaleString(),
    verified: true
  };
};

export const generateResponseLog = () => {
  const actions = [
    'IP Address Blocked',
    'Traffic Isolated to Quarantine',
    'Firewall Rule Updated',
    'Alert Sent to Administrator',
    'Connection Terminated',
    'Port Closed',
    'Access Denied'
  ];
  
  const now = new Date();
  return {
    id: Math.random().toString(36).substr(2, 9),
    action: actions[Math.floor(Math.random() * actions.length)],
    triggeredBy: threatTypes[Math.floor(Math.random() * threatTypes.length)],
    time: now.toLocaleString(),
    ipAddress: generateRandomIP()
  };
};

// Initial mock data
export const initialThreats = Array.from({ length: 10 }, generateRandomThreat);

export const initialBlockchainBlocks = Array.from({ length: 15 }, (_, i) => 
  generateBlockchainBlock(i + 1)
);

export const initialResponseLogs = Array.from({ length: 20 }, generateResponseLog);

export const nodes = [
  { id: 1, name: 'Node 1', location: 'Bangalore', status: 'Online' },
  { id: 2, name: 'Node 2', location: 'Mumbai', status: 'Online' },
  { id: 3, name: 'Node 3', location: 'Delhi', status: 'Online' }
];
