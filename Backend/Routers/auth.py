from fastapi import Depends
from sqlalchemy.exc import IntegrityError
from starlette import status
from fastapi import APIRouter , HTTPException
from pydantic import BaseModel
from Backend.models import Customer, Seller, UserRole , User ,BlackListedToken
from Backend.Routers.dependencies.db_dependencies import db_dependency
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from datetime import timedelta
from Backend.Routers.dependencies.security import create_access_token, bcrypt_context, authenticate_user ,\
                                                    oauth_bearer

router = APIRouter(
    prefix='/auth',
    tags = ['auth']
)

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

class Token(BaseModel):
    access_token : str
    token_type : str

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
async def seller_registration(new_user: CreateNewUser,
                         new_seller: CreateSellerRequest,
                         db: db_dependency):
    try:
        create_user = User(
        username= new_user.username,
        user_role= UserRole.SELLER,
        phone_number=new_user.phone_number,
        email=new_user.email,
        hashed_password = bcrypt_context.hash(new_user.password)
        )
        db.add(create_user)
        db.flush()

        create_seller = Seller(
            user_id=create_user.user_id,
            first_name=new_seller.first_name,
            last_name=new_seller.last_name,
            address=new_seller.address,
            Bio=new_seller.Bio
        )

        db.add(create_seller)
        db.commit()
        return {"message" : " Seller successfully registered" , "Username" : create_user.username}


    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400 , detail='User already exist')

    except HTTPException as e :
        db.rollback()
        print("Something went wrong!")
        raise e


@router.post("/token" , response_model=Token)
async def login_access_token(form_data : Annotated[OAuth2PasswordRequestForm , Depends()] , db : db_dependency):
    user = authenticate_user(form_data.username , form_data.password , db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail='username or password incorrect')

    token = create_access_token(user.user_id , user.username , user.user_role , timedelta(minutes=30))

    return {'access_token' : token , 'token_type' : 'bearer'}


@router.post("/logout")
async def logout( db : db_dependency ,
                     token : Annotated[str , oauth_bearer]):

    token_to_add = BlackListedToken(encoded_string= token)
    db.add(token_to_add)
    db.commit()

    return {'message' : 'logout successful'}