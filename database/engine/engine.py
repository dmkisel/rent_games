from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from database.engine.config import (DB_URL,
                                    DB_ECHO)

engine = create_async_engine(DB_URL, echo=DB_ECHO)

async_session = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)


async def get_db():
    async with async_session() as session:
        yield session
