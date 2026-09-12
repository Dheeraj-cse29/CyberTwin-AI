from sqlalchemy.orm import Session

from app.models.risk import Risk
from app.repositories.risk_repository import RiskRepository
from app.risk_engine.risk_calculator import RiskCalculator


risk_repository = RiskRepository()


class RiskService:

    @staticmethod
    def calculate_and_create_risk(
        db: Session,
        detection,
        attack_severity: int,
        attack_id: int,
        asset_id: int,
        owner_id: int,
    ):
        # ---------------------------------
        # 1. Calculate risk
        # ---------------------------------

        result = RiskCalculator.calculate_risk(
            attack_severity=attack_severity,
            detection_severity=detection.severity,
        )

        # ---------------------------------
        # 2. Create risk record
        # ---------------------------------

        risk = Risk(
            detection_id=detection.id,
            attack_id=attack_id,
            asset_id=asset_id,
            risk_score=result["risk_score"],
            risk_level=result["risk_level"],
            owner_id=owner_id,
        )

        risk = risk_repository.create(
            db,
            risk
        )

        return risk

    @staticmethod
    def get_risks(
        db: Session,
        owner_id: int,
    ):
        return risk_repository.get_by_owner(
            db,
            owner_id
        )

    @staticmethod
    def get_detection_risks(
        db: Session,
        detection_id: int,
        owner_id: int,
    ):
        return risk_repository.get_by_detection(
            db,
            detection_id,
            owner_id,
        )