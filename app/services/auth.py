from app.schemas.user import UserLogin
from app.repositories.user import UserRepository
from app.core.security import verify_password, create_jwt_token
from fastapi import HTTPException, status


class AuthService():
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def login(self, user_login: UserLogin):
        user = await self.user_repo.get_by_email(user_login.email)
        
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

        if not verify_password(user_login.password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

        return create_jwt_token(user.id)