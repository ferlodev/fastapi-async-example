import asyncio
from typing import Optional

from fastapi import APIRouter
from fastapi_cache import JsonCoder
from fastapi_cache.decorator import cache

from app.crud import user_crud
from app.main import my_key_builder
from app.services import gg

router = APIRouter()


@router.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):

    response = await user_crud.get_user_by_id(item_id)
    return response


@router.get("/items")
@cache(expire=60)
# @cache(expire=60, coder=JsonCoder, key_builder=my_key_builder)
async def read_items(q: Optional[str] = None):

    print("read_items")
    r1, r2, r3, r4 = await asyncio.gather(
        user_crud.get_user_by_id(1),
        user_crud.get_user_by_id(2),
        user_crud.get_user_by_id(3),
        gg.get_google_home(),
        return_exceptions=True
    )

    return [r1, r2, r3, r4]
