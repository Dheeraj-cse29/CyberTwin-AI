from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.attack import Attack
from app.models.detection import Detection
from app.models.risk import Risk


class AnalyticsService:

    @staticmethod
    def get_security_summary(
        db: Session,
        owner_id: int,
    ):
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

        total_risks = (
            db.query(func.count(Risk.id))
            .filter(Risk.owner_id == owner_id)
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
            "total_attacks": total_attacks or 0,
            "total_detections": total_detections or 0,
            "total_risks": total_risks or 0,
            "high_risks": high_risks or 0,
            "critical_risks": critical_risks or 0,
        }