from fastapi import FastAPI
from Backend.Routers import auth , seller , customer , admin
from Backend.database import Base, engine

app = FastAPI()


app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(seller.router)
app.include_router(customer.router)



@app.get('/')
def checkup():
    return {'status' : 'running'}