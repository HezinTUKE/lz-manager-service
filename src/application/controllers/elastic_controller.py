import asyncio
import logging

from fastapi import APIRouter

from application.enums.elastic_indexes import ElasticIndexes
from application.indexes.address_index import AddressIndex


class ElasticController:
    logger = logging.getLogger("uvicorn.error")

    name = "elastic"
    router = APIRouter()

    INDEX_MAPPER = {ElasticIndexes.ADDRESS_INDEX.value: AddressIndex}

    @staticmethod
    @router.post(path=f"/{name}/create-index", tags=[name])
    async def create_index(index: str):
        try:
            index = ElasticController.INDEX_MAPPER.get(index)
            asyncio.create_task(index.create_index())
            return {"result": True}
        except Exception as ex:
            ElasticController.logger.error(f"Error occurred: {ex}")
            return {"result": False}
