from typing import Optional
from pydantic import BaseModel


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


# схемы корзины

class CartBase(BaseModel):
    user_id: int


class CartCreate(CartBase):
    pass


class Cart(CartBase):
    id: int
    games: list[CartBase]

    class Config:
        orm_mode = True
