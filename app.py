from flask import Flask
import json
from flask import request, jsonify, make_response
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Noushin Jooon, problem solved!'


@app.route('/about')
def about():
    return 'This is about Noushin'



@app.route('/json', methods=["POST"])
def json():

    if not request.json:
        return make_response(jsonify({
            "code": 400,
            "message": "Input should be a json"
        }), 400)
    try:
        body = request.json
    except:
        return make_response(jsonify({
            "code": 400,
            "message": "Failed to parse input json"
        }), 400)
    return make_response(jsonify({
            "code": 200,
            "sender": body,
            "message": "success"
        }), 200)
