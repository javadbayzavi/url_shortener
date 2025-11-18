from services.cache.cache_service import cache_service
from services.db.urL_service import url_repository
from services.shortener.encoder import encoder
from asyncio import Lock
from typing import Protocol

class URLShortener(Protocol):
    def __init__(self, cache = None, repository = None):
        self.url_repository = repository if repository else url_repository
        self.cache_service = cache if cache else cache_service
    
    async def shorten_url(self, url) -> str:
        lock = Lock()
        async with lock:
            while True:
                shortened_code = encoder(url=url)
                if not self.url_repository.get_short_code(shortened_code):
                    self.url_repository.add_url(url, shortened_code)
                    self.cache_service.set(shortened_code, url)
                    return shortened_code


url_shortener = URLShortener()