from fastapi import APIRouter, Depends, HTTPException, status
from app.services.partyParticipant import PartyParticipantService
from app.api.dependencies import get_partyParticipant_service
from app.schemas.partyParticipant import *

router = APIRouter(prefix="/party-participant", tags=["Party-Participant"])

@router.post("", response_model=PartyParticipantResponse, status_code=status.HTTP_201_CREATED)
async def create_party_participant(participant: PartyParticipantCreate, partyParticipant_service: PartyParticipantService = Depends(get_partyParticipant_service)):
    return await partyParticipant_service.create_party_participant(participant)

@router.get("/{id}", response_model=PartyParticipantResponse, status_code=status.HTTP_200_OK)
async def get_party_participant_by_id(id: str, partyParticipant_service: PartyParticipantService = Depends(get_partyParticipant_service)):
    try:
        participant = await partyParticipant_service.get_party_participant_by_id(id)
        return participant
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    
@router.delete("/{id}", response_model=PartyParticipantDeleteResponse, status_code=status.HTTP_200_OK)
async def delete_party_participant(id: str, partyParticipant_service: PartyParticipantService = Depends(get_partyParticipant_service)):
    try:
        return await partyParticipant_service.delete_party_participant(PartyParticipantDeleteRequest(id=id))
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/{party_id}/all", response_model=list[PartyParticipantResponse], status_code=status.HTTP_200_OK)
async def get_all_participants_in_party(party_id: str, partyParticipant_service: PartyParticipantService = Depends(get_partyParticipant_service)):
    try:
        participants = await partyParticipant_service.get_all_participants_in_party(party_id)
        return participants
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/{user_id}/all", response_model=list[PartyParticipantResponse], status_code=status.HTTP_200_OK)
async def get_all_parties_for_user(user_id: str, partyParticipant_service: PartyParticipantService = Depends(get_partyParticipant_service)):
    try:
        parties = await partyParticipant_service.get_all_parties_for_user(user_id)
        return parties
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))