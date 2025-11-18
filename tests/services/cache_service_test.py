from testcontainers.redis import RedisContainer
from services.cache.cache_service import CacheService, CachingProvider
import pytest

class FakeRedisClient:
    def __init__(self):
        self.cache = {}

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        self.cache[key] = value
        return True

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
            return 1
        return 0

@pytest.fixture
def cache_service_fake():
    fake_client = FakeRedisClient()
    return CacheService(provider=fake_client)


@pytest.fixture
def cache_service():
    redis_container = RedisContainer()

    with redis_container:
    
        cache_service = CacheService()
        yield cache_service

        redis_container.get_client().flushall()




def test_cache_service_set_value(cache_service_fake):

    cache_service_fake.set("test_key", "test_value")
    
    assert cache_service_fake.get("test_key") == "test_value"

def test_cache_service_get_value(cache_service_fake):
    cache_service_fake.set("test_key", "test_value")
    
    assert cache_service_fake.get("test_key") == "test_value"

def test_cache_service_delete_value(cache_service_fake):
    cache_service_fake.set("test_key", "test_value")
    
    assert cache_service_fake.delete("test_key") == 1
    assert cache_service_fake.get("test_key") is None


def test_cache_service_delete_nonexistent_value(cache_service_fake):
    assert cache_service_fake.delete("nonexistent_key") == 0

def test_cache_service_get_nonexistent_value(cache_service_fake):
    assert cache_service_fake.get("nonexistent_key") is None

def test_cache_service_not_duplicated_key(cache_service_fake):
    cache_service_fake.set("test_key", "test_value")
    cache_service_fake.set("test_key", "test_new_value")

    assert cache_service_fake.get("test_key") == "test_new_value"


def test_integrated_cache_service_set_value(cache_service):

    cache_service.set("test_key", "test_value")
    
    assert cache_service.get("test_key") == "test_value"

def test_cintegrated_ache_service_get_value(cache_service):
    cache_service.set("test_key", "test_value")
    
    assert cache_service.get("test_key") == "test_value"

def test_cintegrated_ache_service_delete_value(cache_service):
    cache_service.set("test_key", "test_value")
    
    assert cache_service.delete("test_key") == 1
    assert cache_service.get("test_key") is None


def test_integrated_cache_service_delete_nonexistent_value(cache_service):
    assert cache_service.delete("nonexistent_key") == 0

def test_integrated_cache_service_get_nonexistent_value(cache_service):
    assert cache_service.get("nonexistent_key") is None

def test_integrated_cache_service_not_duplicated_key(cache_service):
    cache_service.set("test_key", "test_value")
    cache_service.set("test_key", "test_new_value")

    assert cache_service.get("test_key") == "test_new_value"
