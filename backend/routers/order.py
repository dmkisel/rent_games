from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi_users import fastapi_users, FastAPIUsers
from backend.auth.auth import auth_backend
from backend.auth.manager import get_user_manager
from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.users import User
from backend.models.base import get_db
from backend.schemas.games import (GameCreate,
                                   GameBase,
                                   GameRead)
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


#создать заказ
#подтвердить заказ
#оплатить заказ
#отменить заказ
#получить историю заказов



# @payment_router.post("/create/", response_model=GameCreate)
# async def create_payment(user: User = Depends(current_superuser), db: AsyncSession = Depends(get_db)):
#
