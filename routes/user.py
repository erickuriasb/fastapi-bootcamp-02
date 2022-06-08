from typing import List, Generator

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from config.db import SessionLocal
import crud
import schemas


router = APIRouter()

# Dependency


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    try:
        crud.create_user(db=db, user=user)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=ex)
    else:
        return HTTPException(status_code=200, detail="User creates sucessfully")


@router.get('/', response_model=List[schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)

    return users


@router.get('/{user_id}/', response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)

    if not db_user:
        raise HTTPException(status_code=400, detail="User not found")

    return db_user


@router.delete('/{user_id}', response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)

    if not db_user:
        raise HTTPException(status_code=400, detail="User not found")

    try:
        crud.delete_user(db, user_id=db_user.id)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=ex)
    
    return HTTPException(status_code=200, detail="User Deleted")
