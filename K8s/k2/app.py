from flask import Flask, request, jsonify
import os

app = Flask(__name__)
DATA_DIR = "/aiwin_PV_dir/"

@app.route('/calculate', methods=['POST'])
def get_data():
    try:
        request_data = request.get_json()

        filename = request_data.get("file") if request_data else None
        product_name = request_data.get("product") if request_data else None

        if filename is None or product_name is None:
            return jsonify({'file': filename, 'error': 'Invalid JSON input.'}), 400    

        file_path = os.path.join(DATA_DIR, filename)
        try:
            with open(file_path, 'r') as file:
                lines = file.read().split('\n')
                header = [item.strip() for item in lines[0].split(',')]

                if "product" not in header or "amount" not in header:
                    return jsonify({'file': filename, 'error': 'Input file not in CSV format.'}), 400

                product_index = header.index("product")
                amount_index = header.index("amount")

                total_sum = 0
                for line in lines[1:]:
                    data = [item.strip() for item in line.split(',')]
                    if data and data[product_index] == product_name:  
                        try:
                            total_sum += int(data[amount_index])
                        except ValueError:
                            return jsonify({'file': filename, 'error': 'Invalid amount value in CSV.'}), 400

                return jsonify({'file': filename, 'sum': total_sum}), 200

        except FileNotFoundError:
            return jsonify({'file': filename, 'error': 'File not found.'}), 404
        except Exception as e:
            return jsonify({'file': filename, 'error': 'Input file not in CSV format.'}), 400

    except Exception as e:
        return jsonify({'file': None, 'error': 'Invalid JSON input.'}), 400

    
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=6002)
