from fastapi import HTTPException
from sqlalchemy.orm import Session

from API.Models import user_model as models
from API.Schemas import user_schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schemas.UserCreate):
    if user.user_id == 0:
        print("create")
        _user = get_user_by_email(db, email=user.email)
        if _user:
            raise HTTPException(status_code=400, detail="Email already registered")
        fake_hashed_password = user.password
        db_user = models.User(email=user.email, password=fake_hashed_password)
        db.add(db_user)

        db.commit()
        db.refresh(db_user)
        return db_user
    else:
       print("update")
       _u =  db.query(models.User).filter(models.User.user_id == user.user_id).one_or_none()
       _u.email = user.email
       _u.password = user.password

       db.add(_u)
       db.commit()
       db.refresh(_u)
       return _u


