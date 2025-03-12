from flask import Flask, request
import webbrowser
import threading
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Simple Web Page</h1><p>This is a basic web page using Python and Flask.</p>"

def open_browser():
    """Opens the web browser after Flask starts"""
    webbrowser.open_new("http://127.0.0.1:5000/")

def stop_flask():
    time.sleep(30)
    func = request.environ.get('werkzeug.server.shutdown')
    if func:
        func()

if __name__ == '__main__':
    threading.Timer(1.5, open_browser).start()  # Open browser after 1.5 sec
    threading.Thread(target=stop_flask).start()
    app.run(debug=True)
