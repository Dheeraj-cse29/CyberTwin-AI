from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.database import get_db
from app.models.user import User

from app.threat_hunting.hunter import ThreatHunter


router = APIRouter(
    prefix="/threat-hunting",
    tags=["Threat Hunting"],
)


@router.get("/")
def hunt_threats(
    threat_level: str | None = None,
    attack_type: str | None = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return ThreatHunter.hunt(
        db=db,
        owner_id=current_user.id,
        threat_level=threat_level,
        attack_type=attack_type,
    )