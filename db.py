import aioredis
from config import settings


async def get_redis():
    redis = await aioredis.create_redis_pool(
        f"redis://{settings.redis_host}:{settings.redis_port}"
    )
    try:
        yield redis
    finally:
        redis.close()
        await redis.wait_closed()