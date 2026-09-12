from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.models.user import User
from app.database.session import get_db

from app.schemas.network import (
    NetworkCreate,
    NetworkResponse,
    NetworkUpdate,
    NetworkTopologyResponse,
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
    return service.get_all_networks(
        db=db,
        owner_id=current_user.id
    )


@router.get("/{network_id}", response_model=NetworkResponse)
def get_network(
    network_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    network = service.get_network(
        db=db,
        network_id=network_id,
        owner_id=current_user.id
    )

    if network is None:
        raise HTTPException(
            status_code=404,
            detail="Network does not exist."
        )

    return network


@router.get(
    "/{network_id}/topology",
    response_model=NetworkTopologyResponse
)
def get_network_topology(
    network_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    network = service.get_network_topology(
        db=db,
        network_id=network_id,
        owner_id=current_user.id
    )

    if network is None:
        raise HTTPException(
            status_code=404,
            detail="Network does not exist."
        )

    return network


@router.put("/{network_id}", response_model=NetworkResponse)
def update_network(
    network_id: int,
    network: NetworkUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    updated_network = service.update_network(
        db=db,
        network_id=network_id,
        network=network,
        owner_id=current_user.id
    )

    if updated_network is None:
        raise HTTPException(
            status_code=404,
            detail="Network does not exist."
        )

    return updated_network


@router.delete("/{network_id}")
def delete_network(
    network_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    deleted = service.delete_network(
        db=db,
        network_id=network_id,
        owner_id=current_user.id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Network does not exist."
        )

    return {
        "message": "Network deleted successfully"
    }