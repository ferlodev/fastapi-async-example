from typing import Optional
from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()


@router.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


app.include_router(router)

# async def main():
#     print("Hello")

# if __name__ == "__main__":
#     asyncio.run(main())
#     #print("Prueba")
    