from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)
@app.route('/calculate', methods=['POST'])
def get_data():
    data = request.get_json()
    # fetching file name
    name = data.get('file')
    product = data.get('product')
    path = os.path.join('/data', name)

    if not name:
        return jsonify({"file": None, "error": "Invalid JSON input."})
    
    if not os.path.exists(path):
        return jsonify({"file": name, "error": "File not found."})

    return sum(path, product)
#Calculating sum
def sum(file_path, product):
    try:
        with open(file_path, 'r') as dat_file:
            file_data = csv.DictReader(dat_file)
            sum = 0
            for row in file_data:
                if row['product'] == product:
                    sum += int(row['amount'])
            return jsonify({"file": os.path.basename(file_path), "sum": sum})
    except Exception as e:
        return jsonify({"file": os.path.basename(file_path), "error": "Input file not in CSV format."})
