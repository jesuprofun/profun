from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
        {
            'name' : 'My Wonderful Store',
            'items' : [
                    {
                    'name' : 'pencil',
                    'price' : 5.00
                    }
            ]
        }
]
# Get
# Post

# POST store  ---> /store/<name> method: POST
# GET store   ---> /store/<name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message' : 'Store not found'})
# GET stores  ---> /store
@app.route('/store')
def get_all_stores():
    return jsonify({'stores' : stores})
# POST items  ---> /store/<name>/item method : POST
# GET Items   ---> /store/<name>/item
# @app.route('/store/<string.name>/item')
# def get_all_items(name):


app.run (port = 5000)
