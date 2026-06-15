from flask import Flask, request, jsonify
from flask_cors import CORS
import threading, time, queue, json

app = Flask(__name__)
CORS(app, origins="*")

request_queue = queue.Queue()
response_store = {}
response_events = {}
counter = [0]

@app.route('/proxy/request', methods=['POST'])
def receive_request():
    data = request.json
    req_id = str(counter[0]); counter[0] += 1
    event = threading.Event()
    response_events[req_id] = event
    request_queue.put({"id": req_id, "request": data})
    # Cekaj max 90s na browser odgovor
    if event.wait(timeout=90):
        resp = response_store.pop(req_id, {"error": "no response"})
        return jsonify(resp)
    return jsonify({"type":"error","error":{"type":"timeout","message":"Browser proxy timeout"}}), 504

@app.route('/proxy/poll', methods=['GET'])
def poll():
    try:
        item = request_queue.get_nowait()
        return jsonify(item)
    except queue.Empty:
        return jsonify({"id": None})

@app.route('/proxy/respond', methods=['POST'])
def respond():
    data = request.json
    req_id = data.get('id')
    response_store[req_id] = data.get('response')
    if req_id in response_events:
        response_events[req_id].set()
    return jsonify({"ok": True})

@app.route('/proxy/health', methods=['GET'])
def health():
    return jsonify({"ok": True, "pending": request_queue.qsize()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False, threaded=True)
