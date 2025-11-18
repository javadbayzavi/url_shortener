from fastapi.routing import APIRouter
from fastapi.responses import RedirectResponse, JSONResponse
from services.shortener.shortener import url_shortener
from services.shortener.expander import url_expander
router = APIRouter(prefix="/urls")


@router.post("/shorten")
async def shorten(url: str):
    code = await url_shortener.shorten_url(url)
    return JSONResponse(
        content={
            code : code
        },
        status_code=200
    ) 



@router.get("/expand/{code}")
async def expand(code: str, redirect: bool = True):
    url = url_expander.expand(code)
    if redirect:
        return RedirectResponse(url=url, status_code=302)
    return JSONResponse(
        content={
            "url": url
        },
        status_code=200
    )
