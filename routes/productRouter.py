from fastapi import APIRouter, Response
from models.productModel import Product
from controllers.productController import create_product_controller, get_product_controller, update_product_controller, delete_product_controller, get_products_id_controller

ProductRouter = APIRouter(
    # means every route inside this router automatically starts with /products.
    prefix= '/products',
    tags= ['products']
    # This grps all api under group named products : Organized
)
# products = []
# id = 0

# Create Product
@ProductRouter.post('/postproducts')
def create_product(product: Product, response: Response):
    return create_product_controller(product, response)

# Get products
@ProductRouter.get('/getproducts')
def get_products(response: Response):
    return get_product_controller(response)

# Get product by ID
@ProductRouter.get('/getproduct/{productid}')
def get_products_id(productid: int, response: Response):
    return get_products_id_controller(productid, response)

# Delete Product
@ProductRouter.delete('/deleteproduct/{productid}')
def delete_product(productid: int, response: Response):
    return delete_product_controller(productid, response)

# Update Product
@ProductRouter.put('/updateproduct/{productid}')
def update_product(productid: int,updated_product: Product, response: Response):
    return update_product_controller(productid, updated_product, response)
#### All str for mongoDb id:int to id:str


