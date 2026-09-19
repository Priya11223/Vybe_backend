from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.base import BaseRepository

from app.models.party import Party

class PartyRepository(BaseRepository[Party]):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
    
    async def get_by_id(self, party_id: str) -> Party | None:
        query = select(Party).where(Party.id == party_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, party: Party) -> Party:
        self.session.add(party)
        await self.session.flush()
        await self.session.refresh(party)
        return party