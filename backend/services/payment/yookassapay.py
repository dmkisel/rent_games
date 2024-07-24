import json
import os

from backend.config import token, account

import uuid

from yookassa import Configuration, Payment

Configuration.account_id = account
Configuration.secret_key = token


async def create_pay(order, site_url):
    redirect_url = site_url + f"state/{order.cart_id}/"
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
        "description": f"ОПЛАТА ЗАКАЗА №{order.id} ОТ {order.date_created}"
    }, idempotence_key)
    return payment


async def get_payment(payment):
    confirmation_url = payment.confirmation.confirmation_url
    # print(confirmation_url)
    # print(idempotence_key)
    # test = '2e2dbea5-000f-5000-a000-12070da8dfae'
    # payment = Payment.find_one(test)
    # res = Payment.list()
    # print(type(res))
    # print(res.)
    # print(type(payment))
    # print(payment.status)
    return confirmation_url

# if __name__ == '__main__':
#     main()
