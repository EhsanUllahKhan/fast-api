from pydantic import BaseModel
from pydantic.schema import date

class FoundItemBase(BaseModel):
    # found_items_id :int
    # name : str
    found_lattitude:float
    found_longitude: float
    found_date : date
    user_id : int
    lost_item_id: int

class FoundItemCreate(FoundItemBase):
    # found_items_id :int
    # name : str
    found_lattitude:float
    found_longitude: float
    found_date : date
    user_id : int
    lost_item_id: int

class FoundItem(FoundItemBase):
    foundItem_id :int
    # name : str
    found_lattitude:float
    found_longitude: float
    found_date : date
    user_id : int
    lost_item_id: int

    class Config:
        orm_mode = True
