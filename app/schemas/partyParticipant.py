from pydantic import BaseModel, EmailStr, Field, ConfigDict
import uuid
from app.models.partyParticipant import PartyParticipantRole

class PartyParticipantCreate(BaseModel):
    party_id: uuid.UUID
    user_id: uuid.UUID
    role: PartyParticipantRole    
class PartyParticipantResponse(BaseModel):
    id: uuid.UUID
    party_id: uuid.UUID
    user_id: uuid.UUID
    role: PartyParticipantRole

    model_config = ConfigDict(from_attributes=True)
    
class PartyParticipantDeleteRequest(BaseModel):
    id: uuid.UUID

class PartyParticipantDeleteResponse(BaseModel):
    message: str
    
    model_config = ConfigDict(from_attributes=True)