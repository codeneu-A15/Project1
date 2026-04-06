from database import Base
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, DateTime, Text, Numeric


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer,primary_key=True,index=True)
    email = Column(String , unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    phone_number = Column(String)
    address = Column(String)
    is_active = Column(Boolean ,default=True)

class Seller(Base):
    __tablename__ = 'Seller'

    seller_id = Column(Integer,primary_key=True,index=True)
    email = Column(String , unique=True)
    user_name = Column(String , unique=True)
    first_name = Column(String)
    hashed_password = Column(String)
    phone_number = Column(String)
    address = Column(String)
    created_at = Column(DateTime)
    Bio = Column(Text)

class Product(Base):
    __tablename__ = 'products'
    prod_id = Column(Integer , primary_key=True, index=True)
    name = Column(String)
    price = Column(Numeric(10,2) , nullable=False)
    stock = Column(Integer)
    seller_id = Column(Integer , ForeignKey('Seller.id') , unique=True)
    category = Column(String)





