from typing import List

from sqlalchemy import Integer, and_, cast, func, insert, inspect, select, text

from APIHandler.app.pkg.sbermarket_store_parser.db.database import (
    async_engine,
    async_session_factory,
    session_factory,
    sync_engine,
)
from APIHandler.app.pkg.sbermarket_store_parser.db.models import Base, Category, Product


class AsyncORM:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def insert_item(data: Category | Product):
        async with async_session_factory() as session:
            session.add(data)
            await session.flush()
            await session.commit()

    @staticmethod
    async def select_items():
        async with async_session_factory() as session:
            query = select(Category)
            result = await session.execute(query)
            items = result.scalars().all()
            print(f"{items=}")