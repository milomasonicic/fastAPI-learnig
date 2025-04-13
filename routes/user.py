from models.user import User
from schemas.user import UserBase, UserResponse
from core.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from typing import List

router = APIRouter()

@router.post("/createUser/", response_model=UserResponse)
async def create_user(user: UserBase, db: Session = Depends(get_db)):
    new_user = User(
            first_name=user.first_name,
            last_name=user.last_name,
        )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user   


@router.get("/getAllUsers", response_model=List[UserResponse])
async def get_all_users(db: Session = Depends(get_db)):
    # Preuzimanje svih korisnika iz baze
    users = db.query(User).all()
    return users     


