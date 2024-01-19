from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    file_name = data.get('file')
    product = data.get('product')

    if not file_name:
        return jsonify({"file": None, "error": "Invalid JSON input."})

    file_path = os.path.join('/data', file_name)

    if not os.path.exists(file_path):
        return jsonify({"file": file_name, "error": "File not found."})

    return calculate_sum(file_path, product)

def calculate_sum(file_path, product):
    try:
        with open(file_path, 'r') as dat_file:
            csv_reader = csv.DictReader(dat_file)
            sum = 0
            for row in csv_reader:
                if row['product'] == product:
                    sum += int(row['amount'])
            return jsonify({"file": os.path.basename(file_path), "sum": sum})
    except Exception as e:
        return jsonify({"file": os.path.basename(file_path), "error": "Input file not in CSV format."})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6002)
