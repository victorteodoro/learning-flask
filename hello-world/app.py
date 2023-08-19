from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h2>Hello, World!</h2>\n<p>This is your first Flask app 😉</p>"

if __name__ == "__main__":
    app.run(debug = True, port = '8080', host = '0.0.0.0')
