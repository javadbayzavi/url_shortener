from services.cache.cache_provider import redis_client
from typing import Protocol

class CachingProvider(Protocol):
    def get(self, key):
        ...

    def set(self, key, value):
        ...

    def delete(self, key):
        ...


class CacheService:
    def __init__(self, provider: CachingProvider = None):
        self.client = provider if provider else redis_client
        pass

    def get(self, key):
        return self.client.get(key)

    def set(self, key, value):
        return self.client.set(key, value)

    def delete(self, key):
        return self.client.delete(key)


cache_service = CacheService()