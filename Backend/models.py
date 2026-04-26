import enum
from Backend.database import Base
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, Text, Numeric,Enum
from  sqlalchemy.orm import relationship

class UserRole(enum.Enum):
    CUSTOMER = 'customer'
    ADMIN = 'admin'
    SELLER = 'seller'

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer,primary_key=True,index=True)
    user_role = Column(Enum(UserRole) , nullable= False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String)

    customer_profile = relationship('Customer', back_populates='user', cascade='all , delete-orphan')
    seller_profile = relationship('Seller',back_populates= 'user' , cascade= 'all , delete-orphan')

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer,primary_key=True,index=True)
    address = Column(String ,nullable= False)
    is_active = Column(Boolean ,default=True)
    user_id = Column(Integer , ForeignKey('user.user_id' , ondelete="CASCADE"))
    user = relationship('User',back_populates='customer_profile')

class Seller(Base):

    __tablename__ = 'seller'
    id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String , nullable= False)
    last_name = Column (String , nullable= False)
    address = Column(String , nullable=False)
    Bio = Column(Text)
    user_id = Column(Integer , ForeignKey('user.user_id' , ondelete="CASCADE"))
    products = relationship("Product", back_populates="seller")

    user = relationship('User',back_populates='seller_profile' , uselist=False)


class Product(Base):
    __tablename__ = 'product'

    product_id = Column(Integer , primary_key=True, index=True)
    product_name = Column(String ,nullable= False)
    price = Column(Numeric(10,2) , nullable=False)
    stock = Column(Integer)
    seller_id = Column(Integer , ForeignKey('seller.id' , ondelete="CASCADE") )
    category = Column(String)
    seller = relationship("Seller", back_populates="products" , uselist=False)

