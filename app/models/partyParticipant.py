from app.db.database import Base
from sqlalchemy import (
    Date,
    Enum as SQLEnum,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column
import uuid


class PartyParticipant(Base):
    __tablename__ = "party_participants"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True
    )
    
    party_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("partys.id"),
        nullable=False
    )
    
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    __table_args__ = (
        UniqueConstraint("party_id", "user_id", name="unique_party_user"),
    )