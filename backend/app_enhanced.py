from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from datetime import datetime, timedelta
import random
import hashlib
import io
from collections import Counter

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# ==================== IN-MEMORY DATA STORES (No DB) ====================

threat_history = []
live_threats = []
blockchain_ledger = []
response_logs = []
user_submitted_threats = []

# Static data
nodes_status = [
    {'nodeId': 'Node-A', 'location': 'Bangalore', 'status': 'Online', 'threatsDetected': 0, 'uptime': '99.9%', 'latency': '25ms'},
    {'nodeId': 'Node-B', 'location': 'Mumbai', 'status': 'Online', 'threatsDetected': 0, 'uptime': '99.8%', 'latency': '30ms'},
    {'nodeId': 'Node-C', 'location': 'Delhi', 'status': 'Online', 'threatsDetected': 0, 'uptime': '99.7%', 'latency': '28ms'}
]

ai_status = {
    'modelType': 'Anomaly Detection Neural Network',
    'accuracy': 93.5,
    'trainingStatus': 'Active',
    'lastRetrainTime': (datetime.now() - timedelta(days=2)).isoformat(),
    'modelVersion': '2.1.4',
    'activeModels': ['DDoS Detector', 'Malware Classifier', 'Anomaly Detector'],
    'threatsAnalyzed': 0,
    'falsePositiveRate': 1.5,
    'nextRetrainScheduled': (datetime.now() + timedelta(hours=12)).isoformat()
}

# Configuration
THREAT_TYPES = ['DDoS Attack', 'SQL Injection', 'XSS Attack', 'Brute Force', 'Malware Detection', 
                'Port Scanning', 'Phishing Attempt', 'Zero-Day Exploit', 'Ransomware', 'Data Exfiltration']
THREAT_SEVERITIES = ['Critical', 'High', 'Medium', 'Low']
THREAT_SOURCES = ['External', 'Internal', 'Unknown']
THREAT_STATUSES = ['Blocked', 'Isolated', 'Monitoring', 'Mitigated']

block_counter = 1

# ==================== HELPER FUNCTIONS ====================

def generate_random_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

def generate_threat_hash(threat_type, timestamp):
    data = f"{threat_type}{timestamp}{random.random()}"
    return hashlib.sha256(data.encode()).hexdigest()[:16]

def generate_realistic_threat():
    """Generate realistic threat with proper metadata"""
    threat_type = random.choice(THREAT_TYPES)
    severity = random.choice(THREAT_SEVERITIES)
    source_ip = generate_random_ip()
    timestamp = datetime.now()
    node = random.choice(nodes_status)
    
    threat = {
        'threatId': f"THR-{random.randint(1000, 9999)}",
        'type': threat_type,
        'severity': severity,
        'source': random.choice(THREAT_SOURCES),
        'ip': source_ip,
        'timestamp': timestamp.isoformat(),
        'status': random.choice(THREAT_STATUSES),
        'description': f'Suspicious {threat_type.lower()} activity detected from {source_ip}',
        'nodeId': node['nodeId'],
        'location': node['location'],
        'protocol': random.choice(['TCP', 'UDP', 'HTTP', 'HTTPS']),
        'port': random.choice([80, 443, 22, 3389, 8080, 3306]),
        'attackVector': random.choice(['Network', 'Application', 'System', 'Database']),
        'confidence': round(random.uniform(75, 99), 2)
    }
    
    return threat

def create_blockchain_block(threat):
    """Create blockchain block for threat"""
    global block_counter
    
    threat_hash = generate_threat_hash(threat['type'], threat['timestamp'])
    previous_hash = blockchain_ledger[-1]['currentHash'] if blockchain_ledger else '0' * 16
    
    block = {
        'blockNumber': block_counter,
        'threatHash': threat_hash,
        'currentHash': generate_threat_hash(str(block_counter), threat_hash),
        'previousHash': previous_hash,
        'threatType': threat['type'],
        'threatId': threat['threatId'],
        'timestamp': threat['timestamp'],
        'verificationStatus': '✅ Verified',
        'nodeId': threat['nodeId'],
        'severity': threat['severity'],
        'minedBy': threat['nodeId'],
        'transactionCount': 1
    }
    
    blockchain_ledger.append(block)
    block_counter += 1
    return block

def generate_automated_response(threat):
    """Generate automated response based on severity"""
    actions = {
        'Critical': ['IP Blocked', 'Firewall Rule Updated', 'Port Closed', 'Session Terminated'],
        'High': ['IP Blocked', 'Firewall Rule Updated', 'Alert Sent'],
        'Medium': ['Traffic Throttled', 'Rate Limit Applied', 'Alert Sent'],
        'Low': ['Alert Sent', 'Monitoring Enabled']
    }
    
    if threat['severity'] in ['Critical', 'High'] or (threat['severity'] == 'Medium' and random.random() < 0.7):
        action = random.choice(actions.get(threat['severity'], ['Alert Sent']))
        
        response_log = {
            'logId': f"LOG-{random.randint(1000, 9999)}",
            'action': action,
            'targetIp': threat['ip'],
            'threatType': threat['type'],
            'threatId': threat['threatId'],
            'timestamp': datetime.now().isoformat(),
            'status': 'Success' if random.random() > 0.1 else 'Pending',
            'nodeId': threat['nodeId'],
            'severity': threat['severity'],
            'responseTime': f"{random.randint(10, 500)}ms",
            'automated': True
        }
        
        response_logs.append(response_log)
        return response_log
    return None

def initialize_sample_data():
    """Initialize with realistic sample data (not DB dependent)"""
    global ai_status
    
    # Generate initial threat history
    for i in range(30):
        threat = generate_realistic_threat()
        threat['timestamp'] = (datetime.now() - timedelta(minutes=random.randint(10, 1440))).isoformat()
        threat_history.append(threat)
        
        # Create blockchain block
        create_blockchain_block(threat)
        
        # Generate response
        generate_automated_response(threat)
        
        # Update node threats
        for node in nodes_status:
            if node['nodeId'] == threat['nodeId']:
                node['threatsDetected'] += 1
    
    # Generate live threats
    for i in range(10):
        threat = generate_realistic_threat()
        threat['timestamp'] = (datetime.now() - timedelta(minutes=random.randint(0, 30))).isoformat()
        live_threats.append(threat)
    
    # Update AI status
    ai_status['threatsAnalyzed'] = len(threat_history)

# Initialize on startup
initialize_sample_data()

# ==================== API ROUTES ====================

@app.route('/')
def home():
    return jsonify({
        'message': 'Self-Adaptive Cyber Defense Mesh API',
        'version': '2.0.0',
        'status': 'active',
        'features': ['Real-time monitoring', 'User input', 'Analytics', 'PDF Reports'],
        'note': 'Student demo project with simulated data'
    })

@app.route('/api/live-threats')
def get_live_threats():
    """Get last 10 live threats"""
    return jsonify({
        'success': True,
        'count': len(live_threats),
        'threats': sorted(live_threats, key=lambda x: x['timestamp'], reverse=True)[:10]
    })

@app.route('/api/threat-history')
def get_threat_history():
    """Get all threat history"""
    return jsonify({
        'success': True,
        'count': len(threat_history),
        'threats': sorted(threat_history, key=lambda x: x['timestamp'], reverse=True)
    })

@app.route('/api/blockchain-ledger')
def get_blockchain_ledger():
    """Get blockchain blocks"""
    return jsonify({
        'success': True,
        'totalBlocks': len(blockchain_ledger),
        'blocks': sorted(blockchain_ledger, key=lambda x: x['blockNumber'], reverse=True)[:50]
    })

@app.route('/api/nodes-status')
def get_nodes_status():
    """Get nodes status"""
    # Update sync times
    for node in nodes_status:
        node['lastSyncTime'] = datetime.now().isoformat()
        node['latency'] = f"{random.randint(10, 100)}ms"
    
    return jsonify({
        'success': True,
        'totalNodes': len(nodes_status),
        'nodes': nodes_status
    })

@app.route('/api/ai-status')
def get_ai_status():
    """Get AI model status"""
    ai_status['threatsAnalyzed'] = len(threat_history) + len(user_submitted_threats)
    ai_status['updatedAt'] = datetime.now().isoformat()
    
    return jsonify({
        'success': True,
        'aiStatus': ai_status
    })

@app.route('/api/response-logs')
def get_response_logs():
    """Get response logs"""
    return jsonify({
        'success': True,
        'count': len(response_logs),
        'logs': sorted(response_logs, key=lambda x: x['timestamp'], reverse=True)[:50]
    })

# ==================== USER INPUT ENDPOINT ====================

