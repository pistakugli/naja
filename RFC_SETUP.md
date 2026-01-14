# RFC Configuration - NAJA Setup

## Quick Setup (Za Stevana)

### 1. RFC Password već setovan
```bash
# U .env fajlu (lokalno):
RFC_PASSWORD=22327
```

### 2. Development Instance Setup

**Opcija A: Docker (Preporučeno)**
```bash
docker run -d \
  --name naja-dev \
  -p 55080:80 \
  -e RFC_PASSWORD=22327 \
  agent0ai/agent-zero-base:latest
```

**Opcija B: Lokalni folder**
```bash
# Drugi folder za development
mkdir -p /media/pista/agent/naja-dev
cd /media/pista/agent/naja-dev

# Clone ili copy NAJA
git clone https://github.com/pistakugli/naja.git .

# Setup .env
echo "RFC_PASSWORD=22327" >> .env
echo "PORT=55080" >> .env

# Install
pip install -r requirements.txt

# Run
python run_ui.py
```

### 3. Production Settings

Idi na: http://localhost:50001/settings → **Developer** tab

Set:
```
RFC URL: localhost
RFC Port HTTP: 55080
RFC Port SSH: 55022
```

Sačuvaj settings.

### 4. Test RFC

```bash
cd /media/pista/agent/naja

python3 << 'PYEOF'
import asyncio
from python.helpers import rfc

async def test():
    try:
        result = await rfc.call_rfc(
            url="http://localhost:55080/rfc",
            password="22327",
            module="os",
            function_name="getcwd",
            args=[],
            kwargs={}
        )
        print(f"✅ RFC WORKS! Dev instance dir: {result}")
    except Exception as e:
        print(f"❌ RFC FAILED: {e}")

asyncio.run(test())
PYEOF
```

Expected:
```
✅ RFC WORKS! Dev instance dir: /a0
```

## Šta RFC radi?

```
Production (Port 50001)          Development (Port 55080)
┌─────────────────────┐         ┌─────────────────────┐
│ NAJA Main Instance  │         │  NAJA Dev Instance  │
│                     │         │                     │
│ Job Loop: Running   │──RFC──>│  Job Loop: Paused   │
│ Code: Native        │ calls  │  Code: Executed     │
│ Debug: VS Code      │ secure │  Env: Isolated      │
└─────────────────────┘         └─────────────────────┘
```

**Benefit:**
- Debuguješ kod u VS Code (production)
- Izvršavanje se dešava u izolovanom okruženju (development)
- Job loop radi samo jednom (production poziva dev preko RFC da pauzira)

## Sigurnost

⚠️ **NIKAD NE PUSH-UJ .env NA GITHUB!**

```bash
# .env je u .gitignore ✅
**/.env
```

Password "22327" je samo za **lokalni setup između tvoje dve instance**.

Za remote development preko interneta koristi **dugačak secure password**:
```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

## Ako NE koristiš development instancu

Samo ignoriši warning:
```
Error: Failed to pause job loop by development instance: No RFC password
```

NAJA će raditi normalno. RFC je **OPCIONI** feature.

## Status

✅ RFC_PASSWORD = 22327 (lokalno u .env)
✅ .env.example push-ovan na GitHub (sa placeholder)
✅ .gitignore sprečava push .env fajla
✅ mcp_server.py fixovan za fastmcp 2.3.4
✅ requirements.txt updejovan

---
Generated: 2026-01-14
