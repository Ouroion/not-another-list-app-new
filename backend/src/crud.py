from DefaultException import DefaultException
from typing import List
from sqlalchemy.orm import Session
import uuid

import models
import schemas


#########################
#         USER          #
#########################
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_username_password(db: Session, username: str, password: str):
    return db.query(models.User).filter(models.User.username == username, models.User.password == password).first()


def get_user_by_access_id(db: Session, access_id: str):
    return db.query(models.User).filter(models.User.access_id == access_id).first()


def get_user_by_id(db: Session, id: str):
    return db.query(models.User).filter(models.User.id == id).first()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password
    db_user = models.User(username=user.username, password=fake_hashed_password, access_id=str(uuid.uuid4()))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user_by_access_id_password(db: Session, access_id: str, username: str, password: str):
    res = db.query(models.User).filter(
        models.User.access_id == access_id,
        models.User.username == username,
        models.User.password == password).delete()
    db.commit()
    return res == 1


#########################
#         Lists         #
#########################
def format_list(db: Session, results: List[models.List], return_type: str = "dict"):
    return_list = []
    for result in results:
        return_list.append({
            "id": result.id,
            "user_id": result.user_id,
            "name": result.name,
            "description": result.description,
            "is_done": result.is_done,
        })

    return return_list


def get_list_by_id(db: Session, id: str):
    return format_list(db, db.query(models.List).filter(models.List.id == id).all())


def get_list(db: Session, access_id: str):
    results = []

    if access_id is None:
        raise DefaultException(msg="The Access ID is not specified")

    user_id = get_user_by_access_id(db, access_id=access_id).id
    results.extend(db.query(models.List).filter(models.List.user_id == user_id).all())

    return format_list(db, results)


# TODO -> Create List Should Check to make sure the list hasn't already been created
def create_list(db,
                access_id: str,
                name: str,
                description: str,
                is_done: bool):

    if access_id is None:
        raise DefaultException(msg="The Access ID is not specified")

    user_id = get_user_by_access_id(db, access_id=access_id).id

    db_list = models.List(user_id=user_id,
                          name=name,
                          description=description,
                          is_done=is_done)
    db.add(db_list)
    db.commit()
    db.refresh(db_list)
    return format_list(db, [db_list])


# TODO: This should delete by list.id and not by list.name
# -> rookie shit as you can have multiple lists of the same name
def delete_list(db: Session,
                access_id: str, id: str):
    if access_id is None:
        raise DefaultException(msg="The Access ID is not specified")

    user_id = get_user_by_access_id(db, access_id=access_id).id
    result = db.query(models.List).filter(models.List.id == id,
                                          models.List.user_id == user_id).delete()
    db.commit()
    return result == 1


def update_list_is_done(db: Session, access_id: str, id: str, is_done: bool):
    db.query(models.List).filter(models.List.id == id).update({"is_done": is_done})
    db.commit()


#########################
#         TASK          #
#########################
def get_task_by_id(db: Session, id: int):
    return db.query(models.Task).filter(models.Task.id == id).first()


def get_task(db: Session, access_id: str, id: int, list_id: int):
    if list_id != 0 and list_id is not None:
        return db.query(models.Task).filter(models.Task.list_id == list_id).all()
    return db.query(models.Task).filter(models.Task.id == id).all()


def create_task(db: Session, access_id: str, list_id: str, name: str, description: str, is_done: bool):
    db_task = models.Task(list_id=list_id, name=name, description=description, is_done=is_done)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task_is_done(db: Session, access_id: str, id: str, is_done: bool):
    db.query(models.Task).filter(models.Task.id == id).update({"is_done": is_done})
    db.commit()


def delete_task(db: Session, access_id: str, id: int):
    result = db.query(models.Task).filter(models.Task.id == id).delete()
    db.commit()
    return result == 1
