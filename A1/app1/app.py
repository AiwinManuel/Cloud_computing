from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
#verfiying file existance
def verification():
    data = request.get_json()
    name = data['file']
    path = os.path.join('/data', name)

    if not data or 'file' not in data:
        return jsonify({"file": None,"error": "Invalid JSON input."})

    if not os.path.exists(path):
        return jsonify({"file": name,"error": "File not found."})

    product = data.get('product')
    response = data_fetching(path, product)

    return response
#forwarding to 2nd container
def data_fetching(file_path, product):
    url = "http://app2:6002/calculate"
    data = {"file": os.path.basename(file_path), "product": product}
    response = requests.post(url, json=data)
    return response.json()

