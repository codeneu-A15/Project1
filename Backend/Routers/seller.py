import datetime
from starlette import status
from fastapi import APIRouter , HTTPException
from pydantic import BaseModel , Field
from decimal import Decimal
from Backend.Routers.dependencies.db_dependencies import db_dependency
from Backend.Routers.dependencies.user_dependencies import seller_dependency
from Backend.models import Product, OrderItems ,Order
from sqlalchemy import func , extract

router = APIRouter(
    prefix='/seller',
    tags=['seller']
)

class ProductCreateRequest(BaseModel):
    product_name : str = Field(min_length = 3)
    price : Decimal = Field(gt=0,decimal_places=2,max_digits=12)
    stock : int = Field(gt=0)
    brand : str = Field(min_length=3)
    category : str = Field(min_length=3)
    product_image : str | None

class ProductUpdateRequest(BaseModel):
    product_name : str | None = Field(default= None,min_length = 3)
    price : Decimal | None = Field(default= None,decimal_places=2,max_digits=12)
    stock : int | None = Field(default=None ,gt=0)
    category : str | None = Field(default=None , min_length=3)
    product_image : str | None

class SellerSaleQuery(BaseModel):
    year : int = Field(gt=2000,lt= datetime.datetime.now().year + 1)


month_dict = { 1 : 'January' , 2 : 'February' , 3 : 'March' , 4 : 'April' , 5 : 'May' , 6 : 'June' ,
               7 : 'July' , 8 : 'August' , 9 : 'September' , 10 : 'October' , 11 : 'November' , 12 : 'December'}


@router.get('/all_product' , status_code=status.HTTP_200_OK)
async def get_all_product(seller : seller_dependency , db : db_dependency):
     return db.query(Product).filter(Product.seller_id == seller.id).order_by(Product.product_id.desc()).all()


@router.post('/create_product' , status_code=status.HTTP_201_CREATED)
async def create_product(seller : seller_dependency, db : db_dependency, product : ProductCreateRequest):
    item = db.query(Product).filter(Product.product_name == product.product_name,
                                    Product.seller_id==seller.id).first()
    if not item :
        new_product = Product(**product.model_dump() , seller_id=seller.id)
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product
    else:
        raise HTTPException(status_code=400 , detail='Product already exists')

@router.patch('/product/{product_id}' , status_code=status.HTTP_200_OK)
async def update_product(seller : seller_dependency, db : db_dependency
                         ,product_id : int , product : ProductUpdateRequest):
    product_model = db.query(Product).filter(Product.product_id == product_id
                                             , Product.seller_id == seller.id).first()
    if not product_model :
        raise HTTPException(status_code=404 , detail='Product id not exists')

    update_data = product.model_dump(exclude_unset=True)
    for field , value in update_data.items():
        setattr(product_model , field , value)

    db.commit()
    db.refresh(product_model)
    return product_model

@router.delete('/product/{product_id}' , status_code=status.HTTP_200_OK)
async def delete_product(seller : seller_dependency , product_id: int ,  db : db_dependency):
    product = db.query(Product).filter(Product.product_id == product_id ,
                                       Product.seller_id == seller.id).first()
    if not product:
        raise HTTPException(status_code=404 , detail='Product id not exists')
    db.delete(product)
    db.commit()
    return {'message' : 'Successfully deleted product'}


@router.post('/analytics/sales_per_month' , status_code=status.HTTP_201_CREATED)
async def sales_per_month(seller : seller_dependency , db : db_dependency , year :SellerSaleQuery):

    sales_data = (db.query(extract('month', Order.created_at) ,
    func.sum(OrderItems.price_at_purchase * OrderItems.quantity)).join(Order)
                     .filter(OrderItems.seller_id == seller.id,
                    extract('year', Order.created_at)==year.year)
                     .group_by(extract('month',Order.created_at)).all())
    sales_data = dict(sales_data)

    final_sales_data = [
        {
            "month": month_dict[month_num],
            "sales": float(sales_data.get(month_num, 0))
        }
        for month_num in range(1, 13)
    ]

    return final_sales_data
