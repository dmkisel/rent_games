from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status, Response
from database.models import Game, Cart

from database import models, schemas


    # crud для аренды и покупки


async def read_carts(db: AsyncSession, cart_id: int) -> models.Cart:
    db_cart = await db.execute(select(models.Cart).filter(models.Cart.id == cart_id))
    return db_cart.scalar_one_or_none()


