import json
import os
from typing import Optional
try:
    import redis.asyncio as aioredis
    _redis_available = True
except Exception:
    _redis_available = False

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

_redis: Optional[object] = None

async def get_redis():
    global _redis
    if not _redis_available:
        return None
    if _redis is None:
        try:
            _redis = aioredis.from_url(REDIS_URL, encoding="utf-8", decode_responses=True)
            await _redis.ping()
        except Exception:
            _redis = None
    return _redis

async def cache_get(key: str):
    r = await get_redis()
    if not r:
        return None
    try:
        val = await r.get(key)
        return json.loads(val) if val else None
    except Exception:
        return None

async def cache_set(key: str, value, ttl: int = 60):
    r = await get_redis()
    if not r:
        return
    try:
        await r.setex(key, ttl, json.dumps(value, default=str))
    except Exception:
        pass

async def cache_delete(key: str):
    r = await get_redis()
    if not r:
        return
    try:
        await r.delete(key)
    except Exception:
        pass

async def cache_delete_pattern(pattern: str):
    r = await get_redis()
    if not r:
        return
    try:
        keys = await r.keys(pattern)
        if keys:
            await r.delete(*keys)
    except Exception:
        pass
