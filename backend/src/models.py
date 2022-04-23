from sqlalchemy import Column, Integer
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import VARCHAR, Boolean
from database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(VARCHAR(255))
    password = Column(VARCHAR(255))
    access_id = Column(VARCHAR(1024))


class List(Base):
    __tablename__ = 'list'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    name = Column(VARCHAR(255))
    description = Column(VARCHAR(255))
    is_done = Column(Boolean)


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True, index=True)
    list_id = Column(Integer, ForeignKey("list.id", ondelete='SET NULL'), nullable=True)
    name = Column(VARCHAR(255))
    description = Column(VARCHAR(255))
    is_done = Column(Boolean)