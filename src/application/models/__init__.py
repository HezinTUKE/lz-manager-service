from sqlalchemy.orm import configure_mappers

from application.models.address_model import AddressModel
from application.models.building_model import BuildingModel
from application.models.lz_model import LZModel

from .address_model import AddressModel
from .base import Base
from .building_model import BuildingModel
from .lz_model import LZModel

configure_mappers()

__all__ = [
    "Base",
    "AddressModel",
    "BuildingModel",
    "LZModel",
]
