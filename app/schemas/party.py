from pydantic import BaseModel, EmailStr, Field, ConfigDict
import uuid
from datetime import datetime

class PartyCreate(BaseModel):
    description: str
    start_time: str = Field(..., description="Date and time in 'YYYY-MM-DD HH:MM' format")
    end_time: str = Field(..., description="Date and time in 'YYYY-MM-DD HH:MM' format")
    
class PartyResponse(BaseModel):
    id: uuid.UUID
    hosted_by: uuid.UUID
    description: str
    start_time: str = Field(..., description="Date and time in 'YYYY-MM-DD HH:MM' format")
    end_time: str = Field(..., description="Date and time in 'YYYY-MM-DD HH:MM' format")

    model_config = ConfigDict(from_attributes=True)
    
class PartyDeleteRequest(BaseModel):
    id: uuid.UUID
    
class PartyDeleteResponse(BaseModel):
    message: str
    
    model_config = ConfigDict(from_attributes=True)
    
    