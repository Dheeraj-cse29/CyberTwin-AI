from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.database import get_db
from app.models.user import User

from app.digital_twin.twin_engine import DigitalTwinEngine


router = APIRouter(
    prefix="/digital-twin",
    tags=["Digital Twin"],
)


@router.get("/state")
def get_environment_state(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return DigitalTwinEngine.get_environment_state(
        db=db,
        owner_id=current_user.id,
    )