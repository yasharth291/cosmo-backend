from pymongo import MongoClient
from models.product import Product
from models.order import Order

# Initialize MongoDB client and database
client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce_db"]

# Define MongoDB collections
product_collection = db["products"]
order_collection = db["orders"]

# MongoDB related functions for products
def create_product(product: Product):
    # Insert the product into the MongoDB collection
    product_dict = product.dict()
    product_collection.insert_one(product_dict)

def list_products():
    # Retrieve products from the MongoDB collection
    products = list(product_collection.find())
    return [Product(**product) for product in products]

# MongoDB related functions for orders
def create_order(order: Order):
    # Insert the order into the MongoDB collection
    order_dict = order.dict()
    order_collection.insert_one(order_dict)

def list_orders():
    # Retrieve orders from the MongoDB collection
    orders = list(order_collection.find())
    return [Order(**order) for order in orders]

