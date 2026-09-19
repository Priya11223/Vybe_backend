from fastapi import APIRouter

from app.api.v1.routes import user

router = APIRouter(prefix="/v1")

router.include_router(user.router)

def get_router() -> APIRouter:
    return router