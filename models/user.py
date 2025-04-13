from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from core.database import Base

class User(Base):
    __tablename__ = "users"
    
    # id je primarni ključ, koristi Mapped i mapped_column
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    
    # Ostale kolone koje treba da budu mapirane
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)