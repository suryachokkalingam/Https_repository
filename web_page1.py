from flask import Flask, request
import webbrowser
import threading
import time
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Simple Web Page</h1><p>This is a basic web page using Python and Flask.</p>"

@app.route('/shutdown', methods=['GET'])
def shutdown():
    """Endpoint to shut down the Flask server."""
    func = request.environ.get('werkzeug.server.shutdown')
    if func:
        func()  # Properly shuts down Flask
    return "Shutting down server..."

def open_browser():
    """Opens the browser automatically after 1.5 seconds."""
    time.sleep(1.5)
    webbrowser.open_new("http://127.0.0.1:5000/")

def stop_server():
    """Forcefully stops the server after 30 seconds."""
    time.sleep(30)
    try:
        requests.get("http://127.0.0.1:5000/shutdown")  # Calls shutdown endpoint
    except requests.exceptions.RequestException:
        pass  # Ignore errors in case the server is already down
    os._exit(0)  # Forcefully stop the process

if __name__ == '__main__':
    threading.Thread(target=open_browser, daemon=True).start()  # Open browser automatically
    threading.Thread(target=stop_server, daemon=True).start()  # Stop server after 30 sec
    app.run(debug=False, use_reloader=False)  # Run Flask server