@app.route('/api/submit-threat', methods=['POST'])
def submit_threat():
    """Accept user-submitted threat for monitoring"""
    try:
        data = request.json
        
        # Validate required fields
        required_fields = ['ip', 'threatType', 'severity']
        if not all(field in data for field in required_fields):
            return jsonify({
                'success': False,
                'message': 'Missing required fields: ip, threatType, severity'
            }), 400
        
        # Create threat object
        threat = {
            'threatId': f"USR-{random.randint(1000, 9999)}",
            'type': data['threatType'],
            'severity': data['severity'],
            'source': data.get('source', 'User Submitted'),
            'ip': data['ip'],
            'timestamp': datetime.now().isoformat(),
            'status': 'Monitoring',
            'description': data.get('description', f'User submitted {data["threatType"]} from {data["ip"]}'),
            'nodeId': random.choice(nodes_status)['nodeId'],
            'location': data.get('location', 'Unknown'),
            'protocol': data.get('protocol', 'Unknown'),
            'port': data.get('port', 0),
            'attackVector': data.get('attackVector', 'Unknown'),
            'confidence': 100.0,
            'userSubmitted': True
        }
        
        # Add to storage
        user_submitted_threats.append(threat)
        threat_history.append(threat)
        live_threats.append(threat)
        
        # Keep only last 10 live threats
        if len(live_threats) > 10:
            live_threats.pop(0)
        
        # Create blockchain block
        block = create_blockchain_block(threat)
        
        # Generate automated response
        response = generate_automated_response(threat)
        
        # Update AI status
        ai_status['threatsAnalyzed'] += 1
        
        return jsonify({
            'success': True,
            'message': 'Threat submitted successfully and is now being monitored',
            'threat': threat,
            'blockNumber': block['blockNumber'],
            'response': response['action'] if response else 'Monitoring',
            'monitoring': {
                'status': 'Active',
                'startTime': datetime.now().isoformat(),
                'alerts': True
            }
        }), 201
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error processing threat: {str(e)}'
        }), 500

# ==================== ANALYTICS ENDPOINTS ====================

@app.route('/api/analytics/overview')
def get_analytics_overview():
    """Get comprehensive analytics overview"""
    all_threats = threat_history + user_submitted_threats
    
    # Severity distribution
    severity_counts = Counter([t['severity'] for t in all_threats])
    
    # Threat type distribution
    type_counts = Counter([t['type'] for t in all_threats])
    
    # Hourly trends (last 24 hours)
    hourly_threats = {}
    now = datetime.now()
    for i in range(24):
        hour = (now - timedelta(hours=i)).strftime('%H:00')
        hourly_threats[hour] = 0
    
    for threat in all_threats:
        threat_time = datetime.fromisoformat(threat['timestamp'])
        if (now - threat_time).total_seconds() < 86400:
            hour = threat_time.strftime('%H:00')
            if hour in hourly_threats:
                hourly_threats[hour] += 1
    
    # Node performance
    node_performance = [
        {
            'nodeId': node['nodeId'],
            'location': node['location'],
            'threatsDetected': node['threatsDetected'],
            'uptime': node['uptime'],
            'efficiency': round(random.uniform(85, 99), 2)
        }
        for node in nodes_status
    ]
    
    # Response effectiveness
    successful_responses = len([r for r in response_logs if r['status'] == 'Success'])
    total_responses = len(response_logs)
    response_rate = round((successful_responses / total_responses * 100) if total_responses > 0 else 0, 2)
    
    return jsonify({
        'success': True,
        'analytics': {
            'totalThreats': len(all_threats),
            'userSubmittedThreats': len(user_submitted_threats),
            'blockedThreats': len([t for t in all_threats if t['status'] == 'Blocked']),
            'activeMonitoring': len([t for t in all_threats if t['status'] == 'Monitoring']),
            'severityDistribution': dict(severity_counts),
            'threatTypeDistribution': dict(type_counts),
            'hourlyTrends': hourly_threats,
            'nodePerformance': node_performance,
            'responseEffectiveness': response_rate,
            'blockchainIntegrity': '100%',
            'averageResponseTime': f"{random.randint(50, 200)}ms"
        }
    })

@app.route('/api/analytics/threats-trend')
def get_threats_trend():
    """Get threat trends over time"""
    all_threats = threat_history + user_submitted_threats
    
    # Last 7 days trend
    trends = []
    for i in range(7):
        date = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
        count = len([t for t in all_threats if t['timestamp'].startswith(date)])
        trends.append({
            'date': date,
            'count': count,
            'severity': {
                'Critical': random.randint(0, 5),
                'High': random.randint(2, 10),
                'Medium': random.randint(5, 15),
                'Low': random.randint(3, 8)
            }
        })
    
    return jsonify({
        'success': True,
        'trends': trends[::-1]  # Reverse to show oldest first
    })

# ==================== PDF REPORT GENERATION ====================

