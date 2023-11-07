from datetime import datetime
from typing import List, Self
from uuid import uuid4

from sqlalchemy import Column, DateTime, String
from sqlalchemy.sql import expression as sql

from app.db import Base


class User(Base):
    """
    Class used for the representation of a user.
    """
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    full_name = Column(String, nullable=False)
    created_at = Column(DateTime, index=True, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.full_name}>'

    @classmethod
    async def create(cls, db, **kwargs) -> Self:
        query = sql.insert(cls).values(id=str(uuid4()), **kwargs)
        users = await db.execute(query)
        await db.commit()
        return users.first()

    @classmethod
    async def update(cls, db, _id, **kwargs) -> Self:
        query = sql.update(cls).where(cls.id == _id).values(**kwargs).execution_options(
            synchronize_session="fetch").returning(cls.id, cls.full_name
        )
        users = await db.execute(query)
        await db.commit()
        return users.first()

    @classmethod
    async def get(cls, db, _id) -> Self:
        query = sql.select(cls).where(cls.id == _id)
        users = await db.execute(query)
        return users.first()

    @classmethod
    async def get_all(cls, db) -> List[Self]:
        query = sql.select(cls)
        result = await db.execute(query)
        users = result.scalars().all()
        return users

    @classmethod
    async def delete(cls, db, _id) -> bool:
        query = sql.delete(cls).where(cls.id == _id).returning(cls.id, cls.full_name)
        await db.execute(query)
        await db.commit()
        return True
