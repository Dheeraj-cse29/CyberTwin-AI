from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.exceptions.custom_exceptions import ResourceNotFoundException
from app.auth.dependencies import get_current_user
from app.database.database import get_db
from app.models.user import User
from app.schemas.asset import (
    AssetCreate,
    AssetResponse,
    AssetUpdate,
    AssetTopologyResponse,
)
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


@router.get(
    "/{asset_id}/topology",
    response_model=AssetTopologyResponse
)
def get_asset_topology(
    asset_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    asset = AssetService.get_asset_topology(
        db=db,
        asset_id=asset_id,
        owner_id=current_user.id
    )

    if asset is None:
        raise ResourceNotFoundException(
            "Asset does not exist."
        )

    return asset


@router.put("/{asset_id}", response_model=AssetResponse)
def update_asset(
    asset_id: int,
    asset: AssetUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    updated_asset = AssetService.update_asset(
        db=db,
        asset_id=asset_id,
        asset_data=asset,
        owner_id=current_user.id
    )

    if updated_asset is None:
        raise ResourceNotFoundException(
            "Asset does not exist."
        )

    return updated_asset


@router.delete("/{asset_id}")
def delete_asset(
    asset_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    deleted = AssetService.delete_asset(
        db=db,
        asset_id=asset_id,
        owner_id=current_user.id
    )

    if not deleted:
        raise ResourceNotFoundException(
            "Asset does not exist."
        )

    return {
        "message": "Asset deleted successfully"
    }


@router.get("/test-error")
def test_error():
    raise ResourceNotFoundException(
        "Asset does not exist."
    )