from redis import Redis
from core.environment import CACHE_HOST, CACHE_PORT, CACHE_DB

redis_client = Redis(host=CACHE_HOST, port=CACHE_PORT, db=CACHE_DB, decode_responses=True)
