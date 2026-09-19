from pydantic import BaseModel, EmailStr, Field, ConfigDict
import uuid

class PartyParticipantCreate(BaseModel):
    party_id: uuid.UUID
    user_id: uuid.UUID
    
class PartyParticipantResponse(BaseModel):
    id: uuid.UUID
    party_id: uuid.UUID
    user_id: uuid.UUID

    model_config = ConfigDict(from_attributes=True)
    
class PartyParticipantDeleteRequest(BaseModel):
    id: uuid.UUID
    
class PartyParticipantDeleteResponse(BaseModel):
    message: str
    
    model_config = ConfigDict(from_attributes=True)