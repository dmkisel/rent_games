from typing import Optional
from pydantic import BaseModel


class Payment(BaseModel):
    id: int
    order_id: int
    confirmation_url: str
    description: Optional[str] = None
    amount: float

class PaymentCreate(Payment):
    confirmation: dict

    class Config:
        orm_mode = True


class UserPayment(Payment):
    payment_id: str
    state: str

    class Config:
        orm_mode = True
