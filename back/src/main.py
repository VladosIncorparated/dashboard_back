from fastapi import FastAPI, Body, APIRouter,Request
from fastapi.middleware.cors import CORSMiddleware
from .settings import settings
from .api.router_files import router as router_files
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_files, prefix="/files_api")