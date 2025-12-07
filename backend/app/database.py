from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from app.config import settings


engine = create_async_engine(
    settings.database_url,
    echo=settings.debug,
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Base pour les modèles SQLAlchemy
Base = declarative_base()


# Dependency pour FastAPI
async def get_db():
    """
    Crée une session DB pour chaque requête
    Usage : db: AsyncSession = Depends(get_db)
    """
    async with AsyncSessionLocal() as session:
        yield session