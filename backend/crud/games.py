from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.models import Game, Cart

from backend.models.games import Game
from backend.schemas.games import GameCreate


async def create_game(db: AsyncSession, game: GameCreate) -> Game:
    db_game = Game(title=game.title,
                   description=game.description,
                   price=game.price,
                   price_type=game.price_type,
                   quantity=game.quantity,
                   is_active=game.is_active,)
    db.add(db_game)
    await db.commit()
    await db.refresh(db_game)
    return db_game


async def get_games(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Game).offset(skip).limit(limit))
    return result.scalars().all()


async def get_game(db: AsyncSession, game_id: int) -> Game:
    result = await db.execute(select(Game).filter(Game.id == game_id))
    return result.scalars().first()


async def update_game(db: AsyncSession, up_game: GameCreate, game_id: int) -> Game | None:
    db_game = await get_game(db, game_id)
    if db_game is None:
        return None
    db_game.title = up_game.title
    db_game.description = up_game.description
    db_game.price = up_game.price
    db_game.price_type = up_game.price_type
    db_game.quantity = up_game.quantity
    db_game.is_active = up_game.is_active
    db.add(db_game)
    await db.commit()
    await db.refresh(db_game)
    return db_game
