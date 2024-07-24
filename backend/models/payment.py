from sqlalchemy import (Column,
                        Integer,
                        String,
                        ForeignKey,
                        Float,
                        )
from sqlalchemy.dialects.postgresql import JSONB
from .base import Base


class Order(Base):
    __tablename__ = 'order'
    amount = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    cart_id = Column(Integer, ForeignKey('cart.id'), nullable=False)
    contain = confirmation = Column(JSONB, nullable=False)
    type_orders = Column(Integer, ForeignKey("type_price.id"))
    state = Column(String, nullable=False, default='create')
    descriptions = Column(String, nullable=True)


class Payment(Base):
    __tablename__ = 'payment'
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    payment_id = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    descriptions = Column(String, nullable=False)
    state = Column(String, nullable=False, default='create')
    confirmation = Column(JSONB, nullable=False)

