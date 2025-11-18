from services.cache.cache_service import cache_service
from services.db.urL_service import url_repository
class URLExpander:
    def __init__(self, cache_service_instance=None, url_repository_instance=None):
        self.cache_service = cache_service_instance if cache_service_instance else cache_service
        self.url_repository = url_repository_instance if url_repository_instance else url_repository

    def expand(self, url_code: str) -> str | None:
        original = self.cache_service.get(url_code)
        if not original:
            original = self.url_repository.get_original_url(url_code)
            if original:
                self.cache_service.set(url_code, original)
        return original

url_expander = URLExpander()
