from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import os

app = Flask(__name__)


# Database connection details
db_host = 'db1.c5wo4emmyd5g.us-east-1.rds.amazonaws.com'
db_name = 'A1'
username = 'admin'
password = 'adminadmin'

#creating connection
def db_connection():
    try:
        connection = mysql.connector.connect(
            host=db_host,
            database=db_name,
            user=username,
            password=password
        )
        return connection
    except Error as e:
        app.logger.error(f"Database connection error: {e}")
        return None
#inserting value
def insertion(connection, query, values):
    try:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        return True
    except Error as e:
        app.logger.error(f"Failed to execute query: {e}")
        return False
#reading database
def retrieving(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        app.logger.error(f"Failed to execute read query: {e}")
        return None


@app.route('/store-products', methods=['POST'])
def store_products():
    data = request.get_json()
    products = data['products']
    connection = db_connection()
    
    if connection:
        for product in products:
            query = "INSERT INTO products (name, price, availability) VALUES (%s, %s, %s)"
            values = (product['name'], product['price'], product['availability'])
            
            if not insertion(connection, query, values):
                connection.close()
                return jsonify({"error": "An error occurred while storing products"}), 500
                
        connection.close()
        return jsonify({"message": "Success."}), 200
    else:
        return jsonify({"error": "Connection to the database failed. Check logs for more details."}), 500

@app.route('/list-products', methods=['GET'])
def list_products():
    connection = db_connection()
    if connection:
        products = retrieving(connection, "SELECT name, price, availability FROM products")
        connection.close()
        
        if products is not None:
            result = [{"name": name, "price": price, "availability": availability} for 
name, price, availability in products]
            return jsonify({"products": result}), 200
        else:
            return jsonify({"error": "An error occurred while retrieving products"}), 500
    else:
        return jsonify({"error": "Connection to the database failed. Check logs for more details."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=True)
