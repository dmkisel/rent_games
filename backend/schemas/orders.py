from pydantic import BaseModel


class Order(BaseModel):
    id: int
    user_id: int
    cart_id: int


class OrderCreate(Order):
    amount: float
    contain: dict
    type_orders: int
    descriptions: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class OrderRead(Order):
    amount: float
    contain: dict
    type_orders: int
    state: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True




