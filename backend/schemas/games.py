from typing import Optional
from pydantic import BaseModel


class GameBase(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    price: float
    price_type: int
    is_active: Optional[bool] = True
    image_url: Optional[str]


class GameCreate(GameBase):
    quantity: int


class GameRead(GameBase):

    class Config:
        orm_mode = True
