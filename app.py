from flask import Flask, request, jsonify
import products_dao
from connect import connect_sql
app = Flask(__name__)

connection = connect_sql()

@app.route('/get_items', methods=['GET'])
def get_items():
    response = products_dao.retrieve_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("opening")
    app.run(port=5000)