from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase , sessionmaker

Database_url_link = "postgresql://postgres:neeraj55435@localhost/Quiz"

engine = create_engine(Database_url_link,connect_args= {'check same Thread' : False})

Session_local = sessionmaker(autoflush= False , autocommit = False , bind=engine)

class Base(DeclarativeBase):
    pass