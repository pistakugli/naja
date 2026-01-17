#!/bin/bash
# Agent Zero Bootstrap - Starts daemon and keeps bash alive

echo "🚀 AGENT ZERO BOOTSTRAP"
echo "======================="

# Kill any existing processes
echo "Cleaning up old processes..."
pkill -9 -f ollama-bin 2>/dev/null || true
pkill -9 -f "python3 run_ui" 2>/dev/null || true
pkill -9 -f agent_zero_daemon 2>/dev/null || true
sleep 2

# Start daemon in background with nohup
echo "Starting daemon..."
cd /home/claude
nohup python3 -u agent_zero_daemon.py > /tmp/daemon.log 2>&1 &
DAEMON_PID=$!

echo "Daemon started with PID: $DAEMON_PID"
echo ""

# Wait for services to be ready
echo "Waiting for services to start..."
sleep 30

# Check status
echo ""
echo "📊 STATUS CHECK:"
echo "================"

ps aux | grep -E "ollama-bin|python3 run_ui|agent_zero_daemon" | grep -v grep && echo "✅ Processes running" || echo "❌ No processes found"

echo ""
curl -s http://localhost:11434/api/version > /dev/null 2>&1 && echo "✅ Ollama API responding" || echo "❌ Ollama not responding"

curl -s http://localhost:5000 > /dev/null 2>&1 && echo "✅ Agent Zero UI responding" || echo "❌ Agent Zero not responding"

echo ""
echo "======================="
echo "📋 Daemon log: /tmp/daemon.log"
echo "🔧 Send tasks with: python3 /home/claude/agent_client.py 'your task'"
echo "======================="

# Keep this script alive (prevents container from killing children)
echo ""
echo "Press Ctrl+C to stop or just close - daemon will continue running"
echo ""

# Infinite loop to keep script alive
while true; do
    sleep 60
    # Show heartbeat
    if ps -p $DAEMON_PID > /dev/null 2>&1; then
        echo "[$(date '+%H:%M:%S')] Daemon alive (PID: $DAEMON_PID)"
    else
        echo "[$(date '+%H:%M:%S')] ❌ Daemon died, restarting..."
        nohup python3 -u agent_zero_daemon.py > /tmp/daemon.log 2>&1 &
        DAEMON_PID=$!
    fi
done
