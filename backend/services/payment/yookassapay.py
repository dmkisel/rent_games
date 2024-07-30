from backend.config import token, account
from yookassa import Configuration, Payment
from backend.models.payment import Payment as Pay
from concurrent.futures import ThreadPoolExecutor
import asyncio
Configuration.account_id = account
Configuration.secret_key = token


def create_pay(order, redirect_url, idempotence_key, formatted_date):
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

    formatted_date = order.date_created.strftime("%d.%m.%Y")
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        payment = await loop.run_in_executor(
            pool,
            create_pay,
            order,
            redirect_url,
            idempotence_key,
            formatted_date
        )
    confirmation_url = payment.confirmation.confirmation_url
    db_pay = Pay(order_id=order.id,
                 amount=order.amount,
                 confirmation=dict(payment),
                 confirmation_url=str(confirmation_url),
                 payment_id=payment.id)
    return db_pay


async def update_payment(payment_id: str) -> Pay:
    payment = Payment.find_one(payment_id)
    return payment
