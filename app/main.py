from typing import Optional

from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
#from starlette.requests import Request
#from starlette.responses import Response

from app.api.routers.test import router
from app.db.redis_db import redis

app = FastAPI()
app.include_router(router)


# def my_key_builder(func, namespace: Optional[str] = "", req: Request = None, resp: Response = None, *args, **kwargs, ):
#     prefix = FastAPICache.get_prefix()
#     cache_key = f"{prefix}:{namespace}:{func.__module__}:{func.__name__}:{args}:{kwargs}"
#     return cache_key


@app.on_event("startup")
async def startup():

    FastAPICache.init(RedisBackend(redis), prefix="fast-async")
