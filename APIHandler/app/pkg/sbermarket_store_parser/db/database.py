import asyncio

from sqlalchemy import URL, create_engine, text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import Session, sessionmaker

from APIHandler.app.pkg.sbermarket_store_parser.db.config import settings


async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False,
    # pool_size=5,
    # max_overflow=10,
)

sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=False,
    # pool_size=5,
    # max_overflow=10,
)

session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)