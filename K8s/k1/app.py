from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)
DATA_DIR = "/aiwin_PV_dir"           


@app.route('/start', methods=['GET'])

 

def test_ip_function():

    return "hello"


@app.route('/store-file', methods=['POST'])
def store_file():
    data = request.get_json()
    if not data or 'file' not in data or 'data' not in data:
        return jsonify({"file": None, "error": "Invalid JSON input."})

    file_path = os.path.join(DATA_DIR, data['file'])
    try:
        with open(file_path, 'w') as file:
            file.write(data['data'])
        return jsonify({"file": data['file'], "message": "Success."})
    except Exception as e:
        return jsonify({"file": data['file'], "error": "Error while storing the file to the storage."})

@app.route('/calculate', methods=['POST'])
def verification():
    data = request.get_json()
    if not data or 'file' not in data:
        return jsonify({"file": None, "error": "Invalid JSON input."})

    file_path = os.path.join(DATA_DIR, data['file'])
    if not os.path.exists(file_path):
        return jsonify({"file": data['file'], "error": "File not found."})

    return data_fetching(file_path, data.get('product'))

def data_fetching(file_path, product):
    url = "http://my-service-app2:80/calculate"  
    data = {"file": os.path.basename(file_path), "product": product}
    response = requests.post(url, json=data)
    return response.json()

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5001)
