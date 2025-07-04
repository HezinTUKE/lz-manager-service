import time
import uuid

from sqlalchemy import UUID, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from application.enums.building_type import BuildingType
from application.models.base import Base


class BuildingModel(Base):
    __tablename__ = "building"

    building_id: Mapped[str] = mapped_column(UUID(as_uuid=False), default=lambda: str(uuid.uuid4()), primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)
    lz_id: Mapped[str] = mapped_column(UUID(as_uuid=False), ForeignKey("living_zone.lz_id"), nullable=True)
    address_id: Mapped[str] = mapped_column(UUID(as_uuid=False), ForeignKey("address.address_id"), nullable=False)
    building_type: Mapped[str] = mapped_column(
        Enum(BuildingType),
        nullable=False,
    )
    created_at: Mapped[int] = mapped_column(Integer, default=lambda: int(time.time()))
    updated_at: Mapped[int] = mapped_column(Integer, default=lambda: int(time.time()), onupdate=lambda: int(time.time()))

    living_zone: Mapped["LZModel"] = relationship("LZModel", back_populates="buildings")
    address: Mapped["AddressModel"] = relationship("AddressModel", back_populates="building")
