from datetime import timedelta
from datetime import datetime
import jwt
from pwdlib import PasswordHash
from app.core.config import get_settings

settings = get_settings()

password_hash = PasswordHash.recommended()
    
def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(password: str, hash: str) -> bool:
    return password_hash.verify(password, hash)

def create_jwt_token(user_id: int) -> str:
    payload = {
        "sub": str(user_id),
        "exp": datetime.now() + timedelta(hours=1)
    }
    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)