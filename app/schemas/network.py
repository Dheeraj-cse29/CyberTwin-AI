from pydantic import BaseModel, ConfigDict

from app.schemas.subnet import SubnetTopologyResponse


class NetworkBase(BaseModel):
    name: str
    description: str | None = None


class NetworkCreate(NetworkBase):
    pass


class NetworkUpdate(BaseModel):
    name: str | None = None
    description: str | None = None


class NetworkResponse(NetworkBase):
    id: int
    owner_id: int

    model_config = ConfigDict(from_attributes=True)


class NetworkTopologyResponse(NetworkBase):
    id: int
    subnets: list[SubnetTopologyResponse] = []

    model_config = ConfigDict(from_attributes=True)