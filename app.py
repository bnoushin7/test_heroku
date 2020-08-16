from flask import Flask, request, jsonify, make_response
import pandas
from intake import open_catalog
import re
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/tag_based", methods=["POST"])
def datasets_per_tag():
	res = ""
	
	if not request.json:
		return make_response(jsonify({
            "code": 400,
            "message": "Input should be a json"
		}), 400)
	try:
		body = request.json
		tag = body['tag']		
		df = pandas.read_excel('tags-datasets.xlsx')		
		my_list = df[lambda x: ~pandas.isnull(x[tag])][tag]		
		pattern = re.compile(r'\s+')
		s = my_list.to_string(index=False).replace('\n',',')
		#return(print(pattern.sub(' ', s)))
		res = pattern.sub(' ', s)
	except Exception as inst:
		print(res)
		return make_response(jsonify({
            "code": 400,
            "message": "Failed to parse input json"
		}), 400)
	return make_response(jsonify({
            "code": 200,
            "result": res,
            "message": "success"
		}), 200)

		
@app.route('/all_data')
def all_data():
	catalog_name='https://raw.githubusercontent.com/kpegion/COLA-DATASETS-CATALOG/gh-pages/intake-catalogs/'
	cat = open_catalog(catalog_name+'master.yaml')
	result = []
	queue = []
	new_name = ""
	def my_recursive(catalog):
		for i in list(catalog):
			queue.append(i)

			while queue:
				level_size = len(queue)
				for _ in range(level_size):
					current = queue.pop()
					result.append(current)
					new_name = catalog_name+current.lower()+'.yaml'
					subcat=open_catalog(new_name)
					for j in list(subcat):
						if j not in ('netcdf','example'):
							queue.append(j)
		return jsonify(result)
		print("66666666666666666666666")
	return(my_recursive(cat))


if __name__ == "__main__":
    app.config['JSON_AS_ASCII'] = False
    app.run()
