import uuid
import asyncio
from backend.config import token, account, site_url
from yookassa import Configuration, Payment
from backend.models.payment import Payment as Pay
from concurrent.futures import ThreadPoolExecutor

Configuration.account_id = account
Configuration.secret_key = token


async def create_pay(order, redirect_url, idempotence_key, formatted_date):
    payment = Payment.create({
        "amount": {
            "value": order.amount,
            "currency": "RUB"
        },
        "payment_method_data": {
            "type": "bank_card"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": redirect_url
        },
        "description": f"ОПЛАТА ЗАКАЗА №{order.id} ОТ {formatted_date}"
    }, idempotence_key)
    return payment


async def get_payment(order) -> Pay:
    redirect_url = site_url + f"/order/"
    idempotence_key = str(uuid.uuid4())
    formatted_date = order.date_created.strftime("%d.%m.%Y")
    payment = await create_pay(order, redirect_url, idempotence_key, formatted_date)
    confirmation_url = payment.confirmation.confirmation_url
    db_pay = Pay(order_id=order.id,
                 amount=order.amount,
                 confirmation_url=str(confirmation_url),
                 payment_id=payment.id)
    return db_pay


async def update_payment(payment_id: str) -> Pay:
    payment = Payment.find_one(payment_id)
    return payment
