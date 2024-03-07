from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)
DATA_DIR = "/aiwin_PV_dir/"  

@app.route('/calculate', methods=['POST'])
def get_data():
    data = request.get_json()
    if not data or 'file' not in data:
        return jsonify({"file": None, "error": "Invalid JSON input."})

    file_path = os.path.join(DATA_DIR, data['file'])
    if not os.path.exists(file_path):
        return jsonify({"file": data['file'], "error": "File not found."})

    return calculate_sum(file_path, data.get('product'))

def calculate_sum(file_path, product):
    try:
        with open(file_path, 'r') as dat_file:
            file_data = csv.DictReader(dat_file)
            total_sum = 0
            for row in file_data:
                if row['product'] == product:
                    total_sum += int(row['amount'])
            return jsonify({"file": os.path.basename(file_path), "sum": total_sum})
    except Exception as e:
        return jsonify({"file": os.path.basename(file_path), "error": "Input file not in CSV format."})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=6002)
