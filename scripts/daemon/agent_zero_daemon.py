#!/usr/bin/env python3
"""
Agent Zero Daemon - Keeps Ollama + Agent Zero alive permanently
"""
import subprocess
import time
import sys
import signal
import os
from pathlib import Path

class AgentZeroDaemon:
    def __init__(self):
        self.ollama_process = None
        self.agent_process = None
        self.running = True
        
    def signal_handler(self, sig, frame):
        """Handle shutdown gracefully"""
        print("\n🛑 Shutting down daemon...")
        self.running = False
        self.cleanup()
        sys.exit(0)
        
    def cleanup(self):
        """Kill child processes"""
        if self.ollama_process:
            print("Stopping Ollama...")
            self.ollama_process.terminate()
            self.ollama_process.wait(timeout=5)
        if self.agent_process:
            print("Stopping Agent Zero...")
            self.agent_process.terminate()
            self.agent_process.wait(timeout=5)
            
    def start_ollama(self):
        """Start Ollama server"""
        print("🚀 Starting Ollama...")
        self.ollama_process = subprocess.Popen(
            ['/mnt/user-data/ollama-bin', 'serve'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            preexec_fn=os.setsid  # Create new process group
        )
        
        # Wait for Ollama to be ready
        for i in range(30):
            try:
                result = subprocess.run(
                    ['curl', '-s', 'http://localhost:11434/api/version'],
                    capture_output=True,
                    timeout=2
                )
                if result.returncode == 0:
                    print("✅ Ollama is ready on port 11434")
                    return True
            except:
                pass
            time.sleep(1)
            
        print("❌ Ollama failed to start")
        return False
        
    def start_agent_zero(self):
        """Start Agent Zero"""
        print("🚀 Starting Agent Zero...")
        
        env = os.environ.copy()
        env['PYTHONPATH'] = '/mnt/user-data/python-packages:' + env.get('PYTHONPATH', '')
        
        self.agent_process = subprocess.Popen(
            ['python3', 'run_ui.py'],
            cwd='/mnt/user-data/naja-repo',
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            preexec_fn=os.setsid
        )
        
        # Wait for Agent Zero to be ready
        for i in range(60):
            try:
                result = subprocess.run(
                    ['curl', '-s', 'http://localhost:5000'],
                    capture_output=True,
                    timeout=2
                )
                if b'html' in result.stdout.lower():
                    print("✅ Agent Zero is ready on port 5000")
                    return True
            except:
                pass
            time.sleep(1)
            
        print("❌ Agent Zero failed to start")
        return False
        
    def monitor_processes(self):
        """Monitor and restart if needed"""
        while self.running:
            # Check Ollama
            if self.ollama_process.poll() is not None:
                print("⚠️  Ollama died, restarting...")
                self.start_ollama()
                
            # Check Agent Zero
            if self.agent_process.poll() is not None:
                print("⚠️  Agent Zero died, restarting...")
                self.start_agent_zero()
                
            time.sleep(5)
            
    def run(self):
        """Main daemon loop"""
        # Setup signal handlers
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
        
        print("="*80)
        print("🤖 AGENT ZERO DAEMON - STARTING")
        print("="*80)
        
        # Start services
        if not self.start_ollama():
            print("Failed to start Ollama, exiting")
            return 1
            
        if not self.start_agent_zero():
            print("Failed to start Agent Zero, exiting")
            self.cleanup()
            return 1
            
        print("\n" + "="*80)
        print("✅ ALL SERVICES RUNNING")
        print("="*80)
        print("📊 Ollama:      http://localhost:11434")
        print("🌐 Agent Zero:  http://localhost:5000")
        print("⌨️  Press Ctrl+C to stop")
        print("="*80 + "\n")
        
        # Monitor forever
        self.monitor_processes()
        
        return 0

if __name__ == '__main__':
    daemon = AgentZeroDaemon()
    sys.exit(daemon.run())
