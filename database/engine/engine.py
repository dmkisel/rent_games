from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.engine.config import (DB_URL,
                                    DB_ECHO)

engine = create_engine(DB_URL, echo=DB_ECHO)

session = sessionmaker(bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
