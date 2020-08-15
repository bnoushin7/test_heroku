from flask import Flask
import json
from flask import request, jsonify, make_response
from intake import open_catalog

import pandas
import re
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Noushin Jooon, problem solved!'


@app.route('/about')
def about():
    return 'This is about Noushin'


@app.route('/all_data')
def all_data():

    catalog_name='https://raw.githubusercontent.com/kpegion/COLA-DATASETS-CATALOG/gh-pages/intake-catalogs/'
    cat = open_catalog(catalog_name+'master.yaml')
    result = []
    queue = []
    def my_recursive(catalog):
        for i in list(catalog):
            queue.append(i)

            while queue:
                level_size = len(queue)
                for _ in range(level_size):
                    current = queue.pop()
                    result.append(current)
                    subcat=open_catalog(catalog_name+current.lower()+'.yaml')


                    for j in list(subcat):
                        if j not in ('netcdf','example'):
                            queue.append(j)
        return result
    return my_recursive(cat)

@app.route('/json', methods=["POST"])
def json():

    if not request.json:
        return make_response(jsonify({
            "code": 400,
            "message": "Input should be a json"
        }), 400)
    try:
        body = request.json
        tagg = body['tag']
        print(tagg)
    except:
        return make_response(jsonify({
            "code": 400,
            "message": "Failed to parse input json"
        }), 400)
    return make_response(jsonify({
            "code": 200,
            "sender": body['tag'],
            "message": "success"
        }), 200)



@app.route('/data_per_tag', methods=["POST", "GET"])
def datasets_per_tag(tag):
    # df = pandas.read_excel('tags-datasets.xlsx')
    # my_list = df[lambda x: ~pandas.isnull(x[tag])][tag]
    # pattern = re.compile(r'\s+')
    # s = my_list.to_string(index=False).replace('\n',',')
    # return(print(pattern.sub(' ', s)))

    if request.method == 'POST':
        if not request.json:
            return make_response(jsonify({
                "code": 400,
                "message": "Input should be a json"
            }), 400)
        try:
            body = request.json
            tag = body['tag']
            print(tag)
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
