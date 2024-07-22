from typing import Optional, List
from pydantic import BaseModel


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
