# system_admin - System Administration with Root Privileges

## 🔐 FULL SYSTEM ACCESS
This tool provides UNRESTRICTED system administration capabilities with root/sudo privileges.

**Use for:**
- System administration tasks
- Network configuration
- Service management
- Package installation
- User/group management
- Firewall configuration
- Hardware management
- Kali tools requiring root

## ⚠️ CRITICAL WARNINGS

**EXTREME CAUTION REQUIRED:**
- Can modify/delete ANY system file
- Can break system if misused
- No safety nets - direct system access
- User assumes ALL responsibility

**Running on BARE METAL:**
This is NOT a Docker container - this is the ACTUAL system.
Mistakes can render the system unusable.

## System Administration Categories

### 📦 Package Management

**APT (Debian/Ubuntu/Kali):**
```python
# Update package lists
tool: "system_admin"
args: {
  "command": "apt-get update",
  "use_sudo": true
}

# Upgrade all packages
tool: "system_admin"
args: {
  "command": "apt-get upgrade -y",
  "use_sudo": true
}

# Install packages
tool: "system_admin"
args: {
  "command": "apt-get install -y nmap wireshark burpsuite",
  "use_sudo": true
}

# Remove packages
tool: "system_admin"
args: {
  "command": "apt-get remove -y package-name",
  "use_sudo": true
}

# Search for packages
tool: "system_admin"
args: {
  "command": "apt-cache search keyword",
  "use_sudo": false
}
```

**DNF/YUM (Fedora/RHEL):**
```python
tool: "system_admin"
args: {
  "command": "dnf install -y package-name",
  "use_sudo": true
}
```

**Pacman (Arch):**
```python
tool: "system_admin"
args: {
  "command": "pacman -Syu",
  "use_sudo": true
}
```

### 🔧 Service Management (systemd)

```python
# Start service
tool: "system_admin"
args: {
  "command": "systemctl start nginx",
  "use_sudo": true
}

# Stop service
tool: "system_admin"
args: {
  "command": "systemctl stop apache2",
  "use_sudo": true
}

# Restart service
tool: "system_admin"
args: {
  "command": "systemctl restart postgresql",
  "use_sudo": true
}

# Enable service (start on boot)
tool: "system_admin"
args: {
  "command": "systemctl enable docker",
  "use_sudo": true
}

# Check service status
tool: "system_admin"
args: {
  "command": "systemctl status ssh",
  "use_sudo": false
}

# View service logs
tool: "system_admin"
args: {
  "command": "journalctl -u nginx -n 50",
  "use_sudo": true
}

# List all services
tool: "system_admin"
args: {
  "command": "systemctl list-units --type=service",
  "use_sudo": false
}
```

### 👥 User & Group Management

```python
# Create user
tool: "system_admin"
args: {
  "command": "useradd -m -s /bin/bash username",
  "use_sudo": true
}

# Set user password
tool: "system_admin"
args: {
  "command": "echo 'username:password' | chpasswd",
  "use_sudo": true
}

# Add user to group
tool: "system_admin"
args: {
  "command": "usermod -aG sudo username",
  "use_sudo": true
}

# Delete user
tool: "system_admin"
args: {
  "command": "userdel -r username",
  "use_sudo": true
}

# Create group
tool: "system_admin"
args: {
  "command": "groupadd groupname",
  "use_sudo": true
}

# List all users
tool: "system_admin"
args: {
  "command": "cat /etc/passwd",
  "use_sudo": false
}

# Show user info
tool: "system_admin"
args: {
  "command": "id username",
  "use_sudo": false
}
```

### 🌐 Network Administration

**Network Interfaces:**
```python
# Show network interfaces
tool: "system_admin"
args: {
  "command": "ip addr show",
  "use_sudo": false
}

# Configure static IP
tool: "system_admin"
args: {
  "command": "ip addr add 192.168.1.100/24 dev eth0",
  "use_sudo": true
}

# Bring interface up/down
tool: "system_admin"
args: {
  "command": "ip link set eth0 up",
  "use_sudo": true
}

# Show routing table
tool: "system_admin"
args: {
  "command": "ip route show",
  "use_sudo": false
}

# Add route
tool: "system_admin"
args: {
  "command": "ip route add 10.0.0.0/8 via 192.168.1.1",
  "use_sudo": true
}
```

