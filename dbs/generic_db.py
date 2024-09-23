from typing import Optional

from models.resource_model import ResourceModel
from models.scan_model import ScanModel
from abc import ABC, abstractmethod


class GenericDB(ABC):
    def __init__(self):
        self.conn = None
        self.connect()

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def insert_scan(self, scan: ScanModel):
        pass

    @abstractmethod
    def insert_resource(self, resource: ResourceModel):
        pass

    @abstractmethod
    def get_all_scans(self):
        pass

    @abstractmethod
    def get_all_resources(self, type: Optional[str] = None, scan_id: Optional[int] = None):
        pass

    @abstractmethod
    def get_resource_types(self):
        pass
