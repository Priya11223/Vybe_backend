from app.repositories.user import UserRepository
from app.services.user import UserService

from app.repositories.party import PartyRepository
from app.services.party import PartyService

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db

def get_user_repo(session: AsyncSession=Depends(get_db)) -> UserRepository:
    return UserRepository(session)

def get_user_service(user_repo: UserRepository=Depends(get_user_repo)) -> UserService:
    return UserService(user_repo)


def get_party_repo(session: AsyncSession=Depends(get_db)) -> PartyRepository:
    return PartyRepository(session)

def get_party_service(party_repo: PartyRepository=Depends(get_party_repo)) -> PartyService:
    return PartyService(party_repo)