from Backend.database import Base
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, Text, Numeric
from  sqlalchemy.orm import relationship

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer,primary_key=True,index=True)
    email = Column(String , unique=True , nullable= False)
    username = Column(String , unique=True , nullable=False)
    hashed_password = Column(String)
    phone_number = Column(String , unique=True , nullable=False)
    address = Column(String ,nullable= False)
    is_active = Column(Boolean ,default=True)

class Seller(Base):

    __tablename__ = 'Seller'
    id = Column(Integer,primary_key=True,index=True)
    email = Column(String , unique=True , nullable= False)
    user_name = Column(String , unique=True , nullable=False)
    first_name = Column(String , nullable= False)
    last_name = Column (String , nullable= False)
    hashed_password = Column(String)
    phone_number = Column(String , nullable=False)
    address = Column(String , nullable=False)
    Bio = Column(Text)

    products = relationship("Product", back_populates="seller")


class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer , primary_key=True, index=True)
    product_name = Column(String ,nullable= False)
    price = Column(Numeric(10,2) , nullable=False)
    stock = Column(Integer)
    seller_id = Column(Integer , ForeignKey('Seller.id') )
    category = Column(String)
    seller = relationship("Seller", back_populates="products")