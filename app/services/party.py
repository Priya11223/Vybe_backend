import uuid
from fastapi import status
from app.repositories.party import PartyRepository
from app.schemas.party import *
from fastapi import HTTPException
from app.models.party import Party

class PartyService():
    def __init__(self, partyRepo: PartyRepository):
        self.partyRepo = partyRepo
        
    async def create_party(self, party: PartyCreate) -> PartyResponse:
        new_party = Party(hosted_by=party.hosted_by)
        res = await self.partyRepo.create(new_party)
        return PartyResponse(id=res.id, hosted_by=res.hosted_by)
    
    async def get_party_by_id(self, party_id: uuid.UUID) -> PartyResponse:
        res = await self.partyRepo.get_by_id(party_id)
        if res is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Party not found")
        return PartyResponse(id=res.id, hosted_by=res.hosted_by)
    
    async def delete_party(self, party: PartyDeleteRequest) -> PartyDeleteResponse:
        existing = await self.partyRepo.get_by_id(party_id=party.id)
        
        if existing is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Party not found")
        
        await self.partyRepo.delete(existing)
        return PartyDeleteResponse(message="Party deleted successfully") 