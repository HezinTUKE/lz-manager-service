from elasticsearch import Elasticsearch


class BaseIndex:
    index = ""
    __mapping__ = {}

    @classmethod
    async def get_client(cls):
        return Elasticsearch("http://localhost:9200")

    @classmethod
    async def create_index(cls):
        client = await cls.get_client()
        client.indices.create(index=cls.index, mappings=cls.__mapping__)
