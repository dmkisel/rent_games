import uvicorn

from fastapi import FastAPI, Depends, HTTPException
from fastapi_users import FastAPIUsers

from backend.models.users import User
from backend.models.base import get_db
from backend.schemas.users import UserRead, UserCreate, UserUpdate
from backend.auth.auth import auth_backend
from backend.auth.manager import get_user_manager
from backend.routers import games, carts, order
from backend.auth.auth import fastapi_users, current_user, current_superuser

app = FastAPI()


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

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


app.include_router(games.game_router,
                   prefix="/games",
                   tags=["games"],
                   )

app.include_router(carts.cart_router,
                   prefix="/carts",
                   tags=["carts"],
                   )

app.include_router(order.order_router,
                   prefix="/order",
                   tags=["order"],
                   )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
