from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    name: str
    price: float
    available_quantity: int