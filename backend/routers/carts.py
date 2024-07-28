from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi_users import fastapi_users, FastAPIUsers
from backend.auth.auth import auth_backend
from backend.auth.manager import get_user_manager
from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.users import User
from backend.models.base import get_db

from backend.schemas.carts import (CartRead,
                                   CartCreate)
from backend.schemas.games import GameBase
from backend.crud.carts import (get_cart_items,
                                add_items,
                                del_games_cart)

'''
1. Просмотр корзины
2. Добавление в корзину
3. Удаление из корзины

'''

cart_router = APIRouter()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()
current_superuser = fastapi_users.current_user(superuser=True)


@cart_router.get("/", response_model=List[GameBase])
async def get_all_from_cart(db: AsyncSession = Depends(get_db), user: User = Depends(current_user)):
    # user_id = user.id
    cart = await get_cart_items(db, user.id)
    return cart


@cart_router.post("/{game_id}/", response_model=List[GameBase])
async def add_to_carts(game_id: int, db: AsyncSession = Depends(get_db), user: User = Depends(current_user)):
    cart = await add_items(db, user.id, game_id)
    return cart


@cart_router.delete("/{game_id}/", response_model=List[GameBase])
async def delete_from_cart(game_id: int, db: AsyncSession = Depends(get_db), user: User = Depends(current_user)):
    cart = await del_games_cart(db, user.id, game_id)
    return cart
