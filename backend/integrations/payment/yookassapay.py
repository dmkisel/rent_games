import json
import os

token = 'test_WZz6F4B1juxUDdElPNgj3IundBnmFFoqa0i1aaqllng'
account = '424098'

import uuid

from yookassa import Configuration, Payment

Configuration.account_id = account
Configuration.secret_key = token

summ = float(300)
currency = "RUB"
descriptions = 'test на сайте '
id_payment = uuid.uuid4()

redirect_url = "https://www.example.com/return_url"



# def main():
#     idempotence_key = str(uuid.uuid4())
    # payment = Payment.create({
    #     "amount": {
    #         "value": "2.00",
    #         "currency": "RUB"
    #     },
    #     "payment_method_data": {
    #         "type": "bank_card"
    #     },
    #     "confirmation": {
    #         "type": "redirect",
    #         "return_url": "https://www.example.com/return_url"
    #     },
    #     "description": "Заказ №72"
    # }, idempotence_key)
    #
    # confirmation_url = payment.confirmation.confirmation_url
    # print(confirmation_url)
    # print(idempotence_key)

    # test = '2e2dbea5-000f-5000-a000-12070da8dfae'
    # payment = Payment.find_one(test)
    # res = Payment.list()
    # print(type(res))
    # print(res.)
    # print(type(payment))
    # print(payment.status)

# if __name__ == '__main__':
#     main()
