from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Noushin Jooon, problem solved!'


@app.route('/about')
def about():
    return 'This is about Noushin'
