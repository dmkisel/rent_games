from sqlalchemy import (Column,
                        Integer,
                        String,
                        ForeignKey,
                        Float,
                        Boolean,
                        Table)
from sqlalchemy.orm import (relationship,
                            DeclarativeBase)
from .base import Base


class Payment(Base):
    __tablename__ = 'payment'
    cart_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    amount = Column(Float, nullable=False)
    descriptions = Column(String, nullable=False)
    payment_id = Column(String, nullable=False)
    state = Column(String, nullable=False, default='create')
