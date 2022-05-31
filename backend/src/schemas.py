from typing import Optional
from pydantic import BaseModel


#########################
# Logged In Base Schema #
#########################
class LoggedInBase(BaseModel):
    access_id: str


#########################
#      USER Schema      #
#########################
class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class UserLogin(UserBase):
    password: str


class UserDelete(UserBase):
    access_id: str
    password: str


class User(UserBase):
    id: int
    access_id: str

    class Config:
        orm_mode = True


#########################
#      List Schema      #
#########################
class ListBase(LoggedInBase):
    pass


class ListGet(ListBase):
    id: Optional[str] = None


class ListCreate(ListBase):
    name: str
    description: str
    is_done: Optional[bool] = False


class ListDelete(ListBase):
    id: str


class ListReturn(BaseModel):
    id: int
    name: str
    description: str
    is_done: bool


#########################
#       Task Schema     #
#########################
class TaskBase(LoggedInBase):
    pass


class TaskGet(TaskBase):
    id: Optional[int] = None
    list_id: Optional[int] = None


class TaskCreate(TaskBase):
    list_id: int
    name: str
    description: str
    is_done: Optional[bool] = False


class TaskDelete(TaskBase):
    id: int


class TaskIsDone(TaskBase):
    id: int
    is_done: Optional[bool] = False


class TaskReturn(BaseModel):
    id: int
    list_id: int
    name: str
    description: str
    is_done: bool

    class Config:
        orm_mode = True
