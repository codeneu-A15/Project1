from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(
    prefix='/customer',
    tags=['customer']
)

class CustomerSearchQuery(BaseModel):
    query : str
