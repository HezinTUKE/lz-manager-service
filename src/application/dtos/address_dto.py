import time
import uuid

from pydantic import BaseModel, Field

from application.enums.address_status import AddressStatus
from application.enums.lz_types_enum import LZAddressTypes


class AddressDTO(BaseModel):
    state: str = ""
    living_zone_type: LZAddressTypes | None = None
    name: str = ""
    street: str = ""
    district: str = ""
    postal_code: str = ""


class AddressBaseDTO(AddressDTO):
    address_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    status: AddressStatus = Field(default=AddressStatus.PENDING)
    extras: dict = Field(default_factory=dict)
    created_at: int = Field(default_factory=lambda: int(time.time()))
    updated_at: int = Field(default_factory=lambda: int(time.time()))
