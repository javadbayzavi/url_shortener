from hashlib import md5

def encoder(url: str) -> str:
    return md5(url.encode()).hexdigest()