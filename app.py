from flask import Flask, jsonify
config = Flask(__name__)

@config.route("/")
def main():
    return jsonify(
        {
            "response" : 200, 
            "message" : "deploy success!."
        }
    )
