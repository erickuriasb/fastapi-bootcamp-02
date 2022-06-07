from typing import Optional
from pydantic import BaseModel

class HomeWorkBase(BaseModel):
    title: str
    description: str

class HomeWorkCreate(HomeWorkBase):
    ower_id: int

class HomeWork(HomeWorkBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True