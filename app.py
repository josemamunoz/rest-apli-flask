from flask import Flask, jsonify

app = Flask(__name__)

from products import products
from categories import categories

# ..................... Obtener todos los productos y categorias ....................................... 

@app.route('/')
def getProducts():
    return jsonify({"products": products, "categories": categories})

# ..................... Obtener un producto .................... ....................................... 

@app.route('/product/<string:product_name>')
def getProduct(product_name):

    product_found = [product for product in products if product['name'] == product_name]
    if (len(product_found) > 0 ):
        return jsonify({"product": product_found[0]})
    return jsonify({"message": "Product not found"})



if __name__== '__main__':
    app.run(debug=True)

