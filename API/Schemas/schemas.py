from typing import List, Optional

from pydantic import BaseModel
from pydantic.schema import date

#
# class LostItemBase(BaseModel):
#     lost_item_id: int
#     name: str
#     description : str
#     lost_lattitude: float
#     lost_longitudee: float
#     lost_date: date
#     is_found: bool
#     user_id: int
#
#
# class LostItemCreate(LostItemBase):
#     lost_item_id :int
#     name : str
#     description : str
#     lost_lattitude:float
#     lost_longitudee: float
#     lost_date : date
#     is_found : bool
#     user_id : int
#
#
# class LostItem(LostItemBase):
#     lost_item_id :int
#     name : str
#     description : str
#     lost_lattitude:float
#     lost_longitudee: float
#     lost_date : date
#     is_found : bool
#     user_id : int
#
#
#     class Config:
#         orm_mode = True
# class FoundItemBase(BaseModel):
#     found_items_id :int
#     name : str
#
#     found_lattitude:float
#     found_longitudee: float
#     found_date : date
#
#     user_id : int
#
#
#
# class FoundItemCreate(FoundItemBase):
#     found_items_id :int
#     name : str
#
#     found_lattitude:float
#     found_longitudee: float
#     found_date : date
#
#     user_id : int
#
#
#
# class FoundItem(FoundItemBase):
#     found_items_id :int
#     name : str
#
#     found_lattitude:float
#     found_longitudee: float
#     found_date : date
#
#     user_id : int
#
#
#     class Config:
#         orm_mode = True

# from ..Models.lost_item_model import LostItem
from API.Schemas.lost_item_schemas import LostItem


class UserBase(BaseModel):

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