@app.route('/api/reports/generate/<section>', methods=['POST'])
def generate_report(section):
    """Generate PDF report for a specific section"""
    try:
        # Import reportlab for PDF generation
        from reportlab.lib.pagesizes import letter, A4
        from reportlab.lib import colors
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.enums import TA_CENTER, TA_LEFT
        
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)
        elements = []
        styles = getSampleStyleSheet()
        
        # Title style
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#1e3a8a'),
            spaceAfter=30,
            alignment=TA_CENTER
        )
        
        # Generate report based on section
        if section == 'live-threats':
            elements.append(Paragraph("Live Threats Report", title_style))
            elements.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
            elements.append(Spacer(1, 0.5*inch))
            
            # Table data
            data = [['Threat ID', 'Type', 'Severity', 'IP', 'Status']]
            for threat in live_threats[:20]:
                data.append([
                    threat['threatId'],
                    threat['type'][:20],
                    threat['severity'],
                    threat['ip'],
                    threat['status']
                ])
            
        elif section == 'threat-history':
            elements.append(Paragraph("Threat History Report", title_style))
            elements.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
            elements.append(Spacer(1, 0.5*inch))
            
            data = [['Threat ID', 'Type', 'Severity', 'IP', 'Timestamp']]
            for threat in threat_history[:30]:
                data.append([
                    threat['threatId'],
                    threat['type'][:20],
                    threat['severity'],
                    threat['ip'],
                    threat['timestamp'][:19]
                ])
            
        elif section == 'blockchain':
            elements.append(Paragraph("Blockchain Ledger Report", title_style))
            elements.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
            elements.append(Spacer(1, 0.5*inch))
            
            data = [['Block #', 'Threat Hash', 'Type', 'Status', 'Node']]
            for block in blockchain_ledger[:30]:
                data.append([
                    str(block['blockNumber']),
                    block['threatHash'][:12],
                    block['threatType'][:20],
                    block['verificationStatus'],
                    block['nodeId']
                ])
        
        elif section == 'nodes':
            elements.append(Paragraph("Node Status Report", title_style))
            elements.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
            elements.append(Spacer(1, 0.5*inch))
            
            data = [['Node ID', 'Location', 'Status', 'Threats', 'Uptime']]
            for node in nodes_status:
                data.append([
                    node['nodeId'],
                    node['location'],
                    node['status'],
                    str(node['threatsDetected']),
                    node['uptime']
                ])
        
        elif section == 'response-logs':
            elements.append(Paragraph("Response Logs Report", title_style))
            elements.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
            elements.append(Spacer(1, 0.5*inch))
            
            data = [['Log ID', 'Action', 'IP', 'Severity', 'Status']]
            for log in response_logs[:30]:
                data.append([
                    log['logId'],
                    log['action'][:20],
                    log['targetIp'],
                    log['severity'],
                    log['status']
                ])
        
        elif section == 'analytics':
            elements.append(Paragraph("Analytics Report", title_style))
            elements.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
            elements.append(Spacer(1, 0.5*inch))
            
            analytics = get_analytics_overview().json['analytics']
            
            data = [
                ['Metric', 'Value'],
                ['Total Threats', str(analytics['totalThreats'])],
                ['User Submitted', str(analytics['userSubmittedThreats'])],
                ['Blocked Threats', str(analytics['blockedThreats'])],
                ['Response Rate', f"{analytics['responseEffectiveness']}%"],
                ['Blockchain Integrity', analytics['blockchainIntegrity']]
            ]
        
        else:
            return jsonify({'success': False, 'message': 'Invalid section'}), 400
        
        # Create table
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e3a8a')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        elements.append(table)
        
        # Build PDF
        doc.build(elements)
        buffer.seek(0)
        
        return send_file(
            buffer,
            mimetype='application/pdf',
            as_attachment=True,
            download_name=f'{section}_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
        )
        
    except ImportError:
        return jsonify({
            'success': False,
            'message': 'PDF generation library not installed. Run: pip install reportlab'
        }), 500
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error generating report: {str(e)}'
        }), 500

# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    return jsonify({'success': False, 'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'success': False, 'error': 'Internal server error'}), 500

# ==================== RUN APP ====================

if __name__ == '__main__':
    print("=" * 70)
    print("🛡️  Self-Adaptive Cyber Defense Mesh API Server v2.0")
    print("=" * 70)
    print("⚠️  STUDENT DEMO PROJECT - ENHANCED WITH USER INPUT & ANALYTICS")
    print("📍 Server: http://localhost:5001")
    print("=" * 70)
    print("\n📡 Available Endpoints:")
    print("  GET  /api/live-threats          - Live threats")
    print("  GET  /api/threat-history        - All threats")
    print("  GET  /api/blockchain-ledger     - Blockchain")
    print("  GET  /api/nodes-status          - Nodes")
    print("  GET  /api/ai-status             - AI Model")
    print("  GET  /api/response-logs         - Responses")
    print("  POST /api/submit-threat         - Submit threat (USER INPUT)")
    print("  GET  /api/analytics/overview    - Analytics")
    print("  GET  /api/analytics/threats-trend - Trends")
    print("  POST /api/reports/generate/<section> - PDF Reports")
    print("=" * 70)
    
    app.run(debug=True, host='0.0.0.0', port=5001)
