from flask import Flask
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

    if request.is_json:

        req = request.get_json()

        response_body = {
            "message": "JSON received!",
            "sender": req.get("message")
        }

        res = make_response(jsonify(response_body), 200)
        return res

    else:
        print("Not Done!")
        return '"message": "Request body must be JSON"}), 400'        
