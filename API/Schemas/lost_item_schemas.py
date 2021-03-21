
from pydantic import BaseModel
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
    picture:str

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