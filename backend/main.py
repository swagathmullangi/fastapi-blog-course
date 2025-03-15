from fastapi import FastAPI
from core.config import settings
from api.base import api_router
from app.base import app_router
from fastapi.staticfiles import StaticFiles

def include_router(app):
    app.include_router(api_router)

def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    return app

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
app.include_router(api_router)
app.include_router(app_router)
# configure_static(app)

# @app.get("/")
# def hello_world():
#     return {"msg": "Hello FastAPI!"}