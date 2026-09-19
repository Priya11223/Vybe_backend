from pydantic import BaseModel, EmailStr, Field, ConfigDict
import uuid

class PartyCreate(BaseModel):
    hosted_by: uuid.UUID
    
class PartyResponse(BaseModel):
    id: uuid.UUID
    hosted_by: uuid.UUID

    model_config = ConfigDict(from_attributes=True)
    
class PartyDeleteRequest(BaseModel):
    id: uuid.UUID
    
class PartyDeleteResponse(BaseModel):
    message: str
    
    model_config = ConfigDict(from_attributes=True)
    
    