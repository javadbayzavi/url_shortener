from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.environment import ALLOWED_METHODS, ALLOWED_ORIGINS
from api import url_shortener_route
from api.api_limiter import api_limiter

app = FastAPI(
    title="URL Shortener service",
    version="1.0.0",
    description="This is a scaling URL shortener service"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=ALLOWED_METHODS,
    allow_headers=["*"],
)

app.middleware("http")(api_limiter.is_allowed)

app.include_router(url_shortener_route.router)
