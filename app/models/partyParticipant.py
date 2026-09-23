from app.db.database import Base
from datetime import datetime
from sqlalchemy import DateTime, Enum as SQLEnum, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid
from enum import Enum

class PartyParticipantRole(str, Enum):
    HOST = "host"
    CO_HOST = "co_host"
    MEMBER = "member"
    
class PartyParticipantStatus(str, Enum):
    INVITED = "invited"
    CONFIRMED = "confirmed"
    ATTENDED = "attended"
    LEFT = "left"
    REMOVED = "removed"


class PartyParticipant(Base):
    __tablename__ = "party_participant"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )
    
    party_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("party.id"),
        nullable=False
    )
    
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("user.id"),
        nullable=False
    )
    
    role: Mapped[PartyParticipantRole] = mapped_column(SQLEnum(PartyParticipantRole), nullable=False, default=PartyParticipantRole.MEMBER)

    status: Mapped[PartyParticipantStatus] = mapped_column(SQLEnum(PartyParticipantStatus), nullable=False, default=PartyParticipantStatus.INVITED)
    joined_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    left_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    party: Mapped["Party"] = relationship(back_populates="participants")
    user: Mapped["User"] = relationship(back_populates="party_participations")

    __table_args__ = (
        UniqueConstraint("party_id", "user_id", name="unique_party_user"),
    )