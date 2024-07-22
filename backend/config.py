DB_ENGINE = "asyncpg"
DB_USER = "user"
DB_PASSWORD = "example"
DB_NAME = "app"
DB_HOST = "localhost"
DB_PORT = 5432

DB_URL = f"postgresql+{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
url_alembic = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

DB_ECHO = True