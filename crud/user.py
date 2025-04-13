from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserBase

def create_user(user: UserBase, db: Session):
    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session):
    return db.query(User).all()

def get_user_by_id(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    return user

def delete_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    db.delete(user)
    db.commit()
    return user

def update_user(user_id: int, updated_data: UserBase, db: Session):
    # Pretraga korisnika u bazi na osnovu user_id
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        return None  # Ako korisnik ne postoji, vraćamo None

    # Ažuriramo podatke korisnika
    user.first_name = updated_data.first_name
    user.last_name = updated_data.last_name
    # Dodaj još polja ako je potrebno, kao što su email, password, itd.

    # Potvrda izmene u bazi
    db.commit()
    db.refresh(user)
    return user

