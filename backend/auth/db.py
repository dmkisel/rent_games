from typing import AsyncGenerator
from sqlalchemy import (Column,
                        Integer,
                        String,
                        ForeignKey,
                        DateTime,
                        Float)

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

from database.engine.config import DB_URL

DATABASE_URL = DB_URL
Base: DeclarativeMeta = declarative_base()


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=True)
    telegram = Column(String, unique=True, nullable=True)
    chat_telegram = Column(String, unique=True)
    pass


engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


