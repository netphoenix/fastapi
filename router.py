from fastapi import APIRouter
from schema import * 
from fastapi import FastAPI, Depends
from database import UserReposytore


user_router = APIRouter(
    prefix="/users",
    tags=['Пользователи']
)

@user_router.post('')
async def add_user(user: UserAdd = Depends()) -> UserId:
    id = await UserReposytore.add_user(user)
    return {"id":id}

@user_router.get('')
async def get_users() -> list[User]:
    users = await UserReposytore.get_users()
    return users

