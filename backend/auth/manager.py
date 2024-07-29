import uuid
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, models, FastAPIUsers
from fastapi_users.authentication import BearerTransport, JWTStrategy, AuthenticationBackend
from starlette.responses import Response
from backend.models.users import User, get_user_db
from backend.config import SECRET_MANEGER
from backend.schemas.users import UserRead
from backend.services.smtp.schemas import EmailSchema
from backend.services.smtp.send_email import send_email

SECRET = SECRET_MANEGER


class UserManager(IntegerIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")
        email = EmailSchema(email=user.email,
                            subject=f'Спасибо за регистрацию, {user.username}',
                            body='Вы зарегистрировались на сервисе')
        await send_email(email)
        print(f"User {user.id} send email to {user.email}.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


    async def on_after_login(self,user: User,request: Optional[Request] = None,response: Optional[Response] = None):
        print(f"Logged in")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy)