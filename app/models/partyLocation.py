from datetime import datetime
from enum import Enum
import uuid
from typing import TYPE_CHECKING

from app.db.database import Base
from sqlalchemy import DateTime, Enum as SQLEnum, ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.party import Party


class LocationVisibility(str, Enum):
    EXACT = "exact"
    APPROXIMATE = "approximate"
    HIDDEN = "hidden"


class PartyLocation(Base):
    __tablename__ = "party_location"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    party_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("party.id", ondelete="CASCADE"), unique=True, nullable=False)
    address_line_1: Mapped[str | None] = mapped_column(String(255))
    address_line_2: Mapped[str | None] = mapped_column(String(255))
    city: Mapped[str | None] = mapped_column(String(100))
    state: Mapped[str | None] = mapped_column(String(100))
    country: Mapped[str | None] = mapped_column(String(100))
    postal_code: Mapped[str | None] = mapped_column(String(20))
    latitude: Mapped[float | None] = mapped_column(Numeric(9, 6))
    longitude: Mapped[float | None] = mapped_column(Numeric(9, 6))
    location_visibility: Mapped[LocationVisibility] = mapped_column(
        SQLEnum(LocationVisibility), default=LocationVisibility.APPROXIMATE, nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    party: Mapped["Party"] = relationship(back_populates="location")