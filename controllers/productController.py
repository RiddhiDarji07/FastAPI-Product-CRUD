from fastapi import APIRouter, Response
from models.productModel import Product
from bson import ObjectId

products = []
id = 0

def create_product_controller(product: Product, response: Response):
    global id
    try:
        id += 1
        product.id = id
        products.append(product)
        response.status_code = 201
        return {'isSuccess':True, 'message' : 'Product Created Successfully', 'product': product}
    except Exception as e:
        print(e)
        response.status_code = 500
        return{'isSuccess' : False, 'message' : str(e)}


def get_products_id_controller(productid: int, response: Response):
    try:
        response.status_code = 200
        for product in products:
            if product.id == productid:
                return {'isSuccess': True, 'product': product}

        response.status_code = 404
        return {'isSuccess':False, 'message' : 'Product not found'}
    except Exception as e:
        print(e)
        response.status_code = 500
        return{'isSuccess' : False, 'message' : str(e)}


def get_product_controller(response: Response):
    try:
        response.status_code = 200
        return {'isSuccess':True, 'message' : 'Product Display Successfully', 'products': products}
    except Exception as e:
        response.status_code = 500
        return{'isSuccess' : False, 'message' : str(e)}


def delete_product_controller(productid: int, response: Response):
    try:
        response.status_code = 200
        for product in products:
            if product.id == productid:
                products.remove(product)
                return {'isSuccess': True, 'message': 'Product Deleted Successfully', 'product': product}
        response.status_code = 404
        return {'isSuccess':False, 'message' : 'Product not found'}
    
    except Exception as e:
        response.status_code = 500

        return {'isSuccess': False, 'message': str(e)}

def update_product_controller(productid: int,updated_product: Product, response: Response):
    try:
        response.status_code = 200
        for product in products:
            if product.id == productid:
                product.name = updated_product.name
                product.price = updated_product.price
                product.description = updated_product.description

                return {'isSuccess': True, 'message': 'Product Updated Successfully', 'product': product}

        response.status_code = 404
        return {'isSuccess': False, 'message': 'Product not found'}

    except Exception as e:
        response.status_code = 500
        return {'isSuccess': False, 'message': str(e)}

