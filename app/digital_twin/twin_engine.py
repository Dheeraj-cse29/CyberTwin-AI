from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.asset import Asset
from app.models.attack import Attack
from app.models.detection import Detection
from app.models.risk import Risk


class DigitalTwinEngine:

    @staticmethod
    def get_environment_state(
        db: Session,
        owner_id: int,
    ):

        total_assets = (
            db.query(func.count(Asset.id))
            .filter(Asset.owner_id == owner_id)
            .scalar()
        )

        active_assets = (
            db.query(func.count(Asset.id))
            .filter(
                Asset.owner_id == owner_id,
                Asset.status == "Active",
            )
            .scalar()
        )

        compromised_assets = (
            db.query(func.count(Asset.id))
            .filter(
                Asset.owner_id == owner_id,
                Asset.status == "Compromised",
            )
            .scalar()
        )

        total_attacks = (
            db.query(func.count(Attack.id))
            .filter(Attack.owner_id == owner_id)
            .scalar()
        )

        total_detections = (
            db.query(func.count(Detection.id))
            .filter(Detection.owner_id == owner_id)
            .scalar()
        )

        critical_risks = (
            db.query(func.count(Risk.id))
            .filter(
                Risk.owner_id == owner_id,
                Risk.risk_level == "CRITICAL",
            )
            .scalar()
        )

        high_risks = (
            db.query(func.count(Risk.id))
            .filter(
                Risk.owner_id == owner_id,
                Risk.risk_level == "HIGH",
            )
            .scalar()
        )

        return {
            "environment": {
                "total_assets": total_assets or 0,
                "active_assets": active_assets or 0,
                "compromised_assets": compromised_assets or 0,
            },
            "security": {
                "total_attacks": total_attacks or 0,
                "total_detections": total_detections or 0,
                "high_risks": high_risks or 0,
                "critical_risks": critical_risks or 0,
            },
        }