from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User
from core.schemas import UserCreate


async def get_all_users(session: AsyncSession) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_user(user_to_create: UserCreate, session: AsyncSession):
    new_user = User(**user_to_create.model_dump())
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user
