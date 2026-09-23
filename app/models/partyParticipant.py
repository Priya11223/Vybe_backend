from app.db.database import Base
from sqlalchemy import (
    Date,
    Enum as SQLEnum,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column
import uuid
from enum import Enum

class PartyParticipantRole(str, Enum):
    HOST = "host"
    GUEST = "guest"
    
class Status(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    DECLINED = "declined"
    WITHDRAWN = "withdrawn"


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
    
    role: Mapped[PartyParticipantRole] = mapped_column(
        SQLEnum(PartyParticipantRole),
        nullable=False,
        default=PartyParticipantRole.GUEST
    )

    status: Mapped[Status] = mapped_column(
        SQLEnum(Status),
        nullable=False,
        default=Status.PENDING
    )

    __table_args__ = (
        UniqueConstraint("party_id", "user_id", name="unique_party_user"),
    )