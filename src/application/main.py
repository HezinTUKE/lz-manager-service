from fastapi import FastAPI

from application.controllers.address_controller import AddressController
from application.controllers.elastic_controller import ElasticController
from application.controllers.lz_controller import LZController

app = FastAPI()

app.include_router(LZController.router)
app.include_router(AddressController.router)
app.include_router(ElasticController.router)
