import uvicorn

from fastapi import FastAPI, Depends, HTTPException
from fastapi_users import fastapi_users, FastAPIUsers

from backend.models.users import User
from backend.models.base import get_db
from backend.schemas.users import UserRead, UserCreate
from backend.auth.auth import auth_backend
from backend.auth.manager import get_user_manager
from backend.routers import games, carts, payment


app = FastAPI()

# авторизация

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()
current_superuser = fastapi_users.current_user(superuser=True)

# игры

app.include_router(games.game_router,
                   prefix="/games",
                   tags=["games"],
                   )

app.include_router(carts.cart_router,
                   prefix="/carts",
                   tags=["carts"],
                   )

app.include_router(payment.payment_router,
                   prefix="/payment",
                   tags=["payment"],
                   )

# Покупка, текущие статусы

# @app.post("/carts/<cart_id>/pay/", response_model=schemas.UserPayment, tags=["payment"])
# async def create_payment(pay: schemas.PaymentCreate, user: User = Depends(current_user), db: AsyncSession = Depends(get_db)):
#     payment = create_pay(pay)


# telegram, email ведомления и подтверждение


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
