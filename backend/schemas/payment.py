from typing import Optional, List
from pydantic import BaseModel
from backend.auth.schemas import UserRead


class Payment(BaseModel):
    id: int


class PaymentCreate(Payment):
    cart_id: int
    amount: float
    description: Optional[str] = None

    class Config:
        orm_mode = True


class UserPayment(Payment):
    payment_id: str
    state: str

    class Config:
        orm_mode = True