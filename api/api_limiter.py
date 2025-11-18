from time import time
from typing import Protocol
from fastapi.responses import JSONResponse

class AppLimiterStrategy(Protocol):
    def allow(self):
        pass

class TokenBucket:
    def __init__(self, capacity:int, rate: float):
        self.capacity = capacity
        self.rate = rate
        self.tokens = capacity
        self.lat_refill = time()

    def allow(self):
        current = time()
        cut_off = current - self.lat_refill
        refilled_rate = self.tokens + cut_off * self.rate
        self.tokens = min(refilled_rate, self.capacity)

        if self.tokens > 1:
            self.tokens -= 1
            return True
        return False


class AppAPILimiter:
    def __init__(self, limiter_strategy: AppLimiterStrategy = None):
        self.limiter = limiter_strategy if limiter_strategy else TokenBucket(200, 0.5)

    async def __call__(self, request, call_next):
        allowed = self.limiter.allow()
        if not allowed:
            return JSONResponse (
                "Too many requests",
                status_code=429
            )
        return await call_next(request)
    


