from flask import Flask, jsonify, request
from db import GroceryDB


app = Flask(__name__)
db = GroceryDB()


# view all grocery
@app.route('/grocery')
def all_grocery():
    """Get all grocery"""
    groceries = db.all()

    return jsonify(groceries)


# view add grocery
@app.route('/grocery/add')
def add_grocery():
    """Add a grocery"""
    if request.method == 'POST':
    
        body = request.get_json()
        
        db.add(body)

        return jsonify({'message': 'succefully added.'})

    else:
        return jsonify({'message': 'method not allowed.'}), 404


# view all grocery by type
@app.route('/grocery/type/<type>')
def all_grocery_by_type(type):
    """Get all grocery by type"""
    
    groceries = db.get_by_type(type=type)

    return jsonify(groceries)


# view all grocery by name
@app.route('/grocery/name/<name>')
def all_grocery_by_name(name):
    """Get all grocery by name"""
    pass


# view all grocery by price
@app.route('/grocery/price/<float:price>')
def all_grocery_by_price(price):
    """Get all grocery by price"""
    pass



if __name__ == '__main__':
    app.run(debug=True)