
from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
        {
            "name" : "My new store",
            "items" : [
                    {
                    "name" : "pen",
                    "price" : 10
                    }
            ]
        }
]

# GET
# POST

# POST sotre --->  /store/<name>
@app.route('/store', methods = ['POST'])
def create_store():
    request_data = request.get_json()
    new_store ={
                'name' : request_data['name'],
                'items' : []
            }
    stores.append(new_store)
    return jsonify(stores)
# GET store --->  /store/<name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    else:
        return jsonify({"message" : "Store not found"})



# GET stores --->  /store
@app.route('/store')
def get_all_stores():
    return jsonify({'stores' : stores})
# POST item ---> /store/<name>/item
# GET item ---> /store/<name>/item


app.run(port = 5000)
