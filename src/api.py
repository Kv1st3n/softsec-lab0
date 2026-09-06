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
    allowed_patterns = r"^[0-9+*/-]{2,10}$"
    
    expression = request.get_data(as_text=True)
    
    if not expression:
        return "Error, missing input", 400
        
    expression = expression["expression"]
    
    if re.match(allowed_patterns, expression):
        result = calc.calc(expression)
        return jsonify({"result": result})
    else:
        return jsonify({"error": "Error, invalid input or unsafe characters"}), 400

    

if __name__ == "__main__":
    app.run()