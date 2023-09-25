from fastapi import APIRouter, HTTPException
from models.product import Product

router = APIRouter()

# Dummy products data
products_db = []

@router.post("/", response_model=Product)
def create_product(product: Product):
    products_db.append(product)
    return product

@router.get("/", response_model=list[Product])
def list_products():
    return products_db

# Define other product-related endpoints here
