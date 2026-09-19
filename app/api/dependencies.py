from app.repositories.user import UserRepository
from app.services.user import UserService

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db

def get_user_repo(session: AsyncSession=Depends(get_db)) -> UserRepository:
    return UserRepository(session)

def get_user_service(user_repo: UserRepository=Depends(get_user_repo)) -> UserService:
    return UserService(user_repo)