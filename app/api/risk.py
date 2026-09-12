from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.database import get_db
from app.models.user import User

from app.schemas.risk import RiskResponse

from app.services.risk_service import RiskService


router = APIRouter(
    prefix="/risks",
    tags=["Risk Engine"],
)


@router.get(
    "/",
    response_model=list[RiskResponse],
)
def get_risks(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return RiskService.get_risks(
        db=db,
        owner_id=current_user.id,
    )


@router.get(
    "/detection/{detection_id}",
    response_model=list[RiskResponse],
)
def get_detection_risks(
    detection_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return RiskService.get_detection_risks(
        db=db,
        detection_id=detection_id,
        owner_id=current_user.id,
    )