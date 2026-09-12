from pydantic import BaseModel, ConfigDict


class DetectionResponse(BaseModel):
    id: int
    attack_id: int
    asset_id: int
    detected: bool
    severity: int
    threat_level: str
    reason: str
    owner_id: int

    model_config = ConfigDict(
        from_attributes=True
    )