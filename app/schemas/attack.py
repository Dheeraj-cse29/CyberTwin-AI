from ipaddress import ip_address

from pydantic import BaseModel, ConfigDict, field_validator

from app.core.enums import AttackType, AttackStatus


class AttackCreate(BaseModel):
    attack_type: AttackType
    source_ip: str
    target_asset_id: int
    severity: int = 1
    description: str | None = None

    @field_validator("source_ip")
    @classmethod
    def validate_source_ip(cls, value: str) -> str:
        try:
            ip_address(value)
        except ValueError:
            raise ValueError("Invalid source IP address")

        return value


class AttackResponse(BaseModel):
    id: int
    attack_type: AttackType
    source_ip: str
    target_asset_id: int
    status: AttackStatus
    severity: int
    description: str | None
    owner_id: int

    model_config = ConfigDict(
        from_attributes=True
    )