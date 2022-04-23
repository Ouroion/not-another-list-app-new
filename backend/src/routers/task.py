# STD Librarys
from typing import List

# 3rd Part Librarys
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

# Self Created Libraries
import schemas
import crud
from database import get_db

router = APIRouter(
    prefix="/task",
    tags=["task"],
    responses={404: {"description": "Not found"}},
)


@router.post("/list", response_model=List[schemas.TaskReturn])
def list_tasks(task_get: schemas.TaskGet, db: Session = Depends(get_db)):
    return crud.get_task(db, access_id=task_get.access_id, id=task_get.id, list_id=task_get.list_id)


@router.post("/create", response_model=schemas.TaskReturn)
def add_task(task_create: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db,
                            access_id=task_create.access_id,
                            list_id=task_create.list_id,
                            name=task_create.name,
                            description=task_create.description,
                            is_done=task_create.is_done)


@router.post("/delete")
def delete_task(task_delete: schemas.TaskDelete, db: Session = Depends(get_db)):
    return crud.delete_task(db,
                            access_id=task_delete.access_id,
                            id=task_delete.id)


@router.post("/isdone")
def is_done(task_is_done: schemas.TaskIsDone, db: Session = Depends(get_db)):
    return crud.update_task_is_done(db,
                                    access_id=task_is_done.access_id,
                                    id=task_is_done.id,
                                    is_done=task_is_done.is_done)
