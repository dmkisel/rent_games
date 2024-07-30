import json
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.auth.auth import current_user
from backend.crud.payment import create_order, get_order_user, confirmed_orders, create_payments, check_payment
from backend.models.users import User
from backend.models.base import get_db
from backend.schemas.orders import (OrderRead,
                                    )
from backend.schemas.payment import UserPayment

order_router = APIRouter()


# подтвердить заказ
# оплатить заказ
# отменить заказ
# получить историю заказов


@order_router.post("/create/", response_model=OrderRead)
async def create_orders(user: User = Depends(current_user),
                        db: AsyncSession = Depends(get_db),
                        user_text: str = ''):
    order = await create_order(db, user.id, user_text)
    return order


@order_router.get("/", response_model=List[OrderRead])
async def get_orders(user: User = Depends(current_user),
                     db: AsyncSession = Depends(get_db)):
    orders = await get_order_user(db, user.id)
    return orders


@order_router.post("/confirmed/{order_id}/", response_model=OrderRead)
async def confirmed_order(order_id: int,
                          user: User = Depends(current_user),
                          db: AsyncSession = Depends(get_db),
                          ):
    order = await confirmed_orders(db, order_id)
    #todo: сделать макет (jinja2)
    # email = EmailSchema(email=user.email,
    #                     subject=f'Сформирован заказ №{order.id}',
    #                     body=f'Сформирован заказ на сумму {order.amount}')
    # await send_email(email)
    return order


@order_router.get("/pay/{order_id}/", response_model=UserPayment)
async def payment_order(order_id: int,
                        user: User = Depends(current_user),
                        db: AsyncSession = Depends(get_db),
                        ):
    order = await create_payments(db, order_id)
    return order


@order_router.get("/state/{order_id}/", response_model=UserPayment)
async def payment_check(order_id: int,
                        user: User = Depends(current_user),
                        db: AsyncSession = Depends(get_db),
                        ):
    order = await check_payment(db, order_id)
    return order
