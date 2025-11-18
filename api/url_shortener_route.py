from fastapi.routing import APIRouter
from fastapi import Depends
from fastapi.responses import RedirectResponse, JSONResponse
from services.shortener.shortener import url_shortener, URLShortener
from services.shortener.expander import url_expander, URLExpander
router = APIRouter(prefix="/urls")


async def get_url_shortener() -> URLShortener:
    return url_shortener

async def get_url_expander() -> URLExpander:
    return url_expander

@router.post("/shorten")
async def shorten(url: str, service: URLShortener = Depends(get_url_shortener) ):
    code = await service.shorten_url(url)
    return JSONResponse(
        content={
            code : code
        },
        status_code=200
    ) 



@router.get("/expand/{code}")
async def expand(code: str, redirect: bool = True, service: URLExpander = Depends(get_url_expander)):
    url = service.expand(code)
    if redirect:
        return RedirectResponse(url=url, status_code=302)
    return JSONResponse(
        content={
            "url": url
        },
        status_code=200
    )
