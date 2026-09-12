from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.database import get_db
from app.models.user import User

from app.schemas.incident import (
    IncidentCreate,
    IncidentResponse,
    IncidentStatusUpdate,
)

from app.incident_response.incident_service import IncidentService


router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"],
)

service = IncidentService()


@router.post(
    "/",
    response_model=IncidentResponse,
)
def create_incident(
    incident: IncidentCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.create_incident(
        db=db,
        title=incident.title,
        description=incident.description,
        severity=incident.severity,
        risk_id=incident.risk_id,
        detection_id=incident.detection_id,
        attack_id=incident.attack_id,
        asset_id=incident.asset_id,
        owner_id=current_user.id,
    )


@router.get(
    "/",
    response_model=list[IncidentResponse],
)
def get_incidents(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.get_incidents(
        db=db,
        owner_id=current_user.id,
    )


@router.get(
    "/{incident_id}",
    response_model=IncidentResponse,
)
def get_incident(
    incident_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.get_incident(
        db=db,
        incident_id=incident_id,
        owner_id=current_user.id,
    )


@router.put(
    "/{incident_id}/status",
    response_model=IncidentResponse,
)
def update_incident_status(
    incident_id: int,
    status_data: IncidentStatusUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return service.update_status(
        db=db,
        incident_id=incident_id,
        status=status_data.status,
        owner_id=current_user.id,
    )


@router.delete("/{incident_id}")
def delete_incident(
    incident_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    service.delete_incident(
        db=db,
        incident_id=incident_id,
        owner_id=current_user.id,
    )

    return {
        "message": "Incident deleted successfully"
    }