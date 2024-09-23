from typing import Optional

from dbs.generic_db import GenericDB
from models.resource_model import ResourceModel


class Resource:
    def __init__(self, db: GenericDB):
        self.db = db
        self.resource_types = db.get_resource_types()

    def create(self, resource_model: ResourceModel):
        self.db.insert_resource(resource_model)

    def get_all(self, type: Optional[str] = None, scan_id: Optional[int] = None):
        if type is None and scan_id is None:
            raise Exception('Missing at least one parameter')
        return self.db.get_all_resources(type, scan_id)
