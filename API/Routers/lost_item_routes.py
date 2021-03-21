from fastapi import APIRouter
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from API.Schemas import lost_item_schemas as schemas
from API.Controllers import  lost_item_controller as crud
from ..database import SessionLocal, engine

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router_lost_items = APIRouter(
    prefix="/lost_items",
    tags=["Lost Items"]
)

@router_lost_items.post("/", response_model=schemas.LostItem)
def create_lostItem(lostItem: schemas.LostItemCreate, db: Session = Depends(get_db)):
    return crud.create_lost_item(db=db, lost_item_schemas=lostItem)

@router_lost_items.put("/{lost_item_id}", response_model=schemas.LostItem)
def read_lost_item(lost_item_id: int,lostItem: schemas.LostItemUpdate, db: Session = Depends(get_db)):
    db_lost_item = crud.update_lost_item(db, lost_item_id=lost_item_id, lost_item_schemas=lostItem )
    if db_lost_item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return db_lost_item

@router_lost_items.get("/", response_model=List[schemas.LostItem])
def read_lost_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lost_item = crud.get_lost_items(db, skip=skip, limit=limit)
    return lost_item

@router_lost_items.get("/{lost_item_id}", response_model=schemas.LostItem)
def read_lost_item(lost_item_id: int, db: Session = Depends(get_db)):
    db_lost_item = crud.get_lost_item(db, lost_item_id=lost_item_id)
    if db_lost_item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return db_lost_item

