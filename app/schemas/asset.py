from ipaddress import ip_address

from pydantic import BaseModel, ConfigDict, field_validator

from app.core.enums import AssetType, AssetStatus


class AssetBase(BaseModel):
    name: str
    asset_type: AssetType
    ip_address: str
    operating_system: str
    status: AssetStatus = AssetStatus.ACTIVE

    @field_validator("ip_address")
    @classmethod
    def validate_ip_address(cls, value: str) -> str:
        try:
            ip_address(value)
        except ValueError:
            raise ValueError("Invalid IP address")

        return value


class AssetCreate(AssetBase):
    subnet_id: int | None = None


class AssetUpdate(BaseModel):
    name: str | None = None
    asset_type: AssetType | None = None
    ip_address: str | None = None
    operating_system: str | None = None
    status: AssetStatus | None = None
    subnet_id: int | None = None

    @field_validator("ip_address")
    @classmethod
    def validate_ip_address(cls, value: str | None) -> str | None:
        if value is None:
            return value

        try:
            ip_address(value)
        except ValueError:
            raise ValueError("Invalid IP address")

        return value


class AssetResponse(AssetBase):
    id: int
    owner_id: int
    subnet_id: int | None = None

    model_config = ConfigDict(from_attributes=True)


class AssetTopologyResponse(BaseModel):
    id: int
    name: str
    asset_type: AssetType
    ip_address: str
    operating_system: str
    status: AssetStatus

    model_config = ConfigDict(from_attributes=True)