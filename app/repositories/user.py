from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.base import BaseRepository
from app.schemas.user import UserUpdate
from app.models.user import User

class UserRepository(BaseRepository[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
    
    
    async def get_by_id(self, user_id: str) -> User | None:
        query = select(User).where(User.id == user_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> User | None:
        query = select(User).where(User.email == email)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_by_username(self, username: str) -> User | None:
        query = select(User).where(User.username == username)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def update(self, user: UserUpdate) -> User:
        curr_user = await self.get_by_id(user.id)
        curr_user.name = user.name if user.name else curr_user.name
        curr_user.email = user.email if user.email else curr_user.email
        curr_user.username = user.username if user.username else curr_user.username
        curr_user.hashed_password = user.password if user.password else curr_user.hashed_password
        await self.session.commit()
        await self.session.refresh(curr_user)
        return curr_user

    async def create(self, user: User) -> User:
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def delete(self, user: User) -> bool:
        await self.session.delete(user)
        await self.session.commit()
        return True