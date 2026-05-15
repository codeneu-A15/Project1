from typing import Annotated
from fastapi import Depends, HTTPException
from Backend.models import UserRole,User,Seller
from jose import jwt,JWTError
import os
from dotenv import load_dotenv
from datetime import timedelta , datetime , timezone
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from Backend.Routers.dependencies.db_dependencies import db_dependency


bcrypt_context = CryptContext(schemes=['bcrypt'] , deprecated = 'auto')
oauth_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

status = load_dotenv('secret.env')

if not status:
    raise FileNotFoundError

SECRET_KEY = os.getenv('SECRET_KEY')

if SECRET_KEY is None:
    raise ValueError

ALGORITHMS = 'HS256'

def create_access_token(user_id : str ,username : str , user_role : UserRole ,expires_delta : timedelta):

    expire_time = datetime.now(timezone.utc) + expires_delta
    issued_at = datetime.now(timezone.utc)

    encode = {
        'sub' : str(user_id),
        'role' : user_role.value,
        'user' : username,
        'exp' : expire_time,
        'iat' : issued_at
    }

    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHMS)

def get_current_user(token : Annotated[str , Depends(oauth_bearer)] , db : db_dependency):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHMS])
        username : str = payload.get('user')
        user_id : str = payload.get('sub')
        if username is None or user_id is None :
            raise HTTPException(status_code=401, detail='Could not validate user.')

        user = db.query(User).filter(User.user_id == int(user_id)).first()

        if not user:
            raise HTTPException(status_code=401 , detail='User does not exist')
        return user

    except JWTError:
        raise HTTPException(status_code=401, detail='Could not validate user.')


def seller_verify(user : Annotated[User , Depends(get_current_user)] , db : db_dependency):
    if user.user_role != UserRole.SELLER:
        raise HTTPException(status_code=403 , detail='Not authorised for this action')
    seller = db.query(Seller).filter(Seller.user_id == user.user_id).first()
    return seller

def admin_verify(user : Annotated[User , Depends(get_current_user)]):
    if user.user_role != UserRole.ADMIN:
        raise HTTPException(status_code=403 , detail='Not authorised for this action')
    return user


def authenticate_user(username : str , password : str , db : db_dependency):
    user = db.query(User).filter(User.username == username).first()
    if not user :
        return False
    if not bcrypt_context.verify(password , user.hashed_password):
        return False
    return user
