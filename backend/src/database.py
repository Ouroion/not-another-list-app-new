import json
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

DEPLOYMENT_CONFIG = os.getenv('deployment', 'dev')
DEPLOYMENT_CONFIG_FILE = 'config/' + DEPLOYMENT_CONFIG + '.config.json'

DATABASE_NAME = 'natl'
DATABASE_IP = 'localhost'
DATABASE_PORT = '3306'
DATABASE_USERNAME = 'dev'
DATABASE_PASSWORD = 'developer'

with open(DEPLOYMENT_CONFIG_FILE, 'r') as f:
    config_json = json.load(f)
    DATABASE_NAME = config_json['databaseName']
    DATABASE_IP = config_json['databaseIp']
    DATABASE_PORT = config_json['databasePort']
    DATABASE_USERNAME = config_json['databaseUsername']
    DATABASE_PASSWORD = config_json['databasePassword']


def get_db():
    db = None
    try:
        db = SessionLocal()
        print('Yield Database')
        yield db
    finally:
        print('Finally - Close Database')
        db.close()


SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://{user}:{password}@{ip}:{port}/{db_name}".format(
    user=DATABASE_USERNAME,
    password=DATABASE_PASSWORD,
    ip=DATABASE_IP,
    port=DATABASE_PORT,
    db_name=DATABASE_NAME
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = scoped_session(SessionLocal)
Base = declarative_base()
Base.query = session.query_property()

