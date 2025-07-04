from pydantic import BaseModel, Field

from application.enums.lz_types_enum import LZTypes


class NewZoneSchema(BaseModel):
    name: str = ""
    zone_type: LZTypes = Field(LZTypes.CITY.value)
