#!/usr/bin/env python3
"""
Quick Start Script for LOVE HACKER Notification Tool
"""

import os
import subprocess
import sys

def check_installation():
    """Check if all required packages are installed"""
    try:
        import flask
        import requests
        print("✅ All Python packages are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        return False

def main():
    print("🚀 LOVE HACKER Notification Tool - Quick Start")
    print("=============================================")
    
    # Check installation
    if not check_installation():
        print("\n📥 Running setup...")
        os.system("chmod +x setup.sh")
        os.system("./setup.sh")
    
    # Start main tool
    print("\n🎯 Starting Notification Tool...")
    os.system("python main.py")

if __name__ == "__main__":
    main()
