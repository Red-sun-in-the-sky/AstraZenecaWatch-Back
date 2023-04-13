import aioredis

def get_redis():
    redis = aioredis.from_url(
        "redis://localhost", encoding="utf-8", decode_responses=True
    )
    return redis
