from fastapi import FastAPI
from api import products, orders  # Import your API routers here

app = FastAPI()

# Include your API routers here
app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])
