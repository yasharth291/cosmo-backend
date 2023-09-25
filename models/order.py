from pydantic import BaseModel
from typing import List
from models.user import UserAddress

class OrderItem(BaseModel):
    product_id: str
    bought_quantity: int
    total_amount: float

class Order(BaseModel):
    timestamp: str  # Use a proper datetime field
    items: List[OrderItem]
    user_address: UserAddress
