from datetime import date, datetime
from enum import Enum
import uuid
from typing import TYPE_CHECKING

from app.db.database import Base
from sqlalchemy import Date, DateTime, ForeignKey, String, Text, Boolean, Enum as SQLEnum, func
from sqlalchemy.orm import Mapped, mapped_column, relationship, synonym

if TYPE_CHECKING:
    from app.models.party import Party
    from app.models.partyParticipant import PartyParticipant
    from app.models.partyRequest import PartyRequest


class AuthProvider(str, Enum):
    LOCAL = "local"
    GOOGLE = "google"
    APPLE = "apple"


class UserStatus(str, Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"
    DELETED = "deleted"

class User(Base):
    __tablename__ = "user"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )
    
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True, 
        nullable=False
    )
    phone_number: Mapped[str | None] = mapped_column(String(20), unique=True)
    password_hash: Mapped[str | None] = mapped_column(String(255))
    auth_provider: Mapped[AuthProvider] = mapped_column(SQLEnum(AuthProvider), default=AuthProvider.LOCAL, nullable=False)
    provider_user_id: Mapped[str | None] = mapped_column(String(255))
    is_email_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_phone_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    status: Mapped[UserStatus] = mapped_column(SQLEnum(UserStatus), default=UserStatus.ACTIVE, nullable=False)
    last_login_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    # Legacy API fields retained while the API migrates to the profile model.
    name: Mapped[str | None] = mapped_column(String(100))
    username: Mapped[str | None] = mapped_column(String(50), unique=True)
    hashed_password = synonym("password_hash")

    profile: Mapped["UserProfile | None"] = relationship(back_populates="user", uselist=False)
    parties: Mapped[list["Party"]] = relationship(back_populates="host")
    party_participations: Mapped[list["PartyParticipant"]] = relationship(back_populates="user")
    party_requests: Mapped[list["PartyRequest"]] = relationship(
        back_populates="user", foreign_keys="PartyRequest.user_id"
    )
    
    
    
class UserProfile(Base):
    __tablename__ = "user_profile"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )
    
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str | None] = mapped_column(String(100))
    date_of_birth: Mapped[date | None] = mapped_column(Date)
    gender: Mapped[str | None] = mapped_column(String(50))
    bio: Mapped[str | None] = mapped_column(Text)
    profile_image_url: Mapped[str | None] = mapped_column(String(500))
    city: Mapped[str | None] = mapped_column(String(100))
    occupation: Mapped[str | None] = mapped_column(String(150))
    relationship_status: Mapped[str | None] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    user: Mapped[User] = relationship(back_populates="profile")