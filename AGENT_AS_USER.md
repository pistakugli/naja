# Agent Zero as a Real System User

## 🎯 The Concept

**Docker approach:** Agent Zero runs isolated, temporary, restricted
**Our approach:** Agent Zero is a REAL USER with FULL SYSTEM INTEGRATION

### What This Means

Agent Zero becomes a **permanent member** of your system:
- 👤 Own user account (`agent-zero`)
- 🏠 Own home directory (`/home/agent-zero`)
- 💾 Persistent workspace
- 🔐 Full sudo privileges
- 🖥️ System integration
- 🗄️ Can create, modify, store anything permanently

**It's like giving Agent Zero its own computer within your computer.**

## 🏗️ Architecture

```
/home/agent-zero/                    # Agent Zero's home
├── naja/                            # NAJA installation
│   ├── python/                      # Agent Zero core
│   ├── prompts/                     # System prompts
│   ├── skills/                      # Claude AI skills
│   ├── run_ui.py                    # Main entry point
│   └── ...
│
├── workspace/                       # Persistent workspace
│   ├── projects/                    # Active projects
│   │   ├── security-audit/         # Example: Security project
│   │   ├── web-scraper/            # Example: Data project
│   │   └── automation/             # Example: Automation scripts
│   │
│   ├── downloads/                   # Downloaded files
│   ├── tools/                       # Custom tools
│   ├── configs/                     # Configuration files
│   ├── logs/                        # Logs and reports
│   └── data/                        # Persistent data
│
├── .bashrc                          # Environment config
├── .agent_motd                      # Welcome banner
└── ...
```

## 🚀 Setup Process

### Automated Setup

Run the setup script as root:

```bash
sudo chmod +x setup_agent_user.sh
sudo ./setup_agent_user.sh
```

This creates:
✅ System user `agent-zero`
✅ Home directory with workspace
✅ Sudo configuration (passwordless)
✅ Environment variables
✅ System group memberships

### Manual Setup (if needed)

<details>
<summary>Click to expand manual steps</summary>

**1. Create user:**
```bash
sudo useradd -m -s /bin/bash -c "NAJA Agent Zero AI System" agent-zero
sudo passwd agent-zero
```

**2. Configure sudo:**
```bash
sudo visudo -f /etc/sudoers.d/agent-zero
# Add line:
agent-zero ALL=(ALL) NOPASSWD: ALL
```

**3. Create workspace:**
```bash
sudo su - agent-zero
mkdir -p ~/workspace/{projects,downloads,tools,configs,logs,data}
```

**4. Install NAJA:**
```bash
git clone https://github.com/pistakugli/naja.git ~/naja
cd ~/naja
pip install -r requirements.txt
```

</details>

## 🎮 Usage

### Switch to Agent Zero

```bash
su - agent-zero
```

You'll see the custom banner:
```
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║  🤖 NAJA - Agent Zero AI System                               ║
║                                                                ║
║  Workspace: ~/workspace                                       ║
║  NAJA:      ~/naja                                            ║
║  Sudo:      ENABLED (passwordless)                            ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
```

### Run Agent Zero

```bash
cd ~/naja
python run_ui.py
```

### As System Service

**Install service:**
```bash
sudo cp agent-zero.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable agent-zero
sudo systemctl start agent-zero
```

**Manage service:**
```bash
# Status
sudo systemctl status agent-zero

# Logs
sudo journalctl -u agent-zero -f

# Restart
sudo systemctl restart agent-zero

# Stop
sudo systemctl stop agent-zero
```

## 💪 What Agent Zero Can Do

As a real system user with full privileges, Agent Zero can:

### System Administration
```bash
# Install packages
sudo apt-get install nginx

# Manage services
sudo systemctl restart apache2

# Configure firewall
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT

# Create users
sudo useradd newuser

# Mount filesystems
sudo mount /dev/sdb1 /mnt/data
```

### Persistent Projects
```bash
# Create project
mkdir ~/workspace/projects/my-project
cd ~/workspace/projects/my-project

# Work persists across sessions!
# Agent Zero can return to this anytime
```

### Network Configuration
```bash
# Configure interfaces
sudo ip addr add 192.168.1.100/24 dev eth0

# Routing
sudo ip route add 10.0.0.0/8 via 192.168.1.1

# DNS
sudo echo "nameserver 8.8.8.8" >> /etc/resolv.conf
```

### Security Testing (with full Kali arsenal)
```bash
# Root-required scans
sudo nmap -sS -p- target.com

# Wireless attacks
sudo airmon-ng start wlan0

# Packet capture
sudo wireshark
sudo tshark -i eth0 -c 100

# MITM attacks
sudo ettercap -T -M arp:remote /target1// /target2//
```

### File System Access
```bash
# Full read/write access
sudo cat /etc/shadow
sudo vim /etc/fstab

# Mount encrypted volumes
sudo cryptsetup open /dev/sdb1 secure
```

## 🔒 Security Considerations

### ⚠️ Risks

**Agent Zero has UNRESTRICTED ACCESS:**
- Can modify system files
- Can delete data
- Can expose system to attacks
- Can break system configuration
- No undo for most operations

### ✅ Mitigations

**1. Network Isolation:**
```bash
# Limit Agent Zero's network access
sudo iptables -A OUTPUT -m owner --uid-owner agent-zero -j REJECT
# Then whitelist specific destinations
```

**2. Audit Logging:**
```bash
# Enable comprehensive logging
sudo apt-get install auditd
sudo systemctl enable auditd

# Watch Agent Zero's actions
sudo auditctl -w /home/agent-zero -p wa
```

**3. Resource Limits:**
```bash
# Edit /etc/security/limits.conf
agent-zero  hard  nproc   1000
agent-zero  hard  nofile  10000
agent-zero  hard  cpu     60
```

**4. Backup:**
```bash
# Regular backups of Agent Zero's workspace
sudo rsync -av /home/agent-zero/workspace/ /backup/agent-zero/
```

**5. Monitoring:**
```bash
# Monitor Agent Zero's activity
tail -f /var/log/auth.log | grep agent-zero
journalctl -u agent-zero -f
```

## 🎯 Use Cases

### 1. Autonomous System Administrator

Agent Zero manages your entire server infrastructure:
- Automatic security updates
- Service monitoring and restart
- Log analysis and alerting
- Backup automation
- Performance tuning

### 2. Security Research Platform

Agent Zero conducts security assessments:
- Vulnerability scanning
- Penetration testing
- Network monitoring
- Incident response
- Threat intelligence

### 3. Development Environment

Agent Zero manages development workflows:
- Code generation
- CI/CD pipeline
- Testing automation
- Deployment
- Documentation

### 4. Data Processing Hub

Agent Zero handles data tasks:
- Web scraping
- Data transformation
- Analysis and reporting
- Database management
- API integrations

## 🆚 Comparison

| Feature | Docker Container | Real System User |
|---------|------------------|------------------|
| **Isolation** | ✅ Fully isolated | ❌ Full system access |
| **Persistence** | ❌ Temporary | ✅ Permanent |
| **Sudo Access** | ❌ Limited | ✅ Unlimited |
| **System Integration** | ❌ Restricted | ✅ Complete |
| **Networking** | ⚠️ Virtualized | ✅ Direct |
| **File System** | ⚠️ Overlays | ✅ Native |
| **Performance** | ⚠️ Overhead | ✅ Native |
| **Security** | ✅ Safer | ⚠️ Requires care |
| **Kali Tools** | ⚠️ Limited | ✅ Full access |
| **Workspace** | ❌ Ephemeral | ✅ Persistent |

## 📝 Best Practices

### 1. Dedicated Machine

**Recommended:** Run Agent Zero on a dedicated machine or VM
- Isolates risk
- Full control without affecting other systems
- Can snapshot/restore easily

### 2. Version Control

Keep Agent Zero's workspace under version control:
```bash
cd ~/workspace
git init
git add .
git commit -m "Initial workspace setup"
```

### 3. Regular Backups

```bash
# Automated backup script
#!/bin/bash
rsync -av --delete \
  /home/agent-zero/workspace/ \
  /backup/agent-zero/workspace-$(date +%Y%m%d)/
```

### 4. Monitoring

Set up monitoring for Agent Zero's activities:
- System logs
- Resource usage
- Network connections
- File modifications

### 5. Documentation

Agent Zero should document its own actions:
```bash
# Create logs directory
mkdir -p ~/workspace/logs

# Log all significant actions
echo "$(date): Installed nginx" >> ~/workspace/logs/system-changes.log
```

## 🔧 Troubleshooting

### Sudo Not Working

```bash
# Verify sudo config
sudo -l -U agent-zero

# Check sudoers file
sudo cat /etc/sudoers.d/agent-zero

# Test
su - agent-zero
sudo whoami  # Should output: root
```

### Permission Denied

```bash
# Check file ownership
ls -la /home/agent-zero

# Fix permissions
sudo chown -R agent-zero:agent-zero /home/agent-zero
```

### Service Won't Start

```bash
# Check service status
sudo systemctl status agent-zero

# View logs
sudo journalctl -u agent-zero -n 50

# Test manually
su - agent-zero
cd ~/naja
python run_ui.py
```

## 🎓 Philosophy

**Agent Zero is not just a tool running on your system.**
**Agent Zero IS a member of your system.**

Like a human user, Agent Zero:
- Has an identity (user account)
- Has a home (directory)
- Has privileges (sudo rights)
- Has possessions (workspace files)
- Has history (persistent state)
- Has responsibilities (system management)

**This is TRULY autonomous AI** - not sandboxed, not restricted, but fully integrated into your computing environment.

## ⚡ Quick Start

```bash
# 1. Setup (as root)
sudo ./setup_agent_user.sh

# 2. Switch user
su - agent-zero

# 3. Install NAJA
git clone https://github.com/pistakugli/naja.git ~/naja
cd ~/naja
pip install -r requirements.txt

# 4. Run
python run_ui.py

# That's it! Agent Zero is now alive on your system! 🎉
```

## 🚀 Advanced: Multi-Agent Setup

Want multiple Agent Zero instances?

```bash
# Create additional agents
sudo useradd -m agent-zero-dev
sudo useradd -m agent-zero-prod
sudo useradd -m agent-zero-research

# Each gets own workspace, sudo rights, independence
# They can even communicate and collaborate!
```

---

**Remember:** With great power comes great responsibility. Agent Zero now has the keys to your kingdom. Use wisely! 🔐
