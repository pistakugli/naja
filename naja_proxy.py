"""
NAJA Proxy Server - prima zahtjeve od NAJA i vraca ih kroz localhost
da browser artifact moze da ih prosledi na Anthropic API
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, origins="*")

# Queue za razmenu poruka
pending_requests = {}
pending_responses = {}
request_counter = [0]

@app.route('/proxy/request', methods=['POST'])
def receive_request():
    """NAJA salje zahtjev ovdje"""
    data = request.json
    req_id = str(request_counter[0])
    request_counter[0] += 1
    pending_requests[req_id] = data
    
    # Cekaj odgovor (polling)
    import time
    timeout = 60
    start = time.time()
    while time.time() - start < timeout:
        if req_id in pending_responses:
            resp = pending_responses.pop(req_id)
            return jsonify(resp)
        time.sleep(0.1)
    
    return jsonify({"error": "timeout"}), 504

@app.route('/proxy/poll', methods=['GET'])
def poll_requests():
    """Browser pita ima li novih zahtjeva"""
    if pending_requests:
        req_id, data = next(iter(pending_requests.items()))
        return jsonify({"id": req_id, "request": data})
    return jsonify({"id": None})

@app.route('/proxy/respond', methods=['POST'])
def receive_response():
    """Browser vraca odgovor"""
    data = request.json
    req_id = data.get('id')
    pending_requests.pop(req_id, None)
    pending_responses[req_id] = data.get('response')
    return jsonify({"ok": True})

@app.route('/proxy/health', methods=['GET'])
def health():
    return jsonify({"ok": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)
