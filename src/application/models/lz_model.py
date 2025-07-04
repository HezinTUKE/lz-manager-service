from __future__ import annotations

import time
import uuid

from sqlalchemy import Enum, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from application.enums.lz_types_enum import LZTypes
from application.models.base import Base


class LZModel(Base):
    __tablename__ = "living_zone"

    lz_id: Mapped[str] = mapped_column(UUID(as_uuid=False), default=lambda: str(uuid.uuid4()), primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    property_type: Mapped[str] = mapped_column(Enum(LZTypes), nullable=False)
    parent_zone_id: Mapped[str] = mapped_column(UUID(as_uuid=False), ForeignKey("living_zone.lz_id"), nullable=True)
    created_at: Mapped[int] = mapped_column(Integer, default=lambda: int(time.time()))
    updated_at: Mapped[int] = mapped_column(Integer, default=lambda: int(time.time()), onupdate=lambda: int(time.time()))

    parent_zone: Mapped["LZModel"] = relationship(back_populates="child_zones", remote_side="LZModel.lz_id")
    child_zones: Mapped[list["LZModel"]] = relationship(back_populates="parent_zone", uselist=True)
    buildings: Mapped[list["BuildingModel"]] = relationship("BuildingModel", back_populates="living_zone", uselist=True)
