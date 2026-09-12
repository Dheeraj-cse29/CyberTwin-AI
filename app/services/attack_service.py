from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.attack import Attack
from app.models.asset import Asset

from app.repositories.attack_repository import AttackRepository

from app.detection_engine.detector import DetectionEngine
from app.services.detection_service import DetectionService
from app.services.risk_service import RiskService
from app.incident_response.incident_service import IncidentService


attack_repository = AttackRepository()


class AttackService:

    @staticmethod
    def simulate_attack(
        db: Session,
        attack_data,
        owner_id: int,
    ):

        # ---------------------------------
        # 1. Validate target asset
        # ---------------------------------

        asset = (
            db.query(Asset)
            .filter(
                Asset.id == attack_data.target_asset_id,
                Asset.owner_id == owner_id,
            )
            .first()
        )

        if asset is None:
            raise HTTPException(
                status_code=404,
                detail="Target asset does not exist or does not belong to you."
            )

        # ---------------------------------
        # 2. Create attack
        # ---------------------------------

        attack = Attack(
            attack_type=attack_data.attack_type,
            source_ip=attack_data.source_ip,
            target_asset_id=attack_data.target_asset_id,
            severity=attack_data.severity,
            description=attack_data.description,
            owner_id=owner_id,
        )

        # Save attack FIRST
        attack = attack_repository.create(
            db,
            attack
        )

        # ---------------------------------
        # 3. Analyze attack
        # ---------------------------------

        detection_result = DetectionEngine.analyze_attack(
            attack
        )

        # ---------------------------------
        # 4. Create detection
        # ---------------------------------

        detection = DetectionService.create_detection(
            db=db,
            attack_id=attack.id,
            asset_id=attack.target_asset_id,
            detection_result=detection_result,
            owner_id=owner_id,
        )

        # ---------------------------------
        # 5. Calculate and create risk
        # ---------------------------------

        risk = RiskService.calculate_and_create_risk(
            db=db,
            detection=detection,
            attack_severity=attack.severity,
            attack_id=attack.id,
            asset_id=attack.target_asset_id,
            owner_id=owner_id,
        )

        # ---------------------------------
        # 6. Create incident for high risk
        # ---------------------------------

        if risk.risk_level in {"HIGH", "CRITICAL"}:

            IncidentService().create_incident(
                db=db,
                title=f"{risk.risk_level} security incident detected",
                description=(
                    f"{detection.reason} "
                    f"Attack type: {attack.attack_type.value}. "
                    f"Source IP: {attack.source_ip}."
                ),
                severity=detection.severity,
                risk_id=risk.id,
                detection_id=detection.id,
                attack_id=attack.id,
                asset_id=attack.target_asset_id,
                owner_id=owner_id,
            )

        # ---------------------------------
        # 7. Return attack
        # ---------------------------------

        return attack

    @staticmethod
    def get_attacks(
        db: Session,
        owner_id: int,
    ):
        return attack_repository.get_by_owner(
            db,
            owner_id
        )

    @staticmethod
    def get_attack(
        db: Session,
        attack_id: int,
        owner_id: int,
    ):
        attack = attack_repository.get_by_id(
            db,
            attack_id
        )

        if attack is None or attack.owner_id != owner_id:
            return None

        return attack