from pydantic import BaseModel, ConfigDict


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