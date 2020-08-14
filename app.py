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
    req = request.get_json()

    print(req)

    return "Thanks!", 200


