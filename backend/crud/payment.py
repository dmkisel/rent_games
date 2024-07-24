import json
from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status, Response

from backend.crud.carts import get_cart_items, get_cart
from backend.models.payment import Order
from backend.schemas.orders import OrderCreate
from backend.services.payment.yookassapay import create_pay, get_payment

#создать заказ
#подтвердить заказ
#оплатить заказ
#отменить заказ
#получить историю заказов


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


async def get_order_user(db: AsyncSession, user_id: int) -> List[Order]:
    db_item = await db.execute(select(Order).where(Order.user_id == user_id).order_by(Order.id.desc()))
    db_orders = db_item.scalars().all()
    return db_orders
