from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.database import get_db
from app.models.user import User

from app.schemas.detection import DetectionResponse

from app.services.detection_service import DetectionService


router = APIRouter(
    prefix="/detections",
    tags=["Detection Engine"],
)


@router.get(
    "/",
    response_model=list[DetectionResponse],
)
def get_detections(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return DetectionService.get_detections(
        db=db,
        owner_id=current_user.id,
    )


@router.get(
    "/attack/{attack_id}",
    response_model=list[DetectionResponse],
)
def get_attack_detections(
    attack_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return DetectionService.get_attack_detections(
        db=db,
        attack_id=attack_id,
        owner_id=current_user.id,
    )