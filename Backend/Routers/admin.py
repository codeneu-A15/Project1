from fastapi import APIRouter , HTTPException
from starlette import  status
from Backend.Routers.dependencies.db_dependencies import db_dependency
from Backend.Routers.dependencies.user_dependencies import admin_dependency
from Backend.models import User, Product, Customer , Seller

router = APIRouter(
    prefix='/admin',
    tags=['admin']
)
@router.get('/user' , status_code=status.HTTP_200_OK)
async def get_all_users( _admin : admin_dependency, db : db_dependency):
    users = db.query(User).all()
    return users

@router.get('/user/customer' , status_code=status.HTTP_200_OK)
async def get_all_customer( _admin : admin_dependency, db : db_dependency):
    customer = db.query(Customer).all()
    return customer

@router.get('/user/seller' , status_code=status.HTTP_200_OK)
async def get_all_users( _admin : admin_dependency, db : db_dependency):
    seller = db.query(Seller).all()
    return seller

@router.get('/user/{user_id}' , status_code=status.HTTP_204_NO_CONTENT)
async def get_user(_admin : admin_dependency , db : db_dependency , user_id: int):
    user = db.query(User).filter(User.user_id == user_id).first()
    return user


@router.delete('/user/{user_id}/delete' , status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_permanent(_admin : admin_dependency , db : db_dependency , user_id: int):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404 , detail='User not exists')
    db.delete(user)
    db.commit()
    return {'message' : f'Successfully deleted {user.username}'}


@router.delete('/product/{product_id}/delete' , status_code=status.HTTP_204_NO_CONTENT)
async def delete_product_permanent(_admin : admin_dependency , db : db_dependency , product_id: int):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise HTTPException(status_code=404 , detail='Product not exists')
    db.delete(product)
    db.commit()
    return {'message' : f'Successfully deleted {product.product_id}'}

