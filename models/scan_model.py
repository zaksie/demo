import datetime
from sqlite3 import Timestamp

from pydantic import BaseModel


class ScanModel(BaseModel):
    id: int = -1
    start: Timestamp = datetime.datetime.now()
    finish: Timestamp = None
