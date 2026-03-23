import redis
import json

r = redis.Redis()

def cache_pdf(hash: str, result: dict):
    r.set(hash, json.dumps(result), ex=86400)

def get_cached_pdf(hash: str):
    data = r.get(hash)
    if data:
        return json.loads(data.decode())