from aiosmtplib import send
from email.message import EmailMessage
from backend.config import rent_game_user, rent_game
from backend.services.smtp.schemas import EmailSchema


async def send_email(email: EmailSchema):
    smtp_host = "smtp.yandex.ru"
    smtp_port = 587
    smtp_user = rent_game_user
    smtp_pass = rent_game

    message = EmailMessage()
    message["From"] = smtp_user
    message["To"] = email.email
    message["Subject"] = email.subject
    message.set_content(email.body)

    await send(
        message,
        hostname=smtp_host,
        port=smtp_port,
        username=smtp_user,
        password=smtp_pass,
        start_tls=True,
    )
