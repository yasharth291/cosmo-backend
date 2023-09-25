from fastapi import APIRouter, HTTPException
from models.user import User, UserAddress

router = APIRouter()

users_db = []

@router.post("/users/", response_model=User)
def create_user(user: User):
    users_db.append(user)
    return user

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    if user_id < 1 or user_id > len(users_db):
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id - 1]

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    if user_id < 1 or user_id > len(users_db):
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id - 1] = updated_user
    return updated_user

@router.post("/users/{user_id}/address", response_model=UserAddress)
def update_user_address(user_id: int, address: UserAddress):
    if user_id < 1 or user_id > len(users_db):
        raise HTTPException(status_code=404, detail="User not found")
    # Update the user's address (replace with your logic)
    users_db[user_id - 1].address = address
    return address