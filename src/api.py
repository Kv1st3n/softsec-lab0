from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    messeage = "Hello"
    return jsonify(messeage)

@app.route("/secret", methods=["GET"])
def secret():
    secret = "123"
    return jsonify(secret)

if __name__ == "__main__":
    app.run()