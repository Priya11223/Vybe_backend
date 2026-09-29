from app.api.dependencies import get_auth_service
from app.services.auth import AuthService
from app.schemas.user import *
from fastapi import APIRouter, Depends, status
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserLogin

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", status_code=status.HTTP_200_OK)
async def login(
    user_login: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(get_auth_service)
):
    try:
        new_login = UserLogin(email=user_login.username, password=user_login.password)
        token =  await auth_service.login(new_login)
        return {
            "access_token": token,
            "token_type": "bearer"
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    