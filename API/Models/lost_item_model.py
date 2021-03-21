from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, Date
from sqlalchemy.orm import relationship


from pydantic import BaseModel

from ..database import Base


class Lost_Item(Base):
    __tablename__ = "lost_items"

    lost_item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=20))
    description=Column(String(length=50))
    lost_lattitude = Column(Float)
    lost_longitudee = Column(Float)
    lost_date = Column(Date)
    is_found=Column(Boolean)
    user_id = Column(Integer, ForeignKey("users.user_id"))

    found_items = relationship("Found_Item", backref="lost_items")
    item_pictures = relationship("Item_Picture", back_populates="lost_items")

    # users = relationship("User", back_populates="lost_items")
    # item_pictures = relationship("item_pictures", back_populates="lost_items")
    # found_items = relationship("Found_Item", back_populates="lost_items")
