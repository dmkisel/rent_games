from sqlalchemy import (Column,
                        String,
                        Boolean,
                        Table)
from sqlalchemy.orm import (relationship,
                            DeclarativeBase)
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
from .base import Base, async_session


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    telegram = Column(String, unique=True)
    chat_telegram = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

# class User(Base):
#     __tablename__ = 'user'
#     username = Column(String, unique=True)
#     email = Column(String, unique=True)
#     telegram = Column(String, unique=True)
#     chat_telegram = Column(String, unique=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True, nullable=False)
#     is_superuser = Column(Boolean, default=False, nullable=False)
#     is_verified = Column(Boolean, default=False, nullable=False)
#     carts = relationship('Cart', back_populates='user')


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