**Firewall (iptables):**
```python
# List firewall rules
tool: "system_admin"
args: {
  "command": "iptables -L -n -v",
  "use_sudo": true
}

# Allow SSH
tool: "system_admin"
args: {
  "command": "iptables -A INPUT -p tcp --dport 22 -j ACCEPT",
  "use_sudo": true
}

# Block IP
tool: "system_admin"
args: {
  "command": "iptables -A INPUT -s 192.168.1.100 -j DROP",
  "use_sudo": true
}

# Save iptables
tool: "system_admin"
args: {
  "command": "iptables-save > /etc/iptables/rules.v4",
  "use_sudo": true
}

# Flush all rules
tool: "system_admin"
args: {
  "command": "iptables -F",
  "use_sudo": true
}
```

**UFW (Uncomplicated Firewall):**
```python
# Enable UFW
tool: "system_admin"
args: {
  "command": "ufw enable",
  "use_sudo": true
}

# Allow port
tool: "system_admin"
args: {
  "command": "ufw allow 80/tcp",
  "use_sudo": true
}

# Show status
tool: "system_admin"
args: {
  "command": "ufw status verbose",
  "use_sudo": true
}
```

**DNS Configuration:**
```python
# Edit resolv.conf
tool: "system_admin"
args: {
  "command": "echo 'nameserver 8.8.8.8' >> /etc/resolv.conf",
  "use_sudo": true
}

# Test DNS
tool: "system_admin"
args: {
  "command": "nslookup google.com",
  "use_sudo": false
}
```

### 💾 Disk & Filesystem Management

```python
# Show disk usage
tool: "system_admin"
args: {
  "command": "df -h",
  "use_sudo": false
}

# Show directory sizes
tool: "system_admin"
args: {
  "command": "du -sh /*",
  "use_sudo": true
}

# Mount filesystem
tool: "system_admin"
args: {
  "command": "mount /dev/sdb1 /mnt/disk",
  "use_sudo": true
}

# Unmount filesystem
tool: "system_admin"
args: {
  "command": "umount /mnt/disk",
  "use_sudo": true
}

# Create filesystem
tool: "system_admin"
args: {
  "command": "mkfs.ext4 /dev/sdb1",
  "use_sudo": true
}

# Check filesystem
tool: "system_admin"
args: {
  "command": "fsck /dev/sdb1",
  "use_sudo": true
}

# List block devices
tool: "system_admin"
args: {
  "command": "lsblk",
  "use_sudo": false
}
```

### 🔒 File Permissions & Ownership

```python
# Change ownership
tool: "system_admin"
args: {
  "command": "chown user:group /path/to/file",
  "use_sudo": true
}

# Change permissions
tool: "system_admin"
args: {
  "command": "chmod 755 /path/to/file",
  "use_sudo": true
}

# Recursive ownership
tool: "system_admin"
args: {
  "command": "chown -R user:group /path/to/directory",
  "use_sudo": true
}

# Set SUID bit
tool: "system_admin"
args: {
  "command": "chmod u+s /path/to/binary",
  "use_sudo": true
}
```

### 🖥️ System Information & Monitoring

```python
# System info
tool: "system_admin"
args: {
  "command": "uname -a",
  "use_sudo": false
}

# CPU info
tool: "system_admin"
args: {
  "command": "lscpu",
  "use_sudo": false
}

# Memory usage
tool: "system_admin"
args: {
  "command": "free -h",
  "use_sudo": false
}

# Process list
tool: "system_admin"
args: {
  "command": "ps aux",
  "use_sudo": false
}

# Top processes
tool: "system_admin"
args: {
  "command": "top -b -n 1",
  "use_sudo": false
}

# Hardware info
tool: "system_admin"
args: {
  "command": "lshw -short",
  "use_sudo": true
}

# PCI devices
tool: "system_admin"
args: {
  "command": "lspci",
  "use_sudo": false
}

# USB devices
tool: "system_admin"
args: {
  "command": "lsusb",
  "use_sudo": false
}
```

### 🔐 Kali Tools Requiring Root

```python
# Nmap SYN scan (requires root)
tool: "system_admin"
args: {
  "command": "nmap -sS -p- 192.168.1.1",
  "use_sudo": true,
  "timeout": 600
}

# Aircrack-ng (requires root)
tool: "system_admin"
args: {
  "command": "airmon-ng start wlan0",
  "use_sudo": true
}

# Wireshark capture (requires root)
tool: "system_admin"
args: {
  "command": "tshark -i eth0 -c 100 -w capture.pcap",
  "use_sudo": true
}

# Ettercap MITM (requires root)
tool: "system_admin"
args: {
  "command": "ettercap -T -M arp:remote /192.168.1.1// /192.168.1.100//",
  "use_sudo": true
}

# Metasploit handler (may require root for ports <1024)
tool: "system_admin"
args: {
  "command": "msfconsole -x 'use exploit/multi/handler; set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST 192.168.1.10; set LPORT 443; run'",
  "use_sudo": true,
  "timeout": 600
}
```

### ⚙️ Kernel & Module Management

```python
# List loaded modules
tool: "system_admin"
args: {
  "command": "lsmod",
  "use_sudo": false
}

# Load module
tool: "system_admin"
args: {
  "command": "modprobe module_name",
  "use_sudo": true
}

# Remove module
tool: "system_admin"
args: {
  "command": "modprobe -r module_name",
  "use_sudo": true
}

# Show kernel version
tool: "system_admin"
args: {
  "command": "uname -r",
  "use_sudo": false
}

# View kernel messages
tool: "system_admin"
args: {
  "command": "dmesg | tail -50",
  "use_sudo": true
}
```

### 🔄 System Updates & Maintenance

```python
# Full system upgrade (Debian/Ubuntu/Kali)
tool: "system_admin"
args: {
  "command": "apt-get update && apt-get dist-upgrade -y",
  "use_sudo": true,
  "timeout": 1800
}

# Clean package cache
tool: "system_admin"
args: {
  "command": "apt-get clean && apt-get autoclean",
  "use_sudo": true
}

# Remove unused packages
tool: "system_admin"
args: {
  "command": "apt-get autoremove -y",
  "use_sudo": true
}

# Reboot system
tool: "system_admin"
args: {
  "command": "reboot",
  "use_sudo": true
}

# Shutdown system
tool: "system_admin"
args: {
  "command": "shutdown -h now",
  "use_sudo": true
}
```

## Parameters

- **command** (required): Shell command to execute
- **use_sudo** (optional): Use sudo for privilege escalation (default: true)
- **timeout** (optional): Command timeout in seconds (default: 300)
- **working_dir** (optional): Working directory for command execution

## Important Notes

1. **Root Access**: Many system tasks require root/sudo
2. **Sudo Configuration**: Ensure user has sudo rights or run Agent Zero as root
3. **Command Syntax**: Use proper shell syntax
4. **Timeouts**: Long-running commands need increased timeout
5. **Working Directory**: Some commands need specific working directories
6. **Error Handling**: Check command output for errors
7. **System State**: Commands can modify system permanently

## Security Best Practices

1. **Verify Commands**: Double-check destructive commands
2. **Backup**: Backup critical data before system changes
3. **Test**: Test commands in safe environment first
4. **Documentation**: Document all system changes
5. **Logging**: Enable command logging for audit trail
6. **Principle of Least Privilege**: Use sudo only when necessary
7. **Review**: Review automated scripts before execution

## Troubleshooting

**Permission Denied:**
- Set `use_sudo: true`
- Check user sudo privileges: `sudo -l`
- Add user to sudo group: `usermod -aG sudo username`

**Command Not Found:**
- Install required package
- Check PATH: `echo $PATH`
- Use full path to binary

**Operation Not Permitted:**
- Some operations require reboot
- Check SELinux/AppArmor policies
- May need to disable security modules temporarily

## 🔐 RESPONSIBILITY WARNING

With great power comes great responsibility.
This tool gives UNRESTRICTED system access.

- Can break the entire system
- Can delete all data
- Can expose system to attacks
- NO UNDO for most operations

**Use with EXTREME CAUTION! ⚠️**
