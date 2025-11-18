import time
from api.api_limiter import TokenBucket, AppAPILimiter
from api.api import app
from fastapi.testclient import TestClient




def test_token_bucket_basic():
    bucket = TokenBucket(capacity=3, rate=1.0)

    # Should allow 3 times immediately
    assert bucket.allow() is True
    assert bucket.allow() is True
    assert bucket.allow() is True

    # 4th should be denied
    assert bucket.allow() is False


def test_token_bucket_refill():
    bucket = TokenBucket(capacity=2, rate=1.0)

    bucket.allow()  # now 1 left
    bucket.allow()  # now 0 left

    assert bucket.allow() is False  # empty

    # wait 1.1 seconds → rate=1.0 → 1 token should refill
    time.sleep(1.1)
    assert bucket.allow() is True


def test_api_limiter_basic(monkeypatch):
    small_bucket = TokenBucket(capacity=2, rate=1.0)

    monkeypatch.setattr("api.api_limiter", AppAPILimiter(small_bucket))

    # app.middleware_stack = app.build_middleware_stack()

    client = TestClient(app)

    assert client.get("/").status_code == 200
    assert client.get("/").status_code == 200
    assert client.get("/").status_code == 429


