from typing import List, Optional
from pydantic import BaseModel
from API.Schemas.lost_item_schemas import LostItem
from API.Schemas.found_item_schemas import FoundItem

class UserBase(BaseModel):
    user_id: int
    email:str
    password :str
    # lost_items: List[LostItem] = []
    # found_items: List[FoundItem] = []
#
# class UserBase(BaseModel):
#     email: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    password: str
    email: str

class User(UserBase):
    user_id: int
    lost_items: List[LostItem] = []
    found_items: List[FoundItem] = []

    class Config:
        orm_mode = True
