from pydantic import BaseModel, EmailStr, Field, ConfigDict
import uuid

class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8, max_length=255)
    username: str = Field(min_length=1, max_length=50)
    

class UserResponse(BaseModel):
    id: uuid.UUID
    name: str
    email: EmailStr
    username: str

    model_config = ConfigDict(from_attributes=True)
    
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=255)
    
class UserUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    email: EmailStr | None = Field(default=None)
    password: str | None = Field(default=None, min_length=8, max_length=255)
    username: str | None = Field(default=None, min_length=1, max_length=50)
    
class UserUpdateResponse(BaseModel):
    id: uuid.UUID
    name: str | None
    email: EmailStr | None
    username: str | None

    model_config = ConfigDict(from_attributes=True)
    
class UserDeleteRequest(BaseModel):
    id: uuid.UUID
    
class UserDeleteResponse(BaseModel):
    message: str
    
    model_config = ConfigDict(from_attributes=True)
    