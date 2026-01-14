# NAJA - Root/Sudo Configuration Guide

## 🔐 Enabling Root Privileges for Agent Zero

Since Agent Zero runs on **bare metal** (not Docker), it needs proper system privileges for:
- System administration
- Kali security tools requiring root
- Network configuration
- Service management
- Package installation

## Option 1: Passwordless Sudo (RECOMMENDED)

**Best for:** Production use, automated tasks, security tools

### Setup Steps:

**1. Create sudoers file for Agent Zero:**
```bash
sudo visudo -f /etc/sudoers.d/agent-zero
```

**2. Add this line (replace `YOUR_USERNAME` with actual user):**
```
YOUR_USERNAME ALL=(ALL) NOPASSWD: ALL
```

**3. Save and exit (Ctrl+X, then Y, then Enter)**

**4. Verify configuration:**
```bash
sudo -l
```

**5. Test passwordless sudo:**
```bash
sudo whoami
# Should output: root (without asking for password)
```

**Example for user 'pista':**
```bash
sudo visudo -f /etc/sudoers.d/agent-zero
# Add line:
pista ALL=(ALL) NOPASSWD: ALL
```

### Restrict to Specific Commands (More Secure):

If you want to limit sudo to specific commands only:

```
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/bin/apt-get, /usr/bin/systemctl, /usr/sbin/iptables, /usr/bin/nmap
```

## Option 2: Run Agent Zero as Root

**Best for:** Testing, lab environments, maximum control

### Method A: Direct root execution
```bash
sudo python run_ui.py
```

### Method B: Change ownership to root
```bash
sudo chown -R root:root /path/to/naja
sudo chmod -R 755 /path/to/naja
```

Then run as root:
```bash
sudo -i
cd /path/to/naja
python run_ui.py
```

### Method C: Create systemd service running as root
```bash
sudo nano /etc/systemd/system/agent-zero.service
```

Content:
```ini
[Unit]
Description=Agent Zero AI System
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/path/to/naja
ExecStart=/usr/bin/python3 /path/to/naja/run_ui.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable agent-zero
sudo systemctl start agent-zero
sudo systemctl status agent-zero
```

## Option 3: Hybrid Approach (Most Secure)

Run Agent Zero as normal user, but with passwordless sudo for specific tasks:

**1. Agent Zero runs as:** Regular user (e.g., pista)
**2. Sudo config:** Passwordless for required commands only
**3. system_admin tool:** Uses sudo automatically

### Recommended sudoers configuration:
```bash
sudo visudo -f /etc/sudoers.d/agent-zero
```

Add:
```
# Agent Zero - Passwordless sudo for essential tools
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/bin/apt-get
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/bin/apt
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/bin/systemctl
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/sbin/iptables
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/sbin/ufw
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/bin/nmap
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/bin/masscan
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/sbin/airmon-ng
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/sbin/aircrack-ng
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/bin/wireshark
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/bin/tshark
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/bin/ettercap
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/bin/msfconsole
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/bin/john
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/bin/hashcat
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/bin/hydra
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/bin/nikto
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/bin/sqlmap
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/bin/gobuster
YOUR_USERNAME ALL=(ALL) NOPASSWD: /sbin/modprobe
YOUR_USERNAME ALL=(ALL) NOPASSWD: /bin/mount
YOUR_USERNAME ALL=(ALL) NOPASSWD: /bin/umount
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/sbin/useradd
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/sbin/userdel
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/sbin/usermod
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/bin/chown
YOUR_USERNAME ALL=(ALL) NOPASSWD: /usr/bin/chmod
```

## Security Considerations

### ⚠️ Risks of Passwordless Sudo:
- **Compromised account** = full system access
- **Malicious scripts** can run as root
- **No password prompt** = no second chance to cancel

### ✅ Mitigation Strategies:
1. **Strong SSH key authentication** (disable password login)
2. **Firewall rules** limiting access
3. **Audit logging** enabled:
   ```bash
   sudo apt-get install auditd
   sudo systemctl enable auditd
   sudo systemctl start auditd
   ```
4. **Command logging** to track all sudo usage:
   ```bash
   # Add to /etc/sudoers (via visudo):
   Defaults log_input, log_output
   Defaults iolog_dir=/var/log/sudo-io
   ```
5. **Regular monitoring** of sudo logs:
   ```bash
   sudo grep sudo /var/log/auth.log
   ```

## Kali Linux Specific

On Kali Linux, root is often the default user. To run Agent Zero optimally:

### Option 1: Run as root (typical Kali setup)
```bash
# Already root in Kali
cd /media/pista/agent/naja
python run_ui.py
```

### Option 2: Create non-root user with sudo
```bash
# As root:
useradd -m -s /bin/bash pista
usermod -aG sudo pista
echo "pista ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/pista

# Switch to user:
su - pista
cd /media/pista/agent/naja
python run_ui.py
```

## Verification

After setup, verify that Agent Zero has proper access:

**1. Test sudo access:**
```bash
sudo whoami
# Should output: root (without password prompt)
```

**2. Test system_admin tool:**
Start Agent Zero and ask it to:
- "Check system status with systemctl"
- "Show firewall rules"
- "List installed packages"

**3. Test Kali tools requiring root:**
- "Scan with nmap -sS"
- "Show network interfaces"
- "List loaded kernel modules"

## Current Setup (Your System)

**System:** Kali Linux (likely)
**User:** pista
**Path:** /media/pista/agent/naja

**Recommended command:**
```bash
sudo visudo -f /etc/sudoers.d/agent-zero
# Add line:
pista ALL=(ALL) NOPASSWD: ALL
```

Then verify:
```bash
sudo -l
sudo whoami  # Should output 'root' without password
```

## Troubleshooting

**"Sorry, user X is not allowed to execute Y"**
→ Run: `sudo visudo` and check sudoers configuration

**"sudo: a password is required"**
→ Verify NOPASSWD is set in sudoers file

**Permission denied even with sudo**
→ Some operations need actual root user (not just sudo)
→ Try: `sudo -i` to become root, then run command

**SELinux/AppArmor blocking**
→ Check: `sudo aa-status` or `getenforce`
→ May need to disable or configure policies

## Summary

**For Production:**
✅ Passwordless sudo (Option 1) - RECOMMENDED
✅ Restricted to specific commands (Option 3) - MOST SECURE

**For Testing/Lab:**
✅ Run as root (Option 2) - SIMPLEST

**For Kali:**
✅ Already root - just run (typical setup)
✅ Or create user with passwordless sudo

**Remember:**
🔐 With great power comes great responsibility
⚠️ Audit and monitor all system changes
🛡️ Use firewalls and access controls
📝 Document all configuration changes
