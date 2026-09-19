from app.db.database import Base
from sqlalchemy import (
    Date,
    Enum as SQLEnum,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column
import uuid

class Party(Base):
    __tablename__ = "partys"    

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True
    )
    
    hosted_by: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )
    
    
    
    