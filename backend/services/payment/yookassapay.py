import datetime
from backend.config import token, account, site_url
import uuid
from yookassa import Configuration, Payment
from backend.models.payment import Payment as Pay
Configuration.account_id = account
Configuration.secret_key = token


async def create_pay(order):
    redirect_url = site_url + f"/order/"
    idempotence_key = str(uuid.uuid4())
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
        "description": f"ОПЛАТА ЗАКАЗА №{order.id} ОТ {datetime.datetime.strptime(order.date_created,"%d.%m.%Y")}"
    }, idempotence_key)
    return payment


async def get_payment(order) -> Pay:
    payment = await create_pay(order)
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
