from sqlalchemy import (Column,
                        Integer,
                        ForeignKey,
                        Table)
from .base import Base


class CartGames(Base):
    __tablename__ = 'cart_games'
    cart_id = Column(Integer, ForeignKey('cart.id'), nullable=False)
    game_id = Column(Integer, ForeignKey('game.id'), nullable=False)


class Cart(Base):
    __tablename__ = 'cart'
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
