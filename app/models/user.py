from app.db.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
import uuid

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True
    )
    
    name: Mapped[str] = mapped_column(
        String(100), 
        nullable=False
    )
    
    hashed_password: Mapped[str] = mapped_column(
        String(255), 
        nullable=False
    
    )
    
    email: Mapped[str] = mapped_column(
        String(100), 
        unique=True, 
        nullable=False
    
    )
    
    username: Mapped[str] = mapped_column(
        String(50), 
        unique=True,
        nullable=False
    )