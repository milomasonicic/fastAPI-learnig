from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException
from models.user import User
from schemas.user import UserBase, UserResponse
from core.database import get_db
from crud.user import create_user, get_all_users, get_user_by_id, delete_user, update_user

router = APIRouter()

@router.post("/createUser/", response_model=UserResponse)
async def create_user_route(user: UserBase, db: Session = Depends(get_db)):
    return create_user(user, db)

@router.get("/getAllUsers/", response_model=List[UserResponse])
async def get_all_users_route(db: Session = Depends(get_db)):
    return get_all_users(db)


@router.get("/getUser/{user_id}", response_model=UserResponse)
async def get_user_by_id_route(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/deleteUser/{user_id}", response_model=UserResponse)
async def delete_user_route(user_id:int, db: Session = Depends(get_db)):
    user = delete_user(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
        
@router.put("/updateUser/{user_id}", response_model=UserResponse)
async def update_user_route(user_id: int, user_data: UserBase, db: Session = Depends(get_db)):
    updated_user = update_user(user_id, user_data, db)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

