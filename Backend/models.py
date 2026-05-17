import enum
from Backend.database import Base
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, Text, Numeric, Enum, DateTime
from  sqlalchemy.orm import relationship
from datetime import datetime, timezone


class UserRole(enum.Enum):
    CUSTOMER = 'customer'
    ADMIN = 'admin'
    SELLER = 'seller'

class PaymentMethod(enum.Enum):
    UPI = 'upi'
    CASH = 'cash_on_delivery'
    CARD = 'card'

class DeliveryStatus(enum.Enum):
    TRANSIT = 'transit'
    PENDING = 'pending'
    DISPATCHED = 'dispatched'
    DELIVERED = 'delivered'
    DELAYED = 'delayed'
    OUT_FOR_DELIVERY = 'out_for_delivery'
    FAILED = 'failed'

class PaymentStatus(enum.Enum):
    DONE = 'done'
    PENDING = 'pending'


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
    product_image = Column(String , nullable= True)
    product_name = Column(String ,nullable= False)
    price = Column(Numeric(10,2) , nullable=False)
    stock = Column(Integer , nullable=False)
    description = Column(String , nullable=False)
    seller_id = Column(Integer , ForeignKey('seller.id' , ondelete="CASCADE") )
    category = Column(String)
    seller = relationship("Seller", back_populates="products" , uselist=False)


class Order(Base):
    __tablename__ = 'order'

    order_id = Column(Integer , primary_key=True , index=True)
    customer_id = Column(Integer , ForeignKey('customer.id'))
    total_amount = Column(Numeric(10 , 2) , nullable=False)
    delivery_mode = Column(Enum(PaymentMethod) , nullable=False)
    created_at = Column(DateTime,default= lambda:datetime.now(timezone.utc))
    payment_status = Column(Enum(PaymentStatus) , default=PaymentStatus.PENDING)


class OrderItems(Base):
    __tablename__ = 'item'

    item_id = Column(Integer , primary_key=True , index=True)
    order_id = Column(Integer , ForeignKey('order.order_id'))
    seller_id = Column(Integer ,ForeignKey('seller.id'))
    quantity = Column(Integer , nullable=False)
    price_at_purchase = Column(Numeric(10 , 2) , nullable=False)
    delivery_status = Column(Enum(DeliveryStatus) , default= DeliveryStatus.PENDING)
