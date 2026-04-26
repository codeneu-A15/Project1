from sqlalchemy.exc import IntegrityError
from starlette import status
from fastapi import APIRouter , HTTPException
from pydantic import BaseModel
from Backend.models import Customer, Seller, UserRole , User
from passlib.context import CryptContext
from  Backend.Routers.dependency import db_dependency

router = APIRouter(
    prefix='/auth',
    tags = ['auth']
)

bcrypt_context = CryptContext(schemes=['bcrypt'] , deprecated = 'auto')

class CreateNewUser(BaseModel):
    username : str
    user_role : UserRole
    phone_number : str
    email : str
    password: str

class CreateCustomerRequest(BaseModel):
    address : str


class CreateSellerRequest(BaseModel):
    first_name : str
    last_name : str
    Bio : str
    address : str


@router.post("/CustomerResgistration" , status_code= status.HTTP_201_CREATED)
async def customer_registration(new_user : CreateNewUser ,
                          new_customer : CreateCustomerRequest,
                          db : db_dependency):
    try:

        create_user = User(
        username= new_user.username,
        user_role= UserRole.CUSTOMER,
        phone_number=new_user.phone_number,
        email=new_user.email,
        hashed_password = bcrypt_context.hash(new_user.password)
        )
        db.add(create_user)
        db.flush()

        create_customer = Customer(
         user_id=create_user.user_id ,
         address = new_customer.address
        )

        db.add(create_customer)
        db.commit()

        return {"message" : " Customer successfully registered" , "Username" : create_user.username}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400 , detail='User already exist')

    except HTTPException as e :
        db.rollback()
        raise e


@router.post("/SellerResgistration", status_code=status.HTTP_201_CREATED)
async def create_new_seller(new_user: CreateNewUser,
                         new_seller: CreateSellerRequest,
                         db: db_dependency):
    try:
        create_user = User(
        username= new_user.username,
        user_role= UserRole.CUSTOMER,
        phone_number=new_user.phone_number,
        email=new_user.email,
        hashed_password = bcrypt_context.hash(new_user.password)
        )
        db.add(create_user)
        db.flush()

        create_seller = Seller(
            first_name=new_seller.first_name,
            last_name=new_seller.last_name,
            address=new_seller.address,
            Bio=new_seller.Bio
        )

        db.add(create_seller)
        db.commit()

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400 , detail='User already exist')

    except HTTPException as e :
        db.rollback()
        print("Something went wrong!")
        raise e

