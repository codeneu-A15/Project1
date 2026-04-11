from fastapi import FastAPI
from Backend.database import Base, engine

app = FastAPI()


Base.metadata.create_all(bind=engine)

