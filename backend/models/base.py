from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from backend.config import (DB_URL,
                            DB_ECHO)
from sqlalchemy import (Column,
                        Integer,
                        DateTime,
                        func)
from sqlalchemy.orm import (DeclarativeBase)


engine = create_async_engine(DB_URL, echo=DB_ECHO)

async_session = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)


async def get_db():
    async with async_session() as session:
        yield session


class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True, index=True)
    date_created = Column(DateTime(timezone=False), server_default=func.now())
    date_updated = Column(DateTime(timezone=False), onupdate=func.now())


