"""Custom model provider koji salje zahtjeve kroz browser proxy."""
import requests
import json
from typing import Any

PROXY_URL = "http://localhost:5001/proxy/request"

def call_via_proxy(messages: list, model: str = "claude-sonnet-4-6", max_tokens: int = 4096, system: str = None) -> str:
    """Salji poruku kroz browser proxy i cekaj odgovor."""
    payload = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": messages,
    }
    if system:
        payload["system"] = system
    
    resp = requests.post(PROXY_URL, json=payload, timeout=120)
    resp.raise_for_status()
    data = resp.json()
    
    # Anthropic format
    if "content" in data:
        for block in data["content"]:
            if block.get("type") == "text":
                return block["text"]
    return str(data)
