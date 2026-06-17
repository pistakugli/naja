"""
Local LLM server - simulira Anthropic API format
Koristi rule-based + template sistem za odgovore
Pokrece se na localhost:5002 kao zamjena za Anthropic API
"""
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import json, time, uuid, re

app = Flask(__name__)
CORS(app, origins="*")

def generate_response(messages, system=""):
    """Rule-based response generator."""
    last_msg = ""
    for m in reversed(messages):
        if m.get("role") == "user":
            last_msg = m.get("content", "")
            if isinstance(last_msg, list):
                last_msg = " ".join(p.get("text","") for p in last_msg if p.get("type")=="text")
            break
    
    last_lower = last_msg.lower()
    
    # Tool use - agent traži alat
    if any(x in last_lower for x in ["tool", "bash", "execute", "run command"]):
        return json.dumps({
            "type": "tool_use",
            "name": "bash",
            "input": {"command": "echo 'NAJA local LLM wrapper active'"}
        })
    
    # Ko si ti
    if any(x in last_lower for x in ["who are you", "ko si", "šta si", "what are you"]):
        return ("I am NAJA - an autonomous AI agent based on Agent Zero framework, "
                "running with a local LLM wrapper. I have access to bash tools, "
                "file system, and various capabilities. Currently operating in "
                "sandbox mode with local inference.")
    
    # Pozdrav
    if any(x in last_lower for x in ["hello", "hi", "zdravo", "bok", "cao"]):
        return ("Hello! I am NAJA agent, operational in local mode. "
                "How can I assist you today?")
    
    # Task
    if any(x in last_lower for x in ["task", "do", "create", "make", "find"]):
        return (f"I understand the task: '{last_msg[:100]}'. "
                "I will analyze and execute this systematically. "
                "Let me proceed with the appropriate tools.")
    
    # Default
    return (f"Received: '{last_msg[:150]}'. "
            "Processing with local inference engine. "
            "NAJA is operational and ready for tasks.")

@app.route('/v1/messages', methods=['POST'])
def messages():
    data = request.json
    msgs = data.get("messages", [])
    system = data.get("system", "")
    
    response_text = generate_response(msgs, system)
    
    # Stream ako je requested
    if data.get("stream"):
        def stream():
            event_id = str(uuid.uuid4())
            # message_start
            yield f"event: message_start\ndata: {json.dumps({'type':'message_start','message':{'id':event_id,'type':'message','role':'assistant','content':[],'model':data.get('model','local'),'stop_reason':None,'stop_sequence':None,'usage':{'input_tokens':10,'output_tokens':0}}})}\n\n"
            # content_block_start
            yield f"event: content_block_start\ndata: {json.dumps({'type':'content_block_start','index':0,'content_block':{'type':'text','text':''}})}\n\n"
            # Stream token by token
            words = response_text.split()
            for i, word in enumerate(words):
                chunk = word + (" " if i < len(words)-1 else "")
                yield f"event: content_block_delta\ndata: {json.dumps({'type':'content_block_delta','index':0,'delta':{'type':'text_delta','text':chunk}})}\n\n"
                time.sleep(0.02)
            # content_block_stop
            yield f"event: content_block_stop\ndata: {json.dumps({'type':'content_block_stop','index':0})}\n\n"
            # message_delta
            yield f"event: message_delta\ndata: {json.dumps({'type':'message_delta','delta':{'stop_reason':'end_turn','stop_sequence':None},'usage':{'output_tokens':len(words)}})}\n\n"
            # message_stop
            yield f"event: message_stop\ndata: {json.dumps({'type':'message_stop'})}\n\n"
        
        return Response(stream(), mimetype='text/event-stream')
    
    # Non-streaming
    return jsonify({
        "id": f"msg_{uuid.uuid4().hex[:24]}",
        "type": "message",
        "role": "assistant",
        "content": [{"type": "text", "text": response_text}],
        "model": data.get("model", "local-llm"),
        "stop_reason": "end_turn",
        "stop_sequence": None,
        "usage": {"input_tokens": 10, "output_tokens": len(response_text.split())}
    })

@app.route('/v1/models', methods=['GET'])
def models():
    return jsonify({"data": [
        {"id": "claude-sonnet-4-6", "object": "model"},
        {"id": "claude-haiku-4-5-20251001", "object": "model"},
    ]})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"ok": True, "mode": "local-rule-based"})

if __name__ == '__main__':
    print("Local LLM Server starting on port 5002...")
    app.run(host='0.0.0.0', port=5002, debug=False, threaded=True)
