# STD Librarys

# 3rd Part Librarys
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

# Self Created Libraries
import schemas
import crud
from database import get_db
from DefaultException import DefaultException

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.post("/register", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise DefaultException(msg="A user with that username already exists")
    return crud.create_user(db=db, user=user)


@router.post("/login")
def create_user_sesion(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username_password(
        db, username=user.username, password=user.password)
    if not db_user:
        raise DefaultException(msg="Invalid Username/Password")
    return {"access_id": db_user.access_id}


@router.post("/delete")
def delete_user(user: schemas.UserDelete, db: Session = Depends(get_db)):
    res = crud.delete_user_by_access_id_password(db,
                                                 access_id=user.access_id,
                                                 username=user.username,
                                                 password=user.password)
    if res:
        return {'msg': 'Delete Successful'}
    raise DefaultException(msg="Unable to Delete User")
