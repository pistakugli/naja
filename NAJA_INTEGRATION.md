# NAJA Integration

This fork integrates custom tools and Claude AI skills into Agent Zero.

## What's Added

### 1. Custom NAJA Tools (`instruments/custom/naja-tools/`)
- `naja-ml` - Kaggle/Colab ML integration
- `naja-tensor` - Tensor Protocol v4.1 for Claude communication
- `naja-kali` - Kali Linux security tools wrapper
- `naja-all` - Combined tool launcher
- `naja-admin` - Admin utilities
- `agent-zero*` - Various Agent Zero launchers

### 2. Claude Skills (`claude_skills/`)
- 16 Claude AI skills (docx, pdf, pptx, xlsx, etc.)
- Full skill documentation in each folder

### 3. Main Launcher
```bash
./naja-integrated
```

## Quick Start
```bash
# Clone repo
git clone https://github.com/pistakugli/naja.git
cd naja

# Run integrated system
chmod +x naja-integrated
./naja-integrated
```

## Architecture
- Base: Agent Zero framework
- Tools: 15 custom naja tools
- Skills: 16 Claude skills
- Integration: Single unified launcher
