from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, Date
from sqlalchemy.orm import relationship

from pydantic import BaseModel

from ..database import Base


class Item_Picture(Base):
    __tablename__ = "item_pictures"

    pictures_id = Column(Integer, primary_key=True, index=True)
    lost_item_id = Column(Integer, ForeignKey("lost_items.lost_item_id"))

    item_pictures = relationship("item_pictures", back_populates="lost_items")
    # found_items = relationship("Lost_item", back_populates="found_items")
