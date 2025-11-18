from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from core.environment import ALLOWED_METHODS, ALLOWED_ORIGINS
from api import url_shortener_route
from api.api_limiter import AppAPILimiter


def create_app(app_limiter: AppAPILimiter = None):
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

    @app.get("/")
    async def root():
        return JSONResponse(
            status_code=200,
            content=None
        )

    if app_limiter:
        app.middleware("http")(app_limiter)
    else:
        app.middleware("http")(AppAPILimiter())

    app.include_router(url_shortener_route.router)
    return app