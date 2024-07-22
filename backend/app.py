# from database.engine import engine
# from sqlalchemy.orm import Session
# from database import schemas, models
# from backend.rout import games

from typing import List

import yaml
from fastapi.responses import RedirectResponse
import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi import APIRouter
from fastapi_users import fastapi_users, FastAPIUsers
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from backend.auth.db import User
from backend.auth.auth import auth_backend
from backend.auth.manager import get_user_manager
from backend.auth.schemas import UserRead, UserCreate
from database import crud, schemas, models
from database.engine.engine import get_db
from backend.services.payment.yookassapay import create_pay,get_payment

with open("config.yaml", "r") as stream:
    config = yaml.safe_load(stream)

app = FastAPI()


#авторизация

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

#игры



@app.post("/games/create/", response_model=schemas.GameCreate, tags=["games"])
async def create_game(new_game: schemas.GameCreate, user: User = Depends(current_superuser), db: AsyncSession = Depends(get_db)):
    db_game = await crud.create_game(db, new_game)
    if db_game is not None:
        return RedirectResponse(f"/games/{db_game.id}", status_code=200)
    raise HTTPException(status_code=501, detail="Game not created")


@app.get("/games/", response_model=List[schemas.GameBase], tags=["games"])
async def get_games(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    games = await crud.get_games(db, skip=skip, limit=limit)
    return games


@app.get("/games/<game_id>/", response_model=schemas.Game, tags=["games"])
async def get_game(game_id: int, db: AsyncSession = Depends(get_db)):
    game = await crud.get_game(db, game_id)
    return game


# @app.put("/games/<game_id>", response_model=schemas.GameCreate, tags="games")
# async def update_game(game_id: int, game: schemas.GameCreate, user: User = Depends(current_superuser), db: AsyncSession = Depends()):
#     db_game = await crud.update_game(db, game, game_id)
#     return db_game

#корзина

@app.post("/carts/", response_model=schemas.Cart, tags=["carts"])
async def create_cart(cart: schemas.CartCreate, db: AsyncSession = Depends(get_db), user: User = Depends(current_user)):
    db_cart = await crud.create_carts(db, cart)

    # if cart.game_ids:
    #     db_cart = await crud.add_to_cart(db, cart, db_cart)
    #
    # # Явное получение атрибутов перед возвратом
    # db_user = db_cart.user
    # db_games = db_cart.games
    #
    # return schemas.Cart(
    #     id=db_cart.id,
    #     user_id=db_cart.user_id,
    #     user=schemas.User(id=db_user.id, name=db_user.name),
    #     games=[schemas.Game(id=game.id, title=game.title, genre=game.genre) for game in db_games]
    # )
    return db_cart

@app.get("/carts/<cart_id>", response_model=schemas.Cart, tags=["carts"])
async def read_cart(cart_id: int, db: AsyncSession = Depends(get_db), user: User = Depends(current_user)):
    db_cart = await crud.read_carts(db, cart_id)
    if db_cart is None:
        raise HTTPException(status_code=404, detail="Cart not found")
    await db.refresh(db_cart)
    db_user = db_cart.user
    db_games = db_cart.games
    return schemas.Cart(id=db_cart.id,
                        user_id=db_cart.user_id,
                        user=schemas.User(id=db_user.id, name=db_user.name),
                        games=[schemas.Game(id=game.id, title=game.title) for game in db_games])





#Покупка, текущие статусы

# @app.post("/carts/<cart_id>/pay/", response_model=schemas.UserPayment, tags=["payment"])
# async def create_payment(pay: schemas.PaymentCreate, user: User = Depends(current_user), db: AsyncSession = Depends(get_db)):
#     payment = create_pay(pay)


#telegram, email ведомления и подтверждение




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)