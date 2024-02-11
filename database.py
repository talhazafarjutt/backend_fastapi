from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker


engine = create_async_engine('postgresql+asyncpg://postgres:root@localhost:5432/backup')

async_session: sessionmaker[Session] = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False,
)

Base = declarative_base()


async def get_session() -> AsyncSession:
    """Dependency to create future sessions."""
    async with async_session() as session:
        yield session