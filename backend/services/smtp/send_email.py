from aiosmtplib import send
from email.message import EmailMessage
from backend.config import rent_game_user,rent_game
from backend.services.smtp.schemas import EmailSchema


async def send_email(email: EmailSchema):
    SMTP_HOST = "smtp.yandex.ru"
    SMTP_PORT = 587
    SMTP_USER = rent_game_user
    SMTP_PASS = rent_game

    message = EmailMessage()
    message["From"] = SMTP_USER
    message["To"] = email.email
    message["Subject"] = email.subject
    message.set_content(email.body)

    await send(
        message,
        hostname=SMTP_HOST,
        port=SMTP_PORT,
        username=SMTP_USER,
        password=SMTP_PASS,
        start_tls=True
    )