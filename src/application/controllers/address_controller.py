from fastapi import APIRouter

from application.enums.address_status import AddressStatus
from application.handlers.address_handler import AddressHandler
from application.dtos.address_dto import AddressDTO


class AddressController:
    name = "address"
    router = APIRouter()

    @staticmethod
    @router.post(path=f"/{name}/register", tags=[name])
    async def register_new_address(address: AddressDTO):
        await AddressHandler.handle_register_address(address=address)
        return {}

    @staticmethod
    @router.put(path=f"/{name}/change-status", tags=[name])
    async def change_status(address_id: str, status: AddressStatus):
        await AddressHandler.handle_change_address_status(address_id=address_id, status=status)
        return {"result": True}
