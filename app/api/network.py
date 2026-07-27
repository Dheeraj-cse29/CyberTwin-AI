from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.models.user import User

from app.database.session import get_db
from app.schemas.network import (
    NetworkCreate,
    NetworkResponse,
    NetworkUpdate,
)
from app.services.network_service import NetworkService

router = APIRouter(
    prefix="/networks",
    tags=["Networks"]
)

service = NetworkService()


@router.post("/", response_model=NetworkResponse)
def create_network(
    network: NetworkCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):

    return service.create_network(
        db=db,
        network=network,
        owner_id=current_user.id
    )


@router.get("/", response_model=list[NetworkResponse])
def get_all_networks(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.get_all_networks(db)


@router.get("/{network_id}", response_model=NetworkResponse)
def get_network(
    network_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.get_network(
        db,
        network_id
    )

@router.put("/{network_id}", response_model=NetworkResponse)
def update_network(
    network_id: int,
    network: NetworkUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.update_network(
        db,
        network_id,
        network
    )

@router.delete("/{network_id}")
def delete_network(
    network_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    service.delete_network(
        db,
        network_id
    )

    return {
        "message": "Network deleted successfully"
    }
    return {
        "message": "Network deleted successfully"
    }