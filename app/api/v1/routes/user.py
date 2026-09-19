from fastapi import APIRouter, Depends, HTTPException, status
from app.services.user import UserService
from app.api.dependencies import get_user_service
from app.schemas.user import *

router = APIRouter(prefix="/users", tags=["User"])

@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, user_service: UserService = Depends(get_user_service)):
    return await user_service.create_user(user)

@router.get("/id/{id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def get_user_by_id(id: str, user_service: UserService = Depends(get_user_service)):
    try:
        user = await user_service.get_user_by_id(id)
        return user
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.patch("/{id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def update_user(id: str, user: UserUpdate, user_service: UserService = Depends(get_user_service)):
    try:
        user.id = id
        return await user_service.update_user(user)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.delete("/{id}", response_model=UserDeleteResponse, status_code=status.HTTP_200_OK)
async def delete_user(id: str, user_service: UserService = Depends(get_user_service)):
    try:
        return await user_service.delete_user(UserDeleteRequest(id=id))
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))