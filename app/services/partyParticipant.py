import uuid
from fastapi import status
from app.repositories.partyParticipate import PartyParticipantRepository
from app.schemas.partyParticipant import *
from fastapi import HTTPException
from app.models.partyParticipant import PartyParticipant

class PartyParticipantService():
    def __init__(self, partyParticipantRepo: PartyParticipantRepository):
        self.partyParticipantRepo = partyParticipantRepo
        
    async def create_party_participant(self, participant: PartyParticipantCreate) -> PartyParticipantResponse:
        
        existing = await self.partyParticipantRepo.get_by_id(participant.user_id)
        if existing is not None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User is already a participant in this party")
        
        new_participant = PartyParticipant(
            party_id=participant.party_id,
            user_id=participant.user_id,
            role=participant.role
        )
        
        return await self.partyParticipantRepo.create(new_participant)
    
    async def get_party_participant_by_id(self, participant_id: uuid.UUID) -> PartyParticipantResponse:
        res = await self.partyParticipantRepo.get_by_id(participant_id)
        if res is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Party participant not found")
        return res
    
    async def delete_party_participant(self, participant: PartyParticipantDeleteRequest) -> PartyParticipantDeleteResponse:
        existing = await self.partyParticipantRepo.get_by_id(participant.id)
        
        if existing is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Party participant not found")
        
        await self.partyParticipantRepo.delete(existing)
        return PartyParticipantDeleteResponse(message="Party participant deleted successfully")