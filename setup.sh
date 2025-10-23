#!/data/data/com.termux/files/usr/bin/bash

echo ""
echo "╔═══════════════════════════════════════════╗"
echo "║           LOVE ❤ HACKER PRESENTS         ║"
echo "║        NOTIFICATION TOOL SETUP           ║"
echo "║              EDUCATIONAL ONLY             ║"
echo "╚═══════════════════════════════════════════╝"
echo ""

echo "[+] Updating packages..."
pkg update -y && pkg upgrade -y

echo "[+] Installing dependencies..."
pkg install python git wget -y

echo "[+] Installing Python packages..."
pip install flask requests

echo "[+] Downloading cloudflared..."
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64 -O cloudflared

echo "[+] Setting up cloudflared..."
chmod +x cloudflared
mv cloudflared $PREFIX/bin/

echo "[+] Creating icons folder..."
mkdir -p icons

echo ""
echo "[✅] Setup completed successfully!"
echo "[🚀] Now run: python main.py"
echo "[📱] Make sure to run: cloudflared tunnel login"
echo ""
