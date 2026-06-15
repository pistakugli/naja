"""
Bridge koji prima Anthropic-format zahtjeve od NAJA/litellm
i prosljedjuje ih browser proxyu (port 5001) koji ima pristup Anthropic API.
"""
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app, origins="*")

BROWSER_PROXY = "http://localhost:5001/proxy"

@app.route('/v1/messages', methods=['POST'])
def messages():
    """Prima zahtjev u Anthropic formatu, salje browser proxyu."""
    payload = request.json
    
    try:
        # Salje browser proxyu
        resp = requests.post(
            f"{BROWSER_PROXY}/request",
            json=payload,
            timeout=120
        )
        resp.raise_for_status()
        data = resp.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({
            "type": "error",
            "error": {"type": "api_error", "message": str(e)}
        }), 500

@app.route('/v1/models', methods=['GET'])
def models():
    return jsonify({
        "data": [{"id": "claude-sonnet-4-6", "object": "model"}]
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"ok": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=False)
