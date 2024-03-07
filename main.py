# pip install fastapi
# uvicorn pydantic aiosqlite sqlalchemy

from fastapi  import FastAPI
from schema import UserAdd, USer, UserId
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import user_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("Base build")
    yield
    await delete_tables()
    print("Base dropped")


app = FastAPI(lifespan=lifespan)
app.include_router(user_router)

