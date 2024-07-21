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


class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True, index=True)

class User(Base):
    __tablename__ = 'user'
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    telegram = Column(String, unique=True)
    chat_telegram = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    carts = relationship('Cart', back_populates='user')


class TypePrice(Base):
    __tablename__ = 'type_price'
    name = Column(String, unique=True)


cart_games = Table('cart_games', Base.metadata,
                   Column('cart_id', Integer, ForeignKey('cart.id'), primary_key=True),
                   Column('game_id', Integer, ForeignKey('game.id'), primary_key=True)
                   )


class Game(Base):
    __tablename__ = 'game'
    title = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    price_type = Column(Integer, ForeignKey("type_price.id"))
    quantity = Column(Integer, default=0)
    is_active = Column(Boolean, default=False)
    carts = relationship('Cart', secondary=cart_games, back_populates='games')

    def deactivate_at_zero(self):
        if self.quantity == 0 or self.price == 0:
            self.is_active = False
        if self.quantity > 0 and self.price > 0:
            self.is_active = True
        return


class Cart(Base):
    __tablename__ = 'cart'
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='carts')
    games = relationship('Game', secondary=cart_games, back_populates='carts')


class Payment(Base):
    __tablename__ = 'payment'
    cart_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    amount = Column(Float, nullable=False)
    descriptions = Column(String, nullable=False)
    payment = Column(String, nullable=False)
    state = Column(String, nullable=False, default='create')


