from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import select
from schema import UserAdd

engine = create_async_engine("sqlite+aiosqlite:///DB.db")
new_session = async_sessionmaker (engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass
class UserOrm(Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str]
    age: Mapped[int]
    phone: Mapped[str|None]

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

class UserReposytore:

    @classmethod
    async def add_user(cls, user:UserAdd) -> int:
        async with new_session() as session:
            data = user.model_dump()
            user = UserOrm(**data)
            session.add(user)
            await session.flush()
            await session.commit()
            return user.id

    @classmethod
    async def get_users(cls) -> list[UserOrm]:
        async with new_session() as session:
            query = select(UserOrm)
            await session.execute()
            await session.commit()
            return user.id

        


