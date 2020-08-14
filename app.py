from flask import Flask
from flask import request
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
            "sender": req.get("name")
        }

        print("Done")
        return 'res'

    else:
        print("Not Done!")
        return make_response(jsonify({"message": "Request body must be JSON"}), 400)        
