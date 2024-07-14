from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import schemas, models
from fastapi import APIRouter
from database.engine import engine

from backend.rout import games

app = FastAPI()


