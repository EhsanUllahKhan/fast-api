from sqlalchemy.orm import Session
from fastapi import HTTPException
from API.Models import found_item_model as models
from API.Schemas import found_item_schemas


def get_found_item(db: Session, found_item_id: int):
    return db.query(models.Found_Item).filter(models.Found_Item.foundItem_id == found_item_id).first()

def get_found_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Found_Item).offset(skip).limit(limit).all()


def create_found_item(db: Session, found_item_schemas: found_item_schemas.FoundItemCreate):
    _u = db.query(models.Lost_Item).filter(models.Lost_Item.lost_item_id == found_item_schemas.lost_item_id).one_or_none()
    if _u is None:
        raise HTTPException(status_code=404, detail="Not Found")

    _u.is_found = found_item_schemas.is_found
    db.add(_u)
    db.commit()
    db.refresh(_u)
    # return _u

    db_found_item = models.Found_Item(
    found_lattitude= found_item_schemas.found_lattitude,
    found_longitude= found_item_schemas.found_longitude,
    found_date=found_item_schemas.found_date,
    user_id= found_item_schemas.user_id,
    lost_item_id=found_item_schemas.lost_item_id,
    )
    db.add(db_found_item)
    db.commit()
    db.refresh(db_found_item)
    return db_found_item

