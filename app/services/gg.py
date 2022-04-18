import httpx

from app.db.redis_db import redis
from app.services.generator import get_int


async def get_google_home():

    status = await redis.get("google_home_status")
    if status:
        return {"id": int(await get_int()), "name": "google", "status": status}

    async with httpx.AsyncClient() as client:
        r = await client.get('https://www.google.com/')
        status = r.status_code
        await redis.set("google_home_status", status, 180)
    return {"id": int(await get_int()), "name": "google", "status": status}
