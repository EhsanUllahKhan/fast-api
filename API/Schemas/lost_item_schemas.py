
from pydantic import BaseModel
from typing import Optional
from pydantic.schema import date

class LostItemBase(BaseModel):
    # lost_item_id: int
    name: str
    description : str
    lost_lattitude: float
    lost_longitude: float
    lost_date: date
    is_found: bool
    user_id: int
    # picture:str

class LostItemCreate(LostItemBase):
    # lost_item_id :int
    name : str
    description : str
    lost_lattitude:float
    lost_longitude: float
    lost_date : date
    is_found : bool
    user_id : int
    picture:str

class LostItemUpdate(LostItemBase):
    # lost_item_id: int
    name : str
    description : str
    lost_lattitude:float
    lost_longitude: float
    lost_date : date
    is_found : bool
    picture:str

class LostItemSearchByLocation(BaseModel):
    lost_lattitude:float
    lost_longitude: float

class LostItemDelete(BaseModel):
    lost_item_id :int

class LostItem(LostItemBase):
    lost_item_id :int
    name : str
    description : str
    lost_lattitude:float
    lost_longitude: float
    lost_date : date
    is_found : bool
    user_id : int
    picture:str

    class Config:
        orm_mode = True