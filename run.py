#!/usr/bin/env python3
"""
Simple script to run the Finance Management App
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from app import app


if __name__ == '__main__':
    print("🚀 Starting Finance Management App...")
    print("💡 Open your browser to: http://127.0.0.1:5000")
    print("🛑 Press Ctrl+C to stop the server")
    app.run(debug=True, host='127.0.0.1', port=5000)
