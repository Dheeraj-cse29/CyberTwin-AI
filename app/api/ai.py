from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.database import get_db
from app.models.user import User

from app.ai.security_analyzer import SecurityAnalyzer


router = APIRouter(
    prefix="/ai",
    tags=["AI Security Analysis"],
)


@router.get("/analyze")
def analyze_security(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return SecurityAnalyzer.analyze(
        db=db,
        owner_id=current_user.id,
    )