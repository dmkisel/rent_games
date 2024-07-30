from typing import Optional, List
from pydantic import BaseModel
from .games import GameRead


class CartBase(BaseModel):
    user_id: int


class CartCreate(CartBase):
    id: int
    is_active: Optional[bool] = True

    class Config:
        orm_mode = True


class CartRead(CartBase):
    id: int
    games: List[GameRead] = []

    class Config:
        orm_mode = True


