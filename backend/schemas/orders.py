from typing import Optional
from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import JSONB


class Order(BaseModel):
    id: int
    user_id: int
    cart_id: int


class OrderCreate(Order):
    amount: float
    contain: JSONB
    type_orders: int
    descriptions: str

    class Config:
        orm_mode = True


class OrderRead(Order):
    amount: float
    contain: JSONB
    type_orders: int
    state: str

    class Config:
        orm_mode = True





