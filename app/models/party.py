from datetime import datetime
from app.db.database import Base
from sqlalchemy import (
    Date,
    Enum as SQLEnum,
    ForeignKey,
    UniqueConstraint,
    DateTime
)
from sqlalchemy.orm import Mapped, mapped_column
import uuid

class Party(Base):
    __tablename__ = "party"    

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )
    
    hosted_by: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("user.id"),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        nullable=False
    )
    start_time: Mapped[str] = mapped_column(
        nullable=False
    )
    end_time: Mapped[str] = mapped_column(
        nullable=False
    )