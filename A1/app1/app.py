from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    if not data or 'file' not in data:
        return jsonify({"file": None, "error": "Invalid JSON input."})

    file_name = data['file']
    file_path = os.path.join('/data', file_name)

    if not os.path.exists(file_path):
        return jsonify({"file": file_name, "error": "File not found."})

    product = data.get('product')
    response = forward_to_container_2(file_path, product)

    return response

def forward_to_container_2(file_path, product):
    container2_url = "http://app2:6002/calculate"
    data = {"file": os.path.basename(file_path), "product": product}
    response = requests.post(container2_url, json=data)
    return response.json()

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=6000)
