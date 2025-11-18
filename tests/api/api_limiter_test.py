import time
from api.api_limiter import TokenBucket

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
    time.sleep(1.5)
    assert bucket.allow() is True