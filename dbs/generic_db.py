from typing import Optional

from models.resource_model import ResourceModel
from models.scan_model import ScanModel
from abc import ABC, abstractmethod


class GenericDB(ABC):
    def __init__(self):
        self.conn = None
        self.init()

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def insert_scan(self, scan: ScanModel):
        pass

    @abstractmethod
    def insert_resource(self, resource: ResourceModel):
        pass

    @abstractmethod
    def get_all_scans(self, page_index: int = 0, page_size: int= 10):
        pass

    @abstractmethod
    def get_all_resources(self, type: Optional[str] = None, scan_id: Optional[int] = None, page_index: int = 0, page_size: int= 10):
        pass

    @abstractmethod
    def get_resource_types(self):
        pass
