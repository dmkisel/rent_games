from typing import Optional, List
from pydantic import BaseModel
from backend.auth.schemas import UserRead

# схемы игр

class GameBase(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    price: float
    price_type: int
    is_active: Optional[bool] = True


class GameCreate(GameBase):
    quantity: int
    pass


class Game(GameBase):

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    carts: List['Cart'] = []

    class Config:
        orm_mode = True

# схемы корзины


class CartBase(BaseModel):
    user_id: int


class CartCreate(CartBase):
    game_ids: Optional[List[int]] = []


class Cart(CartBase):
    id: int
    user: User
    games: List[Game] = []

    class Config:
        orm_mode = True


class Payment(BaseModel):
    id: int


class PaymentCreate(Payment):
    cart_id: int
    amount: float
    description: Optional[str] = None

    class Config:
        orm_mode = True

class UserPayment(Payment):
    payment: str
    state: str

    class Config:
        orm_mode = True