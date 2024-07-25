import json
from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status, Response

from backend.crud.carts import get_cart_items, get_cart
from backend.models import Cart
from backend.models.payment import Order
from backend.schemas.carts import CartCreate
from backend.schemas.orders import OrderCreate
from backend.services.payment.yookassapay import create_pay, get_payment


# создать заказ
# подтвердить заказ
# оплатить заказ
# отменить заказ
# получить историю заказов


async def create_order(db: AsyncSession,
                       user_id: int,
                       user_text: str,
                       ) -> Order:
    db_cart = await get_cart_items(db, user_id)
    cart = await get_cart(db, user_id)
    amount = float()
    for cart_item in db_cart:
        amount += cart_item.price
    db_order = Order(user_id=user_id,
                     cart_id=cart.id,
                     amount=amount,
                     contain=json.dumps(db_cart),
                     descriptions=user_text,
                     type_orders=1
                     )
    db.add(db_order)
    await db.commit()
    await db.refresh(db_order)
    return db_order


async def get_order_user(db: AsyncSession, user_id: int) -> List[Order] | None:
    db_item = await db.execute(select(Order).where(Order.user_id == user_id).order_by(Order.id.desc()))
    db_orders = db_item.scalars().all()
    return db_orders


async def lock_active_cart(db: AsyncSession, order_id: int) -> Cart | None:
    cart = await get_cart(db, order_id)
    cart.is_active = False
    await db.commit()
    await db.refresh(cart)
    return cart


async def confirmed_orders(db: AsyncSession, order_id: int) -> Order:
    item = await db.execute(select(Order).filter(Order.id == order_id))
    db_order = item.scalars().first()
    db_order.state = 'confirmed'
    await db.commit()
    await db.refresh(db_order)
    await lock_active_cart(db, db_order.user_id)
    return db_order


async def create_payments(db: AsyncSession, user_id: int):
    pass
