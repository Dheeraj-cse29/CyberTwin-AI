from pydantic import BaseModel, ConfigDict


class IncidentCreate(BaseModel):
    title: str
    description: str
    severity: int
    risk_id: int
    detection_id: int
    attack_id: int
    asset_id: int


class IncidentStatusUpdate(BaseModel):
    status: str


class IncidentResponse(BaseModel):
    id: int
    title: str
    description: str
    severity: int
    status: str
    risk_id: int
    detection_id: int
    attack_id: int
    asset_id: int
    owner_id: int

    model_config = ConfigDict(
        from_attributes=True
    )