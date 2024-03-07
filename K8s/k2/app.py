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
        with open(file_path, mode='r', newline='') as dat_file:
            file_data = csv.DictReader(dat_file)
            total_sum = 0
            product_found = False
            for row in file_data:
                if row.get('product') == product:
                    try:
                        total_sum += int(row.get('amount', 0))
                        product_found = True
                    except ValueError:
                        # Handle the case where 'amount' is not an integer
                        return jsonify({"file": os.path.basename(file_path), "error": "Invalid amount value."})
            if not product_found:
                # Product was not found in the file
                return jsonify({"file": os.path.basename(file_path), "error": f"Product '{product}' not found."})
            return jsonify({"file": os.path.basename(file_path), "sum": total_sum})
    except Exception as e:
        # This captures any other exception, including issues opening the file
        return jsonify({"file": os.path.basename(file_path), "error": f"Error processing file: {str(e)}"})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=6002)
