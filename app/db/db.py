from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.db.models import Base
from settings import DbConfig


class Db:

    def __init__(self):
        self._dsn = DbConfig.dsn
        self._engine = create_async_engine(self._dsn)
        self._session = sessionmaker(self._engine, class_=AsyncSession, expire_on_commit=False)

    async def load(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def exit(self):
        await self._engine.dispose()
