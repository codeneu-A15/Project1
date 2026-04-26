from Backend.database import Session_local
from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session

def get_db():
    db = Session_local()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]

