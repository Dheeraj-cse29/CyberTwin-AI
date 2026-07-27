from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.exceptions.custom_exceptions import ResourceNotFoundException

from app.auth.dependencies import get_current_user
from app.database.database import get_db
from app.models.user import User
from app.schemas.asset import AssetCreate, AssetResponse
from app.services.asset_service import AssetService

router = APIRouter(
    prefix="/assets",
    tags=["Assets"]
)


@router.post("/", response_model=AssetResponse)
def create_asset(
    asset: AssetCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return AssetService.create_asset(
        db=db,
        asset_data=asset,
        owner_id=current_user.id
    )


@router.get("/", response_model=list[AssetResponse])
def get_assets(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return AssetService.get_assets(
        db=db,
        owner_id=current_user.id
    )
@router.get("/test-error")
def test_error():
    raise ResourceNotFoundException(
        "Asset does not exist."
    )