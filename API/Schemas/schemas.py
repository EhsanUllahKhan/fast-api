from typing import List, Optional
from pydantic import BaseModel
from API.Schemas.lost_item_schemas import LostItem

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

class User(UserBase):
    user_id: int
    lost_items: List[LostItem] = []
    # found_items: List[FoundItem] = []

    class Config:
        orm_mode = True
