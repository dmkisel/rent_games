from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status, Response
from backend.schemas.carts import CartCreate
from backend.models.carts import Cart, CartGames
from backend.models.games import Game
from backend.crud.games import get_game

# crud для корзины


async def create_carts(db: AsyncSession, user_id) -> Cart:
    db_cart = Cart(user_id=user_id)
    db.add(db_cart)
    await db.commit()
    await db.refresh(db_cart)
    return db_cart


async def get_cart(db: AsyncSession, user_id: int) -> Cart | None:
    db_cart = await db.execute(select(Cart).filter(Cart.user_id == user_id and Cart.is_active == True))
    result = db_cart.scalars().first()
    if result is None:
        result = await create_carts(db, user_id)
    return result


async def get_cart_items(db: AsyncSession, user_id: int) -> List[Game]:
    db_cart = await get_cart(db, user_id)
    db_games = await db.execute(select(Game).join(CartGames).filter(CartGames.cart_id == db_cart.id))
    result = db_games.scalars().all()
    return list(result)


async def add_items(db: AsyncSession, user_id: int, game_id: int) -> List[Game]:
    db_cart = await get_cart(db, user_id)
    db_game = CartGames(cart_id=db_cart.id, game_id=game_id)
    db.add(db_game)
    await db.commit()
    db_item = await get_cart_items(db, user_id)
    return db_item


async def del_games_cart(db: AsyncSession, user_id: int, game_id: int) -> List[Game]:
    db_cart = await get_cart(db, user_id)
    game = await db.execute(select(CartGames).filter(CartGames.cart_id == db_cart.id and CartGames.game_id == game_id))
    await db.delete(game)
    await db.commit()
    db_item = await get_cart_items(db, user_id)
    return db_item




# async def add_to_cart(db: AsyncSession, cart: schemas.CartCreate, db_cart: models.Cart):
#     if cart.game_ids:
#         result = await db.execute(select(models.Game).filter(models.Game.id.in_(cart.game_ids)))
#         games = result.scalars().all()
#         db_cart.games = games
#         await db.commit()
#         await db.refresh(db_cart)
#     return db_cart