from starlette import status
from fastapi import APIRouter
from pydantic import BaseModel
from Backend.models import Customer , Seller
from passlib.context import CryptContext
from  Backend.Routers.dependency import db_dependency

router = APIRouter(
    prefix='/auth',
    tags = ['auth']
)

bcrypt_context = CryptContext(schemes=['bcrypt'] , deprecated = 'auto')


class CreateCustomerRequest(BaseModel):
    username : str
    email : str
    password : str
    phone_number : str
    address : str


class CreateSellerRequest(BaseModel):
    username : str
    first_name : str
    last_name : str
    email : str
    password : str
    phone_number : str
    address : str
    Bio : str


@router.post("/new_customer" , status_code= status.HTTP_201_CREATED)
async def create_new_customer(new_user : CreateCustomerRequest , db : db_dependency):
    create_user = Customer(
        username = new_user.username,
        email = new_user.email,
        hashed_password = bcrypt_context.hash(new_user.password),
        phone_number = new_user.phone_number,
        address = new_user.address
    )

    db.add(create_user)
    db.commit()

@router.post("/new_seller" , status_code=status.HTTP_201_CREATED)
async def create_new_customer(new_user : CreateSellerRequest , db : db_dependency):
    create_user = Seller(
        username= new_user.username,
        email= new_user.email,
        hashed_password= bcrypt_context.hash(new_user.password),
        first_name= new_user.first_name,
        last_name= new_user.last_name,
        address= new_user.address,
        phone_number= new_user.phone_number,
        Bio= new_user.Bio
    )

    db.add(create_user)
    db.commit()

