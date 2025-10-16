"""
Main application entry point for Render deployment.
This file imports the Flask app from the backend directory.
"""

from backend.app import app

if __name__ == "__main__":
    import os
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
