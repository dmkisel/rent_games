from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status, Response
from database.models import Game, Cart

from database import models, schemas


# crud для корзины

async def create_carts(db: AsyncSession, cart: schemas.CartCreate) -> models.Cart:
    db_cart = models.Cart(user_id=cart.user_id,)
    db.add(db_cart)
    await db.commit()
    await db.refresh(db_cart)
    return db_cart


async def add_to_cart(db: AsyncSession, cart: schemas.CartCreate, db_cart: models.Cart):
    if cart.game_ids:
        result = await db.execute(select(models.Game).filter(models.Game.id.in_(cart.game_ids)))
        games = result.scalars().all()
        db_cart.games = games
        await db.commit()
        await db.refresh(db_cart)
    return db_cart