from flask import Flask
import webbrowser
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Simple Web Page</h1><p>This is a basic web page using Python and Flask.</p>"

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == '__main__':
    threading.Timer(1.25, open_browser).start()  # Waits a bit before opening
    app.run(debug=True)
