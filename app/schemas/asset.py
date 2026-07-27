from pydantic import BaseModel
from typing import Optional

from app.core.enums import AssetType, AssetStatus


class AssetCreate(BaseModel):

    name: str

    asset_type: AssetType

    ip_address: str

    operating_system: str

    status: Optional[AssetStatus] = AssetStatus.ACTIVE


class AssetResponse(BaseModel):

    id: int

    name: str

    asset_type: AssetType

    ip_address: str

    operating_system: str

    status: AssetStatus

    class Config:
        from_attributes = True