
from dbs.generic_db import GenericDB
from models.scan_model import ScanModel


class Scan:
    def __init__(self, db: GenericDB):
        self.db = db

    def create(self):
        scan_model = ScanModel()
        self.db.insert_scan(scan_model)

    def get_all(self, page_index: int = 0, page_size: int = 10):
        try:
            return self.db.get_all_scans(page_index, page_size)
        except e:
            print(e)
            raise e