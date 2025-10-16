"""
WSGI entry point for the Flask application.
This file allows Render to find the Flask app without path issues.
"""

from backend.app import app

if __name__ == "__main__":
    app.run()
