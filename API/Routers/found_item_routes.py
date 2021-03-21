from fastapi import APIRouter
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from API.Schemas import found_item_schemas as schemas
from API.Controllers import  found_item_controller as crud
from ..database import SessionLocal, engine

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router_found_items = APIRouter(
    prefix="/found_items",
    tags=["Found Items"]
)

@router_found_items.post("/", response_model=schemas.FoundItem)
def create_foundItem(foundItem: schemas.FoundItemCreate, db: Session = Depends(get_db)):
    return crud.create_found_item(db=db, found_item_schemas=foundItem)


@router_found_items.get("/", response_model=List[schemas.FoundItem])
def read_found_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    found_item = crud.get_found_items(db, skip=skip, limit=limit)
    return found_item


@router_found_items.get("/{found_item_id}", response_model=schemas.FoundItem)
def read_found_item(foundItem_id: int, db: Session = Depends(get_db)):
    db_found_item = crud.get_found_item(db, found_item_id=foundItem_id)
    if db_found_item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return db_found_item