DB_ENGINE = "asyncpg"
DB_USER = "user"
DB_PASSWORD = "example"
DB_NAME = "app"
DB_HOST = "localhost"
DB_PORT = 5432

DB_URL = f"postgresql+{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
url_alembic = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

DB_ECHO = False

SECRET_AUTH = 'hobklm80-mumy'
SECRET_MANEGER = 'kjvmdv#908u9'


token = 'test_WZz6F4B1juxUDdElPNgj3IundBnmFFoqa0i1aaqllng'
account = '424098'

site_url = 'http://localhost:8000'