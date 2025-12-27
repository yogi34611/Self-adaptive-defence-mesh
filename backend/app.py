from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
import atexit
from database import init_db, get_db, close_db
from services import background_services
import config

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# Initialize MongoDB
db = init_db()

# Start background services
background_services.start()

# Cleanup on shutdown
@atexit.register
def cleanup():
    background_services.stop()
    close_db()


# ==================== API ROUTES ====================

@app.route('/')
def home():
    """Root endpoint"""
    return jsonify({
        'message': 'Self-Adaptive Cyber Defense Mesh API',
        'version': '1.0.0',
        'status': 'active',
        'note': 'This is a student demo project with simulated data only'
    })

@app.route('/api/live-threats')
def get_live_threats():
    """
    GET /api/live-threats
    Returns the last 10 dummy threats from MongoDB
    """
    db = get_db()
    live_threats = list(db[config.COLLECTIONS['LIVE_THREATS']].find(
        {},
        {'_id': 0}  # Exclude MongoDB _id field
    ).sort('timestamp', -1).limit(10))
    
    return jsonify({
        'success': True,
        'count': len(live_threats),
        'threats': live_threats
    })

@app.route('/api/threat-history')
def get_threat_history():
    """
    GET /api/threat-history
    Returns all stored dummy threats from MongoDB
    """
    db = get_db()
    threat_history = list(db[config.COLLECTIONS['THREAT_HISTORY']].find(
        {},
        {'_id': 0}
    ).sort('timestamp', -1).limit(100))  # Limit to last 100 for performance
    
    return jsonify({
        'success': True,
        'count': len(threat_history),
        'threats': threat_history
    })

@app.route('/api/blockchain-ledger')
def get_blockchain_ledger():
    """
    GET /api/blockchain-ledger
    Returns simulated blockchain blocks from MongoDB
    """
    db = get_db()
    blocks = list(db[config.COLLECTIONS['BLOCKCHAIN_LEDGER']].find(
        {},
        {'_id': 0}
    ).sort('blockNumber', -1).limit(50))  # Last 50 blocks
    
    return jsonify({
        'success': True,
        'totalBlocks': len(blocks),
        'blocks': blocks
    })

@app.route('/api/nodes-status')
def get_nodes_status():
    """
    GET /api/nodes-status
    Returns 3 nodes with status information from MongoDB
    """
    db = get_db()
    nodes = list(db[config.COLLECTIONS['NODES_STATUS']].find(
        {},
        {'_id': 0}
    ))
    
    return jsonify({
        'success': True,
        'totalNodes': len(nodes),
        'nodes': nodes
    })

@app.route('/api/ai-status')
def get_ai_status():
    """
    GET /api/ai-status
    Returns AI model status information from MongoDB
    """
    db = get_db()
    ai_status = db[config.COLLECTIONS['AI_STATUS']].find_one(
        {},
        {'_id': 0}
    )
    
    return jsonify({
        'success': True,
        'aiStatus': ai_status
    })

@app.route('/api/response-logs')
def get_response_logs():
    """
    GET /api/response-logs
    Returns automated response actions from MongoDB
    """
    db = get_db()
    logs = list(db[config.COLLECTIONS['RESPONSE_LOGS']].find(
        {},
        {'_id': 0}
    ).sort('timestamp', -1).limit(50))  # Last 50 response logs
    
    return jsonify({
        'success': True,
        'count': len(logs),
        'logs': logs
    })


# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500


# ==================== RUN APP ====================

if __name__ == '__main__':
    print("=" * 60)
    print("🛡️  Self-Adaptive Cyber Defense Mesh API Server")
    print("=" * 60)
    print("⚠️  STUDENT DEMO PROJECT - SIMULATED DATA ONLY")
    print("📍 Server running on: http://localhost:5001")
    print("=" * 60)
    print("\nAvailable Endpoints:")
    print("  GET /api/live-threats       - Last 10 dummy threats")
    print("  GET /api/threat-history     - All stored threats")
    print("  GET /api/blockchain-ledger  - Simulated blockchain blocks")
    print("  GET /api/nodes-status       - Node status information")
    print("  GET /api/ai-status          - AI model status")
    print("  GET /api/response-logs      - Automated response actions")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5001)
