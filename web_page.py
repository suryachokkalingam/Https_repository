from flask import Flask
import webbrowser
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Simple Web Page</h1><p>This is a basic web page using Python and Flask.</p>"

def run_flask():
    app.run(debug=True, use_reloader=False)  # Prevent Flask from restarting twice

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()  # Run Flask in a separate thread
    threading.Timer(1.25, open_browser).start()  # Open browser after a short delay
    input("Press Enter to exit...\n")  # Keeps the script running until manually closed
