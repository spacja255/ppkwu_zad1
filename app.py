from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "REV API"

@app.route("/rev/<text>")
def rev(text):
    reversed_text = text[::-1]
    return reversed_text

app.run("localhost", 8080)
