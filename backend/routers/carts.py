from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi_users import fastapi_users, FastAPIUsers
from backend.auth.auth import auth_backend
from backend.auth.manager import get_user_manager
from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.users import User
from backend.models.base import get_db

from backend.schemas.carts import CartRead, CartCreate
from backend.crud.carts import get_cart,get_cart_items

cart_router = APIRouter()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()
current_superuser = fastapi_users.current_user(superuser=True)


@cart_router.get("/<user_id>/", response_model=CartCreate)
async def get_item_from_cart(user_id: int, db: AsyncSession = Depends(get_db), user: User = Depends(current_user)):
    # user_id = user.id
    cart = await get_cart(db, user_id)
    return cart


@cart_router.post("/<game_id>/", response_model=CartCreate)
async def add_to_cart(cart_id: int, db: AsyncSession = Depends(get_db), user: User = Depends(current_user)):
    cart = await get_cart_items(db, cart_id)
