from fastapi import APIRouter

from application.schemas.request_schemas.new_zone_schema import NewZoneSchema
from application.schemas.response_schemas.default_response_schema import \
    ResponseSchema


class LZController:
    router = APIRouter()

    @staticmethod
    @router.get("/list")
    async def get_list():
        return {"message": "list"}

    @staticmethod
    @router.post(path="/name", response_model=ResponseSchema)
    async def create_model(new_zone: NewZoneSchema):
        return {"result": True}
