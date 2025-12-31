from contextlib import asynccontextmanager
from fastapi import FastAPI
from api import router as api_router

from core.config import settings
from core.models import db_helper

from core.models import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("[INFO]    App is started")
    yield
    print('[INFO]    Dispose db engine')
    await db_helper.dispose()


app = FastAPI(
    lifespan=lifespan,
)
app.include_router(
    api_router,
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True
    )
