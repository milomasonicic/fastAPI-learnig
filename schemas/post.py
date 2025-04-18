from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    user_id: int  # ID autora

class PostOut(PostBase):
    id: int
    created_at: datetime
    user_id: int

    class Config:
        orm_mode = True
