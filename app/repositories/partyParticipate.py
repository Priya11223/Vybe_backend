from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.base import BaseRepository

from app.models.partyParticipant import PartyParticipant

class PartyParticipantRepository(BaseRepository[PartyParticipant]):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
    
    async def get_by_id(self, participant_id: str) -> PartyParticipant | None:
        query = select(PartyParticipant).where(PartyParticipant.id == participant_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, participant: PartyParticipant) -> PartyParticipant:
        self.session.add(participant)
        await self.session.commit()
        await self.session.refresh(participant)
        return participant
    
    async def delete(self, participant: PartyParticipant) -> bool:
        await self.session.delete(participant)
        await self.session.commit()
        return True

    async def get_all_participants_in_party(self, party_id: str) -> list[PartyParticipant] | None:
        query = select(PartyParticipant).where(PartyParticipant.party_id == party_id)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_all_parties_for_user(self, user_id: str) -> list[PartyParticipant] | None:
        query = select(PartyParticipant).where(PartyParticipant.user_id == user_id)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_by_user_id_and_party_id(self, user_id: str, party_id: str) -> PartyParticipant | None:
        query = select(PartyParticipant).where(PartyParticipant.user_id == user_id, PartyParticipant.party_id == party_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
    
    