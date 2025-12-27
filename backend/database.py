"""
Database connection and initialization
"""
from pymongo import MongoClient, DESCENDING
from datetime import datetime, timedelta
import config

# MongoDB Client
client = None
db = None

def init_db():
    """Initialize MongoDB connection"""
    global client, db
    
    print("🔌 Connecting to MongoDB...")
    client = MongoClient(config.MONGO_URI)
    db = client[config.DATABASE_NAME]
    
    # Test connection
    try:
        client.admin.command('ping')
        print(f"✅ Connected to MongoDB: {config.DATABASE_NAME}")
    except Exception as e:
        print(f"❌ MongoDB connection failed: {e}")
        raise
    
    # Create collections if they don't exist
    existing_collections = db.list_collection_names()
    
    for collection_name in config.COLLECTIONS.values():
        if collection_name not in existing_collections:
            db.create_collection(collection_name)
            print(f"📦 Created collection: {collection_name}")
    
    # Create indexes for better performance
    db[config.COLLECTIONS['LIVE_THREATS']].create_index([('timestamp', DESCENDING)])
    db[config.COLLECTIONS['THREAT_HISTORY']].create_index([('timestamp', DESCENDING)])
    db[config.COLLECTIONS['BLOCKCHAIN_LEDGER']].create_index([('blockNumber', DESCENDING)])
    db[config.COLLECTIONS['RESPONSE_LOGS']].create_index([('timestamp', DESCENDING)])
    
    # Initialize AI Status and Nodes if they don't exist
    initialize_static_data()
    
    print("✅ Database initialized successfully\n")
    return db

def initialize_static_data():
    """Initialize AI status and node status with default data"""
    
    # Initialize AI Status (single document)
    ai_collection = db[config.COLLECTIONS['AI_STATUS']]
    if ai_collection.count_documents({}) == 0:
        ai_status = {
            'modelType': config.AI_MODEL['modelType'],
            'accuracy': config.AI_MODEL['accuracy'],
            'trainingStatus': config.AI_MODEL['trainingStatus'],
            'lastRetrainTime': (datetime.now() - timedelta(days=config.AI_MODEL['lastRetrainDaysAgo'])).isoformat(),
            'modelVersion': config.AI_MODEL['modelVersion'],
            'activeModels': config.AI_MODEL['activeModels'],
            'threatsAnalyzed': 0,
            'falsePositiveRate': 1.5,
            'nextRetrainScheduled': (datetime.now() + timedelta(hours=12)).isoformat(),
            'updatedAt': datetime.now().isoformat()
        }
        ai_collection.insert_one(ai_status)
        print("🤖 Initialized AI Status")
    
    # Initialize Nodes Status
    nodes_collection = db[config.COLLECTIONS['NODES_STATUS']]
    if nodes_collection.count_documents({}) == 0:
        for node in config.NODES:
            node_status = {
                'nodeId': node['nodeId'],
                'location': node['location'],
                'status': node['status'],
                'lastSyncTime': datetime.now().isoformat(),
                'threatsDetected': 0,
                'uptime': '99.9%',
                'latency': '25ms'
            }
            nodes_collection.insert_one(node_status)
        print("🌐 Initialized Nodes Status")

def get_db():
    """Get database instance"""
    return db

def close_db():
    """Close MongoDB connection"""
    if client:
        client.close()
        print("🔌 MongoDB connection closed")
