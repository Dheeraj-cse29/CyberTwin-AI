from pydantic import BaseModel, ConfigDict

from app.schemas.asset import AssetTopologyResponse


class SubnetBase(BaseModel):
    name: str
    cidr_block: str


class SubnetCreate(SubnetBase):
    network_id: int


class SubnetUpdate(BaseModel):
    name: str | None = None
    cidr_block: str | None = None


class SubnetResponse(SubnetBase):
    id: int
    network_id: int

    model_config = ConfigDict(from_attributes=True)


class SubnetTopologyResponse(SubnetBase):
    id: int
    assets: list["AssetTopologyResponse"] = []

    model_config = ConfigDict(from_attributes=True)