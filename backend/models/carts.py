from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from datetime import datetime
from sqlalchemy import (Column,
                        Integer,
                        String,
                        ForeignKey,
                        DateTime,
                        Float,
                        Boolean, Table)
from sqlalchemy.orm import (relationship,
                            DeclarativeBase)


from .base import Base


cart_games = Table('cart_games', Base.metadata,
                   Column('cart_id', Integer, ForeignKey('cart.id'), primary_key=True),
                   Column('game_id', Integer, ForeignKey('game.id'), primary_key=True)
                   )

class Cart(Base):
    __tablename__ = 'cart'
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='carts')
    games = relationship('Game', secondary=cart_games, back_populates='carts')
