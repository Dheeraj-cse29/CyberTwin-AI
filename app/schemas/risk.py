from pydantic import BaseModel, ConfigDict


class RiskResponse(BaseModel):
    id: int
    detection_id: int
    attack_id: int
    asset_id: int
    risk_score: float
    risk_level: str
    owner_id: int

    model_config = ConfigDict(
        from_attributes=True
    )