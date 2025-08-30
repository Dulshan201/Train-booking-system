#!/usr/bin/env python3
"""
Quick start script for the Train Booking Web Application
"""

import os
import sys
import webbrowser
import time
from threading import Timer

def open_browser():
    """Open the web browser after a short delay"""
    webbrowser.open('http://localhost:5000')

def main():
    print("🚂 Starting TrainBook Pro Web Application...")
    print("=" * 50)
    
    # Check if Flask is installed
    try:
        import flask
        print(f"✅ Flask {flask.__version__} detected")
    except ImportError:
        print("❌ Flask not found. Installing dependencies...")
        os.system(f"{sys.executable} -m pip install flask jinja2 werkzeug")
        
    # Start the application
    try:
        print("🌐 Starting web server on http://localhost:5000")
        print("📱 Opening browser in 3 seconds...")
        print("💡 Press Ctrl+C to stop the server")
        print("=" * 50)
        
        # Open browser after 3 seconds
        Timer(3.0, open_browser).start()
        
        # Import and run the Flask app
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)
        
    except KeyboardInterrupt:
        print("\n👋 TrainBook Pro stopped. Thank you!")
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        print("💡 Make sure all dependencies are installed correctly")

if __name__ == "__main__":
    main()
