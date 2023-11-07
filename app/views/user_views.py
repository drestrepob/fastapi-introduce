from typing import List

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.models import User
from app.db import db
from app.serializers import UserSerializer


class UserSchema(BaseModel):
    full_name: str


api = APIRouter(prefix='/users', tags=['users'])


@api.post('/')
async def create_user(user: UserSchema, db_session=Depends(db.get_db)) -> UserSerializer:
    user = await User.create(db_session, **user.model_dump())
    return user


@api.get('/{user_id}')
async def get_user(user_id: int, db_session=Depends(db.get_db)) -> UserSerializer:
    user = await User.get(db_session, user_id)
    return user


@api.get('/')
async def get_all_users(db_session=Depends(db.get_db)) -> List[UserSerializer]:
    users = await User.get_all(db_session)
    return users


@api.put('/{user_id}')
async def update_user(user_id: int, user: UserSchema, db_session=Depends(db.get_db)) -> UserSerializer:
    user = await User.update(db_session, user_id, **user.model_dump())
    return user


@api.delete('/{user_id}')
async def delete_user(user_id: int, db_session=Depends(db.get_db)) -> bool:
    return await User.delete(db_session, user_id)
