from datetime import datetime
from typing import List, Optional, Any
from pydantic import BaseModel


class GameBase(BaseModel):
    title: str
    description: str
    price: float
    available: int


class GameCreate(GameBase):
    pass


class Game(GameBase):
    id: int
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    bookings: List['Booking'] = []
    orders: List['Order'] = []

    class Config:
        orm_mode = True


class RentBase(BaseModel):
    user_id: int
    game_id: int
    date: datetime
    time: datetime


class RentCreate(RentBase):
    pass


class Rent(RentBase):
    id: int
    user: User
    game: Game

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    user_id: int
    game_id: int
    status: str


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    user: User
    game: Game

    class Config:
        orm_mode = True
