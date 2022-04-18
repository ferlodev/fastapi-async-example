from sqlalchemy import text

from app.db.mysql_db import async_session
from app.services.generator import get_int


async def get_user_by_id(id):

    print(f"crud: {id}")
    async with async_session() as session:
        
        sql = text("select user_id id, name from User where user_id = :user_id")
        result = await session.execute(sql, {"user_id": id})
        if result: 
            r = result.fetchone()
            return {"id": int(await get_int()), "name": r.name}
