
from dbs.generic_db import GenericDB
from models.scan_model import ScanModel


class Scan:
    def __init__(self, db: GenericDB):
        self.db = db

    def create(self):
        scan_model = ScanModel()
        self.db.insert_scan(scan_model)

    def get_all(self):
        try:
            return self.db.get_all_scans()
        except e:
            print(e)
            raise e