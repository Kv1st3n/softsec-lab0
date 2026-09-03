from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    messeage = "Hello"
    return jsonify(messeage)

if __name__ == "__main__":
    app.run()