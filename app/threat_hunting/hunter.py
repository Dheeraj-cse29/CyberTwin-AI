from sqlalchemy.orm import Session

from app.models.attack import Attack
from app.models.detection import Detection


class ThreatHunter:

    @staticmethod
    def hunt(
        db: Session,
        owner_id: int,
        threat_level: str | None = None,
        attack_type: str | None = None,
    ):
        query = (
            db.query(Detection, Attack)
            .join(
                Attack,
                Detection.attack_id == Attack.id
            )
            .filter(
                Detection.owner_id == owner_id,
                Attack.owner_id == owner_id,
            )
        )

        if threat_level:
            query = query.filter(
                Detection.threat_level == threat_level.upper()
            )

        if attack_type:
            query = query.filter(
                Attack.attack_type == attack_type.upper()
            )

        results = query.all()

        return [
            {
                "detection_id": detection.id,
                "attack_id": attack.id,
                "attack_type": attack.attack_type,
                "source_ip": attack.source_ip,
                "asset_id": detection.asset_id,
                "severity": detection.severity,
                "threat_level": detection.threat_level,
                "reason": detection.reason,
            }
            for detection, attack in results
        ]