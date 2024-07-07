from datetime import datetime
from sqlalchemy import (Column,
                        Integer,
                        String,
                        ForeignKey,
                        DateTime,
                        Float)
from sqlalchemy.orm import (relationship,
                            DeclarativeBase)


class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True, index=True)


class Users(Base):
    __tablename__ = 'users'
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    bookings = relationship("Booking", back_populates="user")
    orders = relationship("Order", back_populates="user")


class Game(Base):
    __tablename__ = 'games'
    title = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    available = Column(Integer)
    bookings = relationship("Booking", back_populates="game")
    orders = relationship("Order", back_populates="game")


class Rent(Base):
    __tablename__ = 'rent'
    user_id = Column(Integer, ForeignKey("users.id"))
    game_id = Column(Integer, ForeignKey("games.id"))
    date = Column(DateTime, default=datetime.now())
    time = Column(DateTime)
    user = relationship("User", back_populates="bookings")
    game = relationship("Game", back_populates="bookings")


class Orders(Base):
    __tablename__ = 'orders'
    user_id = Column(Integer, ForeignKey("users.id"))
    game_id = Column(Integer, ForeignKey("games.id"))
    status = Column(String, default="pending")  # Status of the order
    date = Column(DateTime, default=datetime.now())
    user = relationship("User", back_populates="orders")
    game = relationship("Game", back_populates="orders")