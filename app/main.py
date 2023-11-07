import logging
import uvicorn

from fastapi import FastAPI

from app.config import settings
from app.db import db

logger = logging.getLogger(__name__)


def init_app():
    application = FastAPI(title='FastAPI with Docker and poetry', description='FastAPI with Docker and poetry', version='0.1.0')

    @application.on_event('startup')
    def startup():
        db.connect(settings.DB_URI)

    @application.on_event('shutdown')
    async def shutdown():
        await db.disconnect()

    from app.views.user_views import api as user_api

    application.include_router(user_api, prefix='/api/v1')
    return application


app = init_app()
