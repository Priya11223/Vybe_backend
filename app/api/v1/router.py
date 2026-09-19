from fastapi import APIRouter

from app.api.v1.routes import user, party, partyParticipant

router = APIRouter(prefix="/v1")

router.include_router(user.router)
router.include_router(party.router)
router.include_router(partyParticipant.router)

def get_router() -> APIRouter:
    return router