from fastapi import APIRouter
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

# from . import crud, models, schemas
from API.Models import user_model as models
from API.Schemas import schemas as schemas
from API.Controllers import  user_controller as crud
from ..database import SessionLocal, engine
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router_user = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router_user.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@router_user.get("/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@router_user.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user