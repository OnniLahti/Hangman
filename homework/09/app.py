from flask import Flask, jsonify, request, make_response
import json

app = Flask(__name__)

id = 2
customers = [{"id": 1, "name": "jack"}, {"id": 2, "name": "hannah"}]

@app.route('/customers')
def get_customers():
    return jsonify(customers)

@app.route('/customers', methods=['POST'])
def add_customer():
    customer = json.loads(request.data)
    # https://www.programiz.com/python-programming/global-keyword
    global id
    id = id + 1
    customer["id"] = id
    customers.append(customer)
    return  make_response(jsonify(customer), 201)

@app.route('/customers/<int:the_id>', methods=['DELETE'])
def delete_customer(the_id):
    index_to_be_deleted = -1
    for i in range(0, len(customers)):
        if(customers[i]["id"] == the_id):
            index_to_be_deleted = i
    if(index_to_be_deleted != -1):
        customers.pop(index_to_be_deleted)
        return make_response("", 204)
    else:
        return make_response("", 404)
if __name__ == "__main__":
    app.run(debug=True)
