from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from backend.auth.auth import current_superuser
from backend.models.users import User
from backend.models.base import get_db
from backend.schemas.games import (GameCreate,
                                   GameBase,
                                   GameRead)
from backend.crud.games import (create_game,
                                get_game,
                                get_games,
                                update_game)
'''
1. Просмотр игр
2. Просмотр карточки игр
3. Добавление игр (админ)
4. Редактирование
5. Удаление игр

'''

game_router = APIRouter()


@game_router.post("/create/", response_model=GameCreate)
async def create_games(new_game: GameCreate,
                       user: User = Depends(current_superuser),
                       db: AsyncSession = Depends(get_db)):
    db_game = await create_game(db, new_game)
    if db_game is not None:
        return RedirectResponse(f"/games/{db_game.id}", status_code=200)
    raise HTTPException(status_code=501, detail="Game not created")


@game_router.get("/", response_model=List[GameBase])
async def get_all_games(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    db_games = await get_games(db, skip=skip, limit=limit)
    return db_games


@game_router.get("/{game_id}/", response_model=GameRead)
async def get_game_by_id(game_id: int, db: AsyncSession = Depends(get_db)):
    db_games = await get_game(db, game_id)
    return db_games


@game_router.put("/{game_id}/", response_model=GameRead)
async def update_games(game_id: int, up_game: GameCreate, user: User = Depends(current_superuser), db: AsyncSession = Depends(get_db)):
    db_game = await update_game(db, up_game)
    return db_game
