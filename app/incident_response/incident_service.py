from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.incident import Incident
from app.models.risk import Risk
from app.models.detection import Detection
from app.models.attack import Attack
from app.models.asset import Asset

from app.repositories.incident_repository import IncidentRepository


class IncidentService:

    def __init__(self):
        self.repository = IncidentRepository()

    def create_incident(
        self,
        db: Session,
        title: str,
        description: str,
        severity: int,
        risk_id: int,
        detection_id: int,
        attack_id: int,
        asset_id: int,
        owner_id: int,
    ):
        # ---------------------------------
        # 1. Validate risk ownership
        # ---------------------------------

        risk = (
            db.query(Risk)
            .filter(
                Risk.id == risk_id,
                Risk.owner_id == owner_id,
            )
            .first()
        )

        if risk is None:
            raise HTTPException(
                status_code=404,
                detail="Risk does not exist or does not belong to you.",
            )

        # ---------------------------------
        # 2. Validate detection ownership
        # ---------------------------------

        detection = (
            db.query(Detection)
            .filter(
                Detection.id == detection_id,
                Detection.owner_id == owner_id,
            )
            .first()
        )

        if detection is None:
            raise HTTPException(
                status_code=404,
                detail="Detection does not exist or does not belong to you.",
            )

        # ---------------------------------
        # 3. Validate attack ownership
        # ---------------------------------

        attack = (
            db.query(Attack)
            .filter(
                Attack.id == attack_id,
                Attack.owner_id == owner_id,
            )
            .first()
        )

        if attack is None:
            raise HTTPException(
                status_code=404,
                detail="Attack does not exist or does not belong to you.",
            )

        # ---------------------------------
        # 4. Validate asset ownership
        # ---------------------------------

        asset = (
            db.query(Asset)
            .filter(
                Asset.id == asset_id,
                Asset.owner_id == owner_id,
            )
            .first()
        )

        if asset is None:
            raise HTTPException(
                status_code=404,
                detail="Asset does not exist or does not belong to you.",
            )

        # ---------------------------------
        # 5. Validate relationships
        # ---------------------------------

        if risk.detection_id != detection_id:
            raise HTTPException(
                status_code=400,
                detail="Risk does not belong to the specified detection.",
            )

        if risk.attack_id != attack_id:
            raise HTTPException(
                status_code=400,
                detail="Risk does not belong to the specified attack.",
            )

        if risk.asset_id != asset_id:
            raise HTTPException(
                status_code=400,
                detail="Risk does not belong to the specified asset.",
            )

        if detection.attack_id != attack_id:
            raise HTTPException(
                status_code=400,
                detail="Detection does not belong to the specified attack.",
            )

        if detection.asset_id != asset_id:
            raise HTTPException(
                status_code=400,
                detail="Detection does not belong to the specified asset.",
            )

        if attack.target_asset_id != asset_id:
            raise HTTPException(
                status_code=400,
                detail="Attack does not target the specified asset.",
            )

        # ---------------------------------
        # 6. Create incident
        # ---------------------------------

        incident = Incident(
            title=title,
            description=description,
            severity=severity,
            status="OPEN",
            risk_id=risk_id,
            detection_id=detection_id,
            attack_id=attack_id,
            asset_id=asset_id,
            owner_id=owner_id,
        )

        return self.repository.create(
            db,
            incident,
        )

    def get_incidents(
        self,
        db: Session,
        owner_id: int,
    ):
        return self.repository.get_by_owner(
            db,
            owner_id,
        )

    def get_incident(
        self,
        db: Session,
        incident_id: int,
        owner_id: int,
    ):
        incident = self.repository.get_by_id_and_owner(
            db,
            incident_id,
            owner_id,
        )

        if incident is None:
            raise HTTPException(
                status_code=404,
                detail="Incident does not exist.",
            )

        return incident

    def update_status(
        self,
        db: Session,
        incident_id: int,
        status: str,
        owner_id: int,
    ):
        incident = self.repository.get_by_id_and_owner(
            db,
            incident_id,
            owner_id,
        )

        if incident is None:
            raise HTTPException(
                status_code=404,
                detail="Incident does not exist.",
            )

        allowed_statuses = {
            "OPEN",
            "INVESTIGATING",
            "CONTAINED",
            "RESOLVED",
            "CLOSED",
        }

        status = status.upper()

        if status not in allowed_statuses:
            raise HTTPException(
                status_code=400,
                detail=(
                    "Invalid status. Allowed values: "
                    "OPEN, INVESTIGATING, CONTAINED, "
                    "RESOLVED, CLOSED"
                ),
            )

        return self.repository.update(
            db,
            incident_id,
            {"status": status},
        )

    def delete_incident(
        self,
        db: Session,
        incident_id: int,
        owner_id: int,
    ):
        incident = self.repository.get_by_id_and_owner(
            db,
            incident_id,
            owner_id,
        )

        if incident is None:
            raise HTTPException(
                status_code=404,
                detail="Incident does not exist.",
            )

        return self.repository.delete(
            db,
            incident_id,
        )