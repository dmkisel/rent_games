from sqlalchemy import (Column,
                        Integer,
                        String,
                        ForeignKey,
                        Float,
                        )
from sqlalchemy.dialects.postgresql import JSONB
from .base import Base


class Payment(Base):
    __tablename__ = 'payment'
    cart_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    payment_id = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    descriptions = Column(String, nullable=False)
    state = Column(String, nullable=False, default='create')
    confirmation = Column(JSONB, nullable=False)
