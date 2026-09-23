from datetime import datetime
from enum import Enum
import uuid
from typing import TYPE_CHECKING

from app.db.database import Base
from sqlalchemy import Boolean, DateTime, Enum as SQLEnum, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship, synonym

if TYPE_CHECKING:
    from app.models.partyCategory import PartyCategory
    from app.models.partyLocation import PartyLocation
    from app.models.partyParticipant import PartyParticipant
    from app.models.partyRequest import PartyRequest
    from app.models.partyRequirement import PartyRequirement
    from app.models.partyRule import PartyRule
    from app.models.partyType import PartyType
    from app.models.user import User


class PartyStatus(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    ONGOING = "ongoing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class PartyVisibility(str, Enum):
    PUBLIC = "public"
    PRIVATE = "private"
    INVITE_ONLY = "invite_only"

class Party(Base):
    __tablename__ = "party"    

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )
    
    host_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("user.id"),
        nullable=False
    )
    party_type_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("party_type.id"), nullable=False)
    party_category_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("party_category.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    start_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    end_time: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    max_participants: Mapped[int] = mapped_column(Integer, nullable=False)
    is_alcohol_allowed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    alcohol_provided_by_host: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    food_provided_by_host: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    drinks_provided_by_host: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    status: Mapped[PartyStatus] = mapped_column(SQLEnum(PartyStatus), default=PartyStatus.DRAFT, nullable=False)
    visibility: Mapped[PartyVisibility] = mapped_column(SQLEnum(PartyVisibility), default=PartyVisibility.PUBLIC, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    cancelled_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    hosted_by = synonym("host_id")
    host: Mapped["User"] = relationship(back_populates="parties")
    party_type: Mapped["PartyType"] = relationship(back_populates="parties")
    party_category: Mapped["PartyCategory"] = relationship(back_populates="parties")
    location: Mapped["PartyLocation | None"] = relationship(back_populates="party", uselist=False)
    rules: Mapped[list["PartyRule"]] = relationship(back_populates="party", cascade="all, delete-orphan")
    requirements: Mapped[list["PartyRequirement"]] = relationship(back_populates="party", cascade="all, delete-orphan")
    participants: Mapped[list["PartyParticipant"]] = relationship(back_populates="party", cascade="all, delete-orphan")
    requests: Mapped[list["PartyRequest"]] = relationship(back_populates="party", cascade="all, delete-orphan")
    


