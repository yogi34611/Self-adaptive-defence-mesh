"""
Background services for automated threat generation, blockchain simulation,
response automation, and node status updates
"""
import threading
import time
import random
import hashlib
from datetime import datetime, timedelta
from database import get_db
import config

class BackgroundServices:
    """Manages all background automation services"""
    
    def __init__(self):
        self.running = False
        self.threads = []
        self.block_counter = 1
        
    def start(self):
        """Start all background services"""
        self.running = True
        
        # Start threat generator
        threat_thread = threading.Thread(target=self._threat_generator_loop, daemon=True)
        threat_thread.start()
        self.threads.append(threat_thread)
        print("🔄 Started: Threat Generator (every 10s)")
        
        # Start node status updater
        node_thread = threading.Thread(target=self._node_updater_loop, daemon=True)
        node_thread.start()
        self.threads.append(node_thread)
        print("🔄 Started: Node Status Updater (every 5s)")
        
        print("✅ All background services started\n")
    
    def stop(self):
        """Stop all background services"""
        self.running = False
        for thread in self.threads:
            thread.join(timeout=2)
        print("🛑 All background services stopped")
    
    # ==================== THREAT GENERATOR ====================
    
    def _threat_generator_loop(self):
        """Background loop to generate threats every 10 seconds"""
        while self.running:
            try:
                self._generate_threat()
                time.sleep(config.THREAT_GENERATION_INTERVAL)
            except Exception as e:
                print(f"❌ Error in threat generator: {e}")
                time.sleep(config.THREAT_GENERATION_INTERVAL)
    
    def _generate_threat(self):
        """Generate a single dummy threat and trigger related actions"""
        db = get_db()
        
        # Generate threat data
        threat_type = random.choice(config.THREAT_TYPES)
        severity = random.choice(config.THREAT_SEVERITIES)
        source_ip = self._generate_random_ip()
        timestamp = datetime.now()
        
        threat = {
            'threatId': f"THR-{random.randint(1000, 9999)}",
            'type': threat_type,
            'severity': severity,
            'source': random.choice(config.THREAT_SOURCES),
            'ip': source_ip,
            'timestamp': timestamp.isoformat(),
            'status': random.choice(config.THREAT_STATUSES),
            'description': f'Suspicious {threat_type.lower()} activity detected from {source_ip}',
            'nodeId': random.choice(config.NODES)['nodeId']
        }
        
        # 1. Insert into threat_history (permanent storage)
        db[config.COLLECTIONS['THREAT_HISTORY']].insert_one(threat.copy())
        
        # 2. Insert into live_threats (keep only last 10)
        db[config.COLLECTIONS['LIVE_THREATS']].insert_one(threat.copy())
        
        # Keep only last 10 live threats
        live_threats_count = db[config.COLLECTIONS['LIVE_THREATS']].count_documents({})
        if live_threats_count > config.LIVE_THREATS_LIMIT:
            # Delete oldest threats
            oldest_threats = db[config.COLLECTIONS['LIVE_THREATS']].find().sort('timestamp', 1).limit(live_threats_count - config.LIVE_THREATS_LIMIT)
            for old_threat in oldest_threats:
                db[config.COLLECTIONS['LIVE_THREATS']].delete_one({'_id': old_threat['_id']})
        
        # 3. Create blockchain block for this threat
        self._create_blockchain_block(threat)
        
        # 4. Generate automated response based on severity
        self._generate_automated_response(threat)
        
        # 5. Update AI status (increment threats analyzed)
        db[config.COLLECTIONS['AI_STATUS']].update_one(
            {},
            {'$inc': {'threatsAnalyzed': 1}, '$set': {'updatedAt': datetime.now().isoformat()}}
        )
        
        # 6. Update node threat counter
        db[config.COLLECTIONS['NODES_STATUS']].update_one(
            {'nodeId': threat['nodeId']},
            {'$inc': {'threatsDetected': 1}}
        )
        
        print(f"🚨 Generated Threat: [{severity}] {threat_type} from {source_ip}")
    
    # ==================== BLOCKCHAIN SIMULATION ====================
    
    def _create_blockchain_block(self, threat):
        """Create a blockchain block for the given threat"""
        db = get_db()
        
        # Generate threat hash
        threat_hash = self._generate_threat_hash(threat['type'], threat['timestamp'])
        
        # Get previous block hash
        last_block = db[config.COLLECTIONS['BLOCKCHAIN_LEDGER']].find_one(
            sort=[('blockNumber', -1)]
        )
        previous_hash = last_block['currentHash'] if last_block else '0' * 16
        
        # Create new block
        block = {
            'blockNumber': self.block_counter,
            'threatHash': threat_hash,
            'currentHash': self._generate_block_hash(str(self.block_counter), threat_hash),
            'previousHash': previous_hash,
            'threatType': threat['type'],
            'threatId': threat['threatId'],
            'timestamp': threat['timestamp'],
            'verificationStatus': '✅ Verified',
            'nodeId': threat['nodeId'],
            'severity': threat['severity']
        }
        
        db[config.COLLECTIONS['BLOCKCHAIN_LEDGER']].insert_one(block)
        print(f"   ⛓️  Block #{self.block_counter} created | Hash: {threat_hash}")
        
        self.block_counter += 1
    
    # ==================== AUTOMATED RESPONSE ====================
    
    def _generate_automated_response(self, threat):
        """Generate automated response based on threat severity"""
        db = get_db()
        
        # Select appropriate actions based on severity
        severity = threat['severity']
        possible_actions = config.RESPONSE_ACTIONS.get(severity, ['Alert Sent'])
        
        # For High and Critical, always take action
        if severity in ['Critical', 'High']:
            action = random.choice(possible_actions)
            self._create_response_log(threat, action)
            print(f"   🛡️  Response: {action} for {threat['ip']}")
        
        # For Medium, 70% chance of action
        elif severity == 'Medium' and random.random() < 0.7:
            action = random.choice(possible_actions)
            self._create_response_log(threat, action)
            print(f"   🛡️  Response: {action} for {threat['ip']}")
    
    def _create_response_log(self, threat, action):
        """Create a response log entry"""
        db = get_db()
        
        response_log = {
            'logId': f"LOG-{random.randint(1000, 9999)}",
            'action': action,
            'targetIp': threat['ip'],
            'threatType': threat['type'],
            'threatId': threat['threatId'],
            'timestamp': datetime.now().isoformat(),
            'status': 'Success' if random.random() > 0.1 else 'Pending',  # 90% success rate
            'nodeId': threat['nodeId'],
            'severity': threat['severity']
        }
        
        db[config.COLLECTIONS['RESPONSE_LOGS']].insert_one(response_log)
    
    # ==================== NODE STATUS UPDATER ====================
    
    def _node_updater_loop(self):
        """Background loop to update node sync times every 5 seconds"""
        while self.running:
            try:
                self._update_node_status()
                time.sleep(config.NODE_SYNC_INTERVAL)
            except Exception as e:
                print(f"❌ Error in node updater: {e}")
                time.sleep(config.NODE_SYNC_INTERVAL)
    
    def _update_node_status(self):
        """Update last sync time for all nodes"""
        db = get_db()
        
        for node in config.NODES:
            db[config.COLLECTIONS['NODES_STATUS']].update_one(
                {'nodeId': node['nodeId']},
                {
                    '$set': {
                        'lastSyncTime': datetime.now().isoformat(),
                        'status': node['status'],  # Always online
                        'latency': f"{random.randint(10, 100)}ms",
                        'uptime': f"{random.randint(98, 100)}.{random.randint(0, 9)}%"
                    }
                }
            )
    
    # ==================== UTILITY FUNCTIONS ====================
    
    def _generate_random_ip(self):
        """Generate a random IP address"""
        return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"
    
    def _generate_threat_hash(self, threat_type, timestamp):
        """Generate a simulated threat hash"""
        data = f"{threat_type}{timestamp}{random.random()}"
        return hashlib.sha256(data.encode()).hexdigest()[:16]
    
    def _generate_block_hash(self, block_number, threat_hash):
        """Generate a simulated block hash"""
        data = f"{block_number}{threat_hash}{random.random()}"
        return hashlib.sha256(data.encode()).hexdigest()[:16]


# Global instance
background_services = BackgroundServices()
