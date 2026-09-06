from flask import Flask, jsonify, request
from calculator import *
import re

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    message = "Hello"
    return jsonify(message)

@app.route("/secret", methods=["GET"])
def secret():
    secret = "123"
    return jsonify(secret)

@app.route("/calc", methods=["POST"])
def calculate():
    calc = Calculator()
    allowed_patterns = r"^[0-9+*/-]{1,10}$"
    
    data = request.get_json(silent=True)
    if not data or "expression" not in data:
        return jsonify({"error": "Error, missing input"}), 400
        
    expression = data["expression"]
    
    if re.match(allowed_patterns, expression):
        result = calc.calc(expression)
        return jsonify({"result": result})
    else:
        return jsonify({"error": "Error, invalid input or unsafe characters"}), 400

    

if __name__ == "__main__":
    app.run()