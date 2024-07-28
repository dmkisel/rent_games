import smtplib
from smtplib import SMTP
from backend.config import rent_game


smtpObj = smtplib.SMTP('smtp.yandex.ru', 465)
smtpObj.login('repack.inc@yanedex.ru', rent_game)


async def send_email_register(email):
    draft = '''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Спасибо за регистрацию</title>
                </head>
                <body>
                    Вы зарегестировались на сайте!
                    Если хотите получать уведомления в Telegram авторизуйтесь в боте: https://t.me/clients_serv_bot
                </body>
                </html>'''
    smtpObj.starttls()
    smtpObj.sendmail("repack.inc@yanedex.ru", email, draft)
    smtpObj.quit()
    return