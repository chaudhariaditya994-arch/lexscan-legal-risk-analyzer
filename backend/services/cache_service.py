import redis

r = redis.Redis()

def cache_pdf(hash: str, content: bytes):
    r.set(hash, content)

def get_cached_pdf(hash: str):
    return r.get(hash)