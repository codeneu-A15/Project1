from fastapi import FastAPI
from Backend.Routers import auth
from Backend.database import Base, engine

app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

