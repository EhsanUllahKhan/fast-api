from typing import List, Optional

from pydantic import BaseModel
from pydantic.schema import date


class LostItemBase(BaseModel):
    lost_item_id: int
    name: str
    description : str
    lost_lattitude: float
    lost_longitudee: float
    lost_date: date
    is_found: bool
    user_id: int


class LostItemCreate(LostItemBase):
    lost_item_id :int
    name : str
    description : str
    lost_lattitude:float
    lost_longitudee: float
    lost_date : date
    is_found : bool
    user_id : int


class LostItem(LostItemBase):
    lost_item_id :int
    name : str
    description : str
    lost_lattitude:float
    lost_longitudee: float
    lost_date : date
    is_found : bool
    user_id : int


    class Config:
        orm_mode = True
class FoundItemBase(BaseModel):
    found_items_id :int
    name : str

    found_lattitude:float
    found_longitudee: float
    found_date : date

    user_id : int



class FoundItemCreate(FoundItemBase):
    found_items_id :int
    name : str

    found_lattitude:float
    found_longitudee: float
    found_date : date

    user_id : int



class FoundItem(FoundItemBase):
    found_items_id :int
    name : str

    found_lattitude:float
    found_longitudee: float
    found_date : date

    user_id : int


    class Config:
        orm_mode = True


class UserBase(BaseModel):
    user_id :int
    email:str
    password :str


class UserCreate(UserBase):
    password: str



class User(UserBase):

    id: int

    is_active: bool

    lost_items: List[LostItem] = []
    found_items: List[FoundItem] = []


    class Config:
        orm_mode = True
