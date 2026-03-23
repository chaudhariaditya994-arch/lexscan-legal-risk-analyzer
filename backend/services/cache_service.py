import redis
import json
import os

r = redis.Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))

def cache_pdf(hash: str, result: dict):
    r.set(hash, json.dumps(result), ex=86400)

def get_cached_pdf(hash: str):
    data = r.get(hash)
    if data:
        return json.loads(data.decode('utf-8'))