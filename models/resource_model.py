from pydantic import BaseModel


class ResourceModel(BaseModel):
    urn: str
    scan_id: int
    name: str
    type: str
    data: str
