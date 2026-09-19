from fastapi import APIRouter

from app.api.v1.routes import user, party

router = APIRouter(prefix="/v1")

router.include_router(user.router)
router.include_router(party.router)

def get_router() -> APIRouter:
    return router