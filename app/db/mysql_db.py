from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


engine = create_async_engine("mysql+aiomysql://root:root00@localhost/test", echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
