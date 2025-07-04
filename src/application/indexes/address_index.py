from application.enums.elastic_indexes import ElasticIndexes
from application.indexes import BaseIndex


class AddressIndex(BaseIndex):
    index = ElasticIndexes.ADDRESS_INDEX.value
    __mapping__ = {
        "mappings": {
            "properties": {
                "address_id": {"type": "keyword"},
                "status": {"type": "keyword"},
                "state": {"type": "text", "fields": {"raw": {"type": "keyword"}}},
                "living_zone_type": {"type": "keyword", "null_value": "null"},
                "name": {"type": "text", "fields": {"raw": {"type": "keyword"}}},
                "street": {"type": "text", "fields": {"raw": {"type": "keyword"}}},
                "district": {"type": "text", "fields": {"raw": {"type": "keyword"}}},
                "postal_code": {"type": "keyword"},
                "extras": {"type": "object", "dynamic": True},
                "created_at": {"type": "date", "format": "epoch_second"},
                "updated_at": {"type": "date", "format": "epoch_second"},
            }
        }
    }
