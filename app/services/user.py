import uuid
from fastapi import status
from app.repositories.user import UserRepository
from app.schemas.user import *
from fastapi import HTTPException
from app.models.user import User

class UserService:
    def __init__(self, userRepo: UserRepository):
        self.userRepo = userRepo
        
    async def create_user(self, user: UserCreate) -> UserResponse:
        temp_user = await self.userRepo.get_by_email(user.email)
        if temp_user:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
        
        new_user = User(name=user.name, email=user.email, username=user.username, hashed_password=user.password)
        return await self.userRepo.create(new_user)

    async def get_user_by_email(self, email: str) -> UserResponse:
        return await self.userRepo.get_by_email(email)

    async def get_user_by_id(self, user_id: uuid.UUID) -> UserResponse:
        return await self.userRepo.get_by_id(user_id)

    async def update_user(self, user: UserUpdate) -> UserResponse:
        existing_user = await self.userRepo.get_by_id(user.id)
        if not existing_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        temp_user = await self.userRepo.get_by_email(user.email)
        if temp_user and temp_user.id != user.id:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists with this email")
        
        temp_user_2 = await self.userRepo.get_by_username(user.username)
        if temp_user_2 and temp_user_2.id != user.id:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists with this username")
        return await self.userRepo.update(user)


    async def delete_user(self, user: UserDeleteRequest) -> UserDeleteResponse:
        existing = await self.userRepo.get_by_id(user.id)
        if not existing:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        await self.userRepo.delete(existing)
        return UserDeleteResponse(message="User deleted successfully")