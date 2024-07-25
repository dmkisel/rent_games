import json
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi_users import fastapi_users, FastAPIUsers
from backend.auth.auth import auth_backend
from backend.auth.manager import get_user_manager
from sqlalchemy.ext.asyncio import AsyncSession

from backend.crud.carts import get_cart_items, get_cart
from backend.crud.payment import create_order, get_order_user, confirmed_orders
from backend.models.users import User
from backend.models.base import get_db
from backend.schemas.orders import (OrderRead,
                                    OrderCreate,
                                    )
from backend.crud.games import (create_game,
                                get_game,
                                get_games)

order_router = APIRouter()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user(verified=True)
current_superuser = fastapi_users.current_user(superuser=True)


# подтвердить заказ
# оплатить заказ
# отменить заказ
# получить историю заказов


@order_router.post("/create/", response_model=OrderRead)
async def create_orders(user: User = Depends(current_user),
                        db: AsyncSession = Depends(get_db),
                        user_text: str = ''):
    order = create_order(db, user.id, user_text)
    return order


@order_router.get("/", response_model=List[OrderRead])
async def get_orders(user: User = Depends(current_user),
                     db: AsyncSession = Depends(get_db)):
    orders = await get_order_user(db, user.id)
    return orders


@order_router.post("/confirmed/<order_id>/", response_model=OrderRead)
async def confirmed_order(order_id: int,
                          user: User = Depends(current_user),
                          db: AsyncSession = Depends(get_db),
                          ):
    order = confirmed_orders(db, order_id)
    return order


@order_router.get("/pay/<order_id>/", response_model=OrderRead)
async def confirmed_order(order_id: int,
                          user: User = Depends(current_user),
                          db: AsyncSession = Depends(get_db),
                          ):
    order = confirmed_orders(db, order_id)
    return order