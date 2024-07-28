import json
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi_users import fastapi_users, FastAPIUsers
from backend.auth.auth import auth_backend
from backend.auth.manager import get_user_manager
from sqlalchemy.ext.asyncio import AsyncSession
from backend.auth.auth import fastapi_users, current_user, current_superuser
from backend.crud.carts import get_cart_items, get_cart
from backend.crud.payment import create_order, get_order_user, confirmed_orders, create_payments, check_payment
from backend.models.users import User
from backend.models.base import get_db
from backend.schemas.orders import (OrderRead,
                                    OrderCreate,
                                    )
from backend.crud.games import (create_game,
                                get_game,
                                get_games)
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
