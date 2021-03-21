from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, Date
from sqlalchemy.orm import relationship


from pydantic import BaseModel

from ..database import Base


class Found_Item(Base):
    __tablename__ = "found_items"
    foundItem_id = Column(Integer,primary_key=True, index=True)
    # name = Column(String(length=20))
    found_lattitude = Column(Float)
    found_longitude = Column(Float)
    found_date = Column(Date)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    lost_item_id=Column(Integer, ForeignKey("lost_items.lost_item_id"))
    users = relationship("User", back_populates="found_items")

    # lost_items = relationship("Lost_Item", back_populates="found_items")
