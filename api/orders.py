from fastapi import APIRouter, HTTPException
from models.order import Order

router = APIRouter()
orders_db = []

@router.post("/", response_model=Order)
def create_order(order: Order):
    orders_db.append(order)
    return order

@router.get("/", response_model=list[Order])
def list_orders(limit: int = 10, offset: int = 0):
    return orders_db[offset:offset + limit]

@router.get("/{order_id}", response_model=Order)
def get_order(order_id: int):
    if order_id < 1 or order_id > len(orders_db):
        raise HTTPException(status_code=404, detail="Order not found")
    return orders_db[order_id - 1]
