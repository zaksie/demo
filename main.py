from typing import Optional

from fastapi import FastAPI, Response, status

from dbs.postgres_db import PostgresDB
from entities.resource import Resource
from entities.scan import Scan
from models.resource_model import ResourceModel

app = FastAPI()
db = PostgresDB()
resource = Resource(db)
scan = Scan(db)


@app.post("/api/v1/scan")
async def create_scan(response: Response):
    try:
        scan.create()
    except e:
        response.status_code = status.HTTP_400_BAD_REQUEST
    return ''


@app.get("/api/v1/scan")
async def get_scans():
    return scan.get_all()

@app.post("/api/v1/resource")
async def create_resource(resource_model: ResourceModel, response: Response):
    try:
        resource.create(resource_model)
    except:
        response.status_code = status.HTTP_400_BAD_REQUEST
    return ''

@app.get("/api/v1/resource")
async def get_resource(type: Optional[str] = None, scan_id: Optional[int] = None):
    return resource.get_all(type, scan_id)


scan.create()
