from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


from pydantic import BaseModel

from ..database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String(length=20), unique=True, index=True)
    password = Column(String(length=20))

    lost_items = relationship("Lost_Item", backref="users")
    found_items = relationship("Found_Item", backref="users")
    # lost_items = relationship("Lost_Item", back_populates="users")
    # found_items = relationship("Found_Item", back_populates="users")
