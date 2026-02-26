from fastapi import FastAPI

from .lifespan import lifespan
from .settings import settings
from .sample.router import router as sample

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan,
)

app.include_router(sample, prefix="")