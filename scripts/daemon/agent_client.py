#!/usr/bin/env python3
"""
Agent Zero Client - Send tasks to running Agent Zero daemon
"""
import sys
import time
sys.path.insert(0, '/mnt/user-data/python-packages')
sys.path.insert(0, '/mnt/user-data/naja-repo')

from agent import AgentContext, UserMessage
from initialize import initialize_agent

def send_task(task_text, wait_time=30):
    """Send task and wait for response"""
    print(f"📝 Task: {task_text}")
    print("="*80)
    
    # Get or create context
    context = AgentContext.current() or AgentContext.first()
    if not context:
        print("Creating new Agent context...")
        config = initialize_agent()
        context = AgentContext(config=config)
    
    print(f"✅ Using context: {context.id}\n")
    
    # Send message
    msg = UserMessage(
        message=task_text,
        attachments=[],
        system_message=[]
    )
    
    initial_logs = len(context.log.logs)
    task = context.communicate(msg)
    
    print(f"⏰ Waiting {wait_time}s for response...\n")
    time.sleep(wait_time)
    
    # Print response
    print("="*80)
    print("AGENT ZERO RESPONSE:")
    print("="*80 + "\n")
    
    for log in context.log.logs[initial_logs:]:
        if log.type in ['agent', 'response', 'tool', 'code_exe']:
            if log.heading:
                print(f"\n[{log.type.upper()}] {log.heading}")
            if log.content:
                content = str(log.content)
                if len(content) > 1000:
                    print(content[:1000] + "\n...[truncated]...")
                else:
                    print(content)
    
    print("\n" + "="*80)
    return context

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 agent_client.py 'your task here' [wait_time]")
        print("Example: python3 agent_client.py 'Execute: print(2+2)' 30")
        sys.exit(1)
    
    task = sys.argv[1]
    wait = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    
    send_task(task, wait)
