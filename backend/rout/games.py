from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from typing import List
from database import schemas, models
from database.engine import engine

router = APIRouter()


@router.post("/games/", response_model=schemas.Game)
def create_game(game: schemas.GameCreate, db: Session = Depends(engine.get_db())):
    new_game = models.Game(title=game.title,
                           description=game.description,
                           price=game.price,
                           )
    db.add(new_game)
    db.commit()
    db.refresh(new_game)
    return new_game


@router.get("/games/", response_model=List[schemas.Game])
def read_games(skip: int = 0, limit: int = 10, db: Session = Depends(engine.get_db)):
    games = db.query(models.Game).offset(skip).limit(limit).all()
    return games


@router.get("/games/{game_id}", response_model=schemas.Game)
def read_game(game_id: int, db: Session = Depends(engine.get_db)):
    db_game = db.query(models.Game).filter(models.Game.id == game_id).first()
    if db_game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return db_game
