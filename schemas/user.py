from typing import List
from pydantic import BaseModel
from schemas.homework import HomeWork


class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    home_works: List[HomeWork] = []

    class Config:
        orm_mode = True