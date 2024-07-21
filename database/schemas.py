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


class User(UserRead):
    carts: List['Cart'] = []

# схемы корзины


class CartBase(BaseModel):
    user_id: int


class CartCreate(CartBase):
    game_ids: List[int]


class Cart(CartBase):
    id: int
    user: User
    games: List[Game] = []

    class Config:
        orm_mode = True