from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.subnet import (
    SubnetCreate,
    SubnetUpdate,
    SubnetResponse,
)
from app.services.subnet_service import SubnetService
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/subnets",
    tags=["Subnets"],
)

service = SubnetService()


@router.post("/", response_model=SubnetResponse)
def create_subnet(
    subnet: SubnetCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.create_subnet(
        db,
        subnet,
    )


@router.get("/", response_model=list[SubnetResponse])
def get_all_subnets(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.get_all_subnets(db)


@router.get("/{subnet_id}", response_model=SubnetResponse)
def get_subnet(
    subnet_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.get_subnet(
        db,
        subnet_id,
    )


@router.put("/{subnet_id}", response_model=SubnetResponse)
def update_subnet(
    subnet_id: int,
    subnet: SubnetUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.update_subnet(
        db,
        subnet_id,
        subnet,
    )


@router.delete("/{subnet_id}")
def delete_subnet(
    subnet_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.delete_subnet(
        db,
        subnet_id,
    )