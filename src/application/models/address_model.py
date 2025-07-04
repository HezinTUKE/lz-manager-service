import time
import uuid

from sqlalchemy import UUID, Enum, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from application.enums.address_status import AddressStatus
from application.enums.lz_types_enum import LZAddressTypes
from application.models.base import Base


class AddressModel(Base):
    __tablename__ = "address"

    address_id: Mapped[str] = mapped_column(UUID(as_uuid=False), default=lambda: str(uuid.uuid4()), primary_key=True)
    status: Mapped[AddressStatus] = mapped_column(Enum(AddressStatus), nullable=False, default=AddressStatus.PENDING)
    state: Mapped[str] = mapped_column(String, nullable=False, index=True)
    living_zone_type: Mapped[LZAddressTypes] = mapped_column(Enum(LZAddressTypes), nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    street: Mapped[str] = mapped_column(String, nullable=False, index=True)
    district: Mapped[str] = mapped_column(String, nullable=True, index=True)
    postal_code: Mapped[str] = mapped_column(String, nullable=False, index=True)
    extras: Mapped[dict] = mapped_column(JSONB, default={})
    created_at: Mapped[int] = mapped_column(Integer, default=lambda: int(time.time()))
    updated_at: Mapped[int] = mapped_column(Integer, default=lambda: int(time.time()), onupdate=lambda: int(time.time()))

    building: Mapped[list["BuildingModel"]] = relationship("BuildingModel", back_populates="address", uselist=True)
