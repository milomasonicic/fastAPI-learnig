from pydantic import BaseModel

# Koristićemo ovu šemu za unos korisničkih podataka
class UserBase(BaseModel):
    first_name: str
    last_name: str

# Ova šema će biti za odgovor, kada kreiraš korisnika
class UserResponse(UserBase):
    id: int
    first_name: str
    last_name: str

    class Config:
        from_attributes = True
