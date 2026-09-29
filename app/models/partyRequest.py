from datetime import datetime
from enum import Enum
import uuid

from app.db.database import Base
from sqlalchemy import DateTime, Enum as SQLEnum, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship


class PartyRequestStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    CANCELLED = "cancelled"


class PartyRequest(Base):
    __tablename__ = "party_request"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    party_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("party.id", ondelete="CASCADE"), nullable=False)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    message: Mapped[str | None] = mapped_column(Text)
    status: Mapped[PartyRequestStatus] = mapped_column(SQLEnum(PartyRequestStatus), default=PartyRequestStatus.PENDING, nullable=False)
    reviewed_by: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("user.id"))
    reviewed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    party: Mapped["Party"] = relationship(back_populates="requests")
    user: Mapped["User"] = relationship(back_populates="party_requests", foreign_keys=[user_id])
    reviewer: Mapped["User | None"] = relationship(foreign_keys=[reviewed_by])