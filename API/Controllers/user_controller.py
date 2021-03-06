from fastapi import HTTPException
from sqlalchemy.orm import Session

from API.Models import user_model as models
from API.Schemas import user_schemas
import re

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def login_user(db: Session, user: user_schemas.UserLogin):
    login = db.query(models.User).filter(
        models.User.email == user.email,
        models.User.password == user.password
        ).one()
    if login is None:
        raise HTTPException(status_code=400, detail="Invalid credentials or user not found")
    return {'msg': 'login successful'}


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schemas.UserCreate):
    # for password regex is
    # reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
    # match_re = re.compile(reg)
    # res = re.search(reg, user.email)
    # print(res)

    email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    match_email = re.compile(email_regex)
    email_result = re.search(email_regex, user.email)
    # validating conditions
    if email_result:
    # if res and email_result:
        print("Valid Password")
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
            _u = db.query(models.User).filter(models.User.user_id == user.user_id).one_or_none()
            _u.email = user.email
            _u.password = user.password

            db.add(_u)
            db.commit()
            db.refresh(_u)
            return _u
    else:
        print("Invalid Password")

        raise HTTPException(status_code=400, detail="Email or Password error")
        # return {"msg": 'Password too weak, min len = 8, 1 special char, 1 num, 1 capital word atleast required'}




