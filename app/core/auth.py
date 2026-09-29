from app.repositories.user import UserRepository
from fastapi import Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordBearer
from app.api.dependencies import get_user_repo
from app.core.config import get_settings
import jwt
from jwt.exceptions import PyJWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/auth/login")
settings = get_settings()

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    repository: UserRepository = Depends(get_user_repo)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except PyJWTError:
        raise credentials_exception

    user = await repository.get_by_id(user_id)
    if user is None:
        raise credentials_exception

    return user
    
    