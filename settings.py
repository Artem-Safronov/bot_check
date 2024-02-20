import logging
import os

logging.basicConfig(
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

API_TOKEN = os.getenv("API_TOKEN")


class DbConfig:
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    db_name = os.getenv("POSTGRES_DB")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    dsn = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}"
