from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return ("REV API")

app.run("192.168.122.44", 8080)
