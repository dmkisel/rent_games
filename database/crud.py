from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status, Response
from database.models import Game, Cart

from database import models, schemas

#crud для игр

async def create_game(db: AsyncSession, game: schemas.GameCreate):
    db_game = Game(title=game.title,
                   description=game.description,
                   price=game.price,
                   price_type=game.price_type,
                   quantity=game.quantity,
                   is_active=game.is_active,)
    db.add(db_game)
    await db.commit()
    await db.refresh(db_game)
    return db_game


async def get_games(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Game).offset(skip).limit(limit))
    return result.scalars().all()


async def get_game(db: AsyncSession, game_id: int) -> models.Game:
    result = await db.execute(select(models.Game).filter(models.Game.id == game_id))
    return result.scalars().first()


async def update_game(db: AsyncSession, up_game: schemas.GameCreate, game_id: int) -> models.Game:
    db_game = await get_game(db, game_id)
    if db_game is None:
        return None
    db_game.title = up_game.title
    db_game.description = up_game.description
    db_game.price = up_game.price
    db_game.price_type = up_game.price_type
    db_game.quantity = up_game.quantity
    db_game.is_active = up_game.is_active

    db.add(db_game)
    await db.commit()
    await db.refresh(db_game)
    return db_game


# crud для корзины

async def create_carts(db: AsyncSession, cart: schemas.CartCreate):
    db_cart = models.Cart(user_id=cart.user_id)
    db.add(db_cart)
    await db.commit()
    await db.refresh(db_cart)
    return db_cart


async def add_to_cart(db: AsyncSession, cart: schemas.CartCreate, db_cart: schemas.Cart):
    result = await db.execute(select(models.Game).filter(models.Game.id.in_(cart.game_ids)))
    game = result.scalars().all()
    db_cart.games = game
    await db.commit()
    await db.refresh(db_cart)
    return db_cart
    # crud для аренды и покупки


async def read_carts(db: AsyncSession, cart_id: int):
    db_cart = await db.execute(select(models.Cart).filter(models.Cart.id == cart_id))
    return db_cart.scalars().all()

