from fastapi import FastAPI, Depends

from app.api.v1.router import get_router
from app.db.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI(
    title="Vbye | Party Hosting and searching system"
)

app.include_router(get_router())

@app.get("/")
async def root():
    return {"message": "Hi! Welcome to Vybe"}   