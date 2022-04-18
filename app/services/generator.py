from app.db.redis_db import redis


async def get_int():
    return await redis.incr("my-counter")
