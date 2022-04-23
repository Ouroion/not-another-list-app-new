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
    prefix="/list",
    tags=["list"],
    responses={404: {"description": "Not found"}},
)


@router.post("/list", response_model=List[schemas.ListReturn])
def list_list(list_get: schemas.ListGet, db: Session = Depends(get_db)):
    if list_get.id is not None:
        return crud.get_list_by_id(db, id=list_get.id)
    return crud.get_list(db,
                         access_id=list_get.access_id)


@router.post("/create",  response_model=schemas.ListReturn)
def add_list(list_create: schemas.ListCreate, db: Session = Depends(get_db)):
    results = crud.create_list(db,
                               access_id=list_create.access_id,
                               name=list_create.name,
                               description=list_create.description,
                               is_done=list_create.is_done)

    if isinstance(results, list):
        return results[0]
    else:
        return results


@router.post("/delete")
def delete_list(list_delete: schemas.ListDelete, db: Session = Depends(get_db)):
    return crud.delete_list(db,
                            access_id=list_delete.access_id,
                            name=list_delete.name)
