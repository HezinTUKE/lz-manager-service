import logging

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from application.enums.address_status import AddressStatus
from application.models.address_model import AddressModel
from application.models.base import with_session
from application.dtos.address_dto import AddressDTO, AddressBaseDTO


class AddressHandler:
    logger = logging.getLogger("uvicorn.error")

    @classmethod
    @with_session(retries=3)
    async def handle_register_address(cls, address: AddressDTO, session: AsyncSession):
        address = AddressBaseDTO(**address.model_dump())

        _query = (
            select(AddressModel)
            .where(
                AddressModel.state == address.state,
                AddressModel.name == address.name,
                AddressModel.living_zone_type == address.lz_type,
                AddressModel.street == address.street,
                AddressModel.district == address.district,
                AddressModel.postal_code == address.postal_code,
            )
            .limit(1)
            .offset(0)
        )
        _query_result = await session.execute(_query)
        records = _query_result.first()

        if records:
            cls.logger.info("Address exists")
            return False

        new_record = AddressModel(**address.model_dump(by_alias=True))
        session.add(new_record)

        return True

    @classmethod
    @with_session(retries=1)
    async def handle_change_address_status(cls, address_id: str, status: AddressStatus, session: AsyncSession):
        stmt = update(AddressModel).where(AddressModel.address_id == address_id).values(status=status)

        await session.execute(stmt)
        await session.commit()
        return True
