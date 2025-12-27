"""
Configuration file for MongoDB connection and app settings
"""

# MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "cyber_defense_db"

# Collections
COLLECTIONS = {
    'LIVE_THREATS': 'live_threats',
    'THREAT_HISTORY': 'threat_history',
    'BLOCKCHAIN_LEDGER': 'blockchain_ledger',
    'RESPONSE_LOGS': 'response_logs',
    'NODES_STATUS': 'nodes_status',
    'AI_STATUS': 'ai_status'
}

# Background Service Settings
THREAT_GENERATION_INTERVAL = 10  # seconds
NODE_SYNC_INTERVAL = 5  # seconds
LIVE_THREATS_LIMIT = 10  # Keep only last 10 in live_threats

# Threat Configuration
THREAT_TYPES = [
    'DDoS Attack',
    'SQL Injection',
    'XSS Attack',
    'Brute Force',
    'Malware Detection',
    'Port Scanning',
    'Phishing Attempt',
    'Zero-Day Exploit',
    'Ransomware',
    'Data Exfiltration'
]

THREAT_SEVERITIES = ['Critical', 'High', 'Medium', 'Low']
THREAT_SOURCES = ['External', 'Internal', 'Unknown']
THREAT_STATUSES = ['Blocked', 'Isolated', 'Monitoring', 'Mitigated']

# Node Configuration
NODES = [
    {'nodeId': 'Node-A', 'location': 'Bangalore', 'status': 'Online'},
    {'nodeId': 'Node-B', 'location': 'Mumbai', 'status': 'Online'},
    {'nodeId': 'Node-C', 'location': 'Delhi', 'status': 'Online'}
]

# AI Model Configuration
AI_MODEL = {
    'modelType': 'Anomaly Detection Neural Network',
    'accuracy': 93.0,
    'trainingStatus': 'Completed',
    'lastRetrainDaysAgo': 2,
    'modelVersion': '2.1.4',
    'activeModels': ['DDoS Detector', 'Malware Classifier', 'Anomaly Detector']
}

# Response Actions Configuration
RESPONSE_ACTIONS = {
    'Critical': ['IP Blocked', 'Firewall Rule Updated', 'Port Closed', 'Session Terminated'],
    'High': ['IP Blocked', 'Firewall Rule Updated', 'Alert Sent'],
    'Medium': ['Traffic Throttled', 'Rate Limit Applied', 'Alert Sent'],
    'Low': ['Alert Sent', 'Monitoring Enabled']
}
