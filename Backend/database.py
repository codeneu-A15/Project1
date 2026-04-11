from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase , sessionmaker
import os
from dotenv import load_dotenv

load_dotenv('db.env')

Database_url_link = os.getenv("Database_url_link")

engine = create_engine(Database_url_link,connect_args= {'check same Thread' : False})

Session_local = sessionmaker(autoflush= False , autocommit = False , bind=engine)

class Base(DeclarativeBase):
    pass