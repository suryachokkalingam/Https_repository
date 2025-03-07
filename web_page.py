from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Web App</h1><p>This is the homepage.</p>"

@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is a simple Python web application using Flask.</p>"

if __name__ == '__main__':
    app.run(debug=True)
