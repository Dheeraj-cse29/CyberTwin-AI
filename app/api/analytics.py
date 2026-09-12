from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.database import get_db
from app.models.user import User

from app.analytics.analytics_service import AnalyticsService


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get("/summary")
def get_security_summary(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return AnalyticsService.get_security_summary(
        db=db,
        owner_id=current_user.id,
    )