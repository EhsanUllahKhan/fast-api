from sqlalchemy.orm import Session

from API.Models import lost_item_model as models
from API.Schemas import lost_item_schemas


def get_lost_item(db: Session, lost_item_id: int):
    return db.query(models.Lost_Item).filter(models.Lost_Item.lost_item_id == lost_item_id).first()

def get_lost_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Lost_Item).filter(models.Lost_Item.is_found == False).offset(skip).limit(limit).all()


def create_lost_item(db: Session, lost_item_schemas: lost_item_schemas.LostItemCreate):
    db_lost_item = models.Lost_Item(
        name= lost_item_schemas.name,
        description= lost_item_schemas.description,
        lost_lattitude= lost_item_schemas.lost_lattitude,
        lost_longitude= lost_item_schemas.lost_longitude,
        lost_date=lost_item_schemas.lost_date,
        is_found= lost_item_schemas.is_found,
        user_id= lost_item_schemas.user_id,
        picture=lost_item_schemas.picture
    )
    db.add(db_lost_item)
    db.commit()
    db.refresh(db_lost_item)
    return db_lost_item

