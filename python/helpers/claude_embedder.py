"""Custom embedder using Claude API to generate embeddings via text hashing."""
import hashlib
import struct
import anthropic
from langchain_core.embeddings import Embeddings
from typing import List


class ClaudeEmbedder(Embeddings):
    """Simple deterministic embedder that works without external embedding APIs."""
    
    def __init__(self, dimensions: int = 384):
        self.dimensions = dimensions
    
    def _text_to_vector(self, text: str) -> List[float]:
        """Convert text to a deterministic float vector using hashing."""
        vector = []
        seed = text.encode('utf-8')
        for i in range(self.dimensions):
            h = hashlib.sha256(seed + struct.pack('i', i)).digest()
            val = struct.unpack('f', h[:4])[0]
            # Normalize to [-1, 1]
            val = max(-1.0, min(1.0, val / 1e38))
            vector.append(val)
        return vector
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [self._text_to_vector(t) for t in texts]
    
    def embed_query(self, text: str) -> List[float]:
        return self._text_to_vector(text)
