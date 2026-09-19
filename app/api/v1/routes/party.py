from fastapi import APIRouter, Depends, HTTPException, status
from app.services.party import PartyService
from app.api.dependencies import get_party_service
from app.schemas.party import *

router = APIRouter(prefix="/party", tags=["Party"])

@router.post("", response_model=PartyResponse, status_code=status.HTTP_201_CREATED)
async def create_party(party: PartyCreate, party_service: PartyService = Depends(get_party_service)):
    return await party_service.create_party(party)

@router.get("/{id}", response_model=PartyResponse, status_code=status.HTTP_200_OK)
async def get_party_by_id(id: str, party_service: PartyService = Depends(get_party_service)):
    try:
        party = await party_service.get_party_by_id(id)
        return party
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@router.delete("/{id}", response_model=PartyDeleteResponse, status_code=status.HTTP_200_OK)
async def delete_party(id: str, party_service: PartyService = Depends(get_party_service)):
    try:
        return await party_service.delete_party(PartyDeleteRequest(id=id))
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))