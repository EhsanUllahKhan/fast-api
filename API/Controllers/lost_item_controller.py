from sqlalchemy.orm import Session
from fastapi import HTTPException
from API.Models import lost_item_model as models
from API.Schemas import lost_item_schemas


def get_lost_item(db: Session, lost_item_id: int):
    return db.query(models.Lost_Item).filter(models.Lost_Item.lost_item_id == lost_item_id).first()

def get_lost_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Lost_Item).filter(models.Lost_Item.is_found == False).offset(skip).limit(limit).all()

def get_lost_items_by_location(db: Session, lost_lattitude: float, lost_longitude: float):
    return db.query(models.Lost_Item).filter(
        models.Lost_Item.lost_lattitude == lost_lattitude,
        models.Lost_Item.lost_longitude == lost_longitude
    ).all()

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

def update_lost_item(db: Session, lost_item_id: int, lost_item_schemas: lost_item_schemas.LostItemUpdate):
    update = db.query(models.Lost_Item).filter(models.Lost_Item.lost_item_id == lost_item_id).first()
    print("\n\nlost item schemas are \n\n", update)
    if update:
        query = models.Lost_Item.update().where(
            models.Lost_Item.lost_item_id == lost_item_id,
            models.Lost_Item.user_id == lost_item_schemas.user_id
        ).values(
            name=lost_item_schemas.name,
            description=lost_item_schemas.description,
            lost_lattitude=lost_item_schemas.lost_lattitude,
            lost_longitude=lost_item_schemas.lost_longitude,
            lost_date=lost_item_schemas.lost_date,
            is_found=lost_item_schemas.is_found,
            user_id=lost_item_schemas.user_id,
            picture=lost_item_schemas.picture
        )
        db.execute(query)
        db.commit()
        db.refresh(update)
        return update
    raise HTTPException(status_code=404, detail="Not Found")
    return update

def delete_lost_item(db: Session, lost_item_id: float):
    delete = db.query(models.Lost_Item).filter(models.Lost_Item.lost_item_id == lost_item_id).first()
    if delete is None:
        raise HTTPException(status_code=404, detail="Not Found")
    db.delete(delete)
    db.commit()
    return {"lost_item_id" : lost_item_id, "message": 'Success'}
