from sqlalchemy.orm import Session

from app.repositories.detection_repository import DetectionRepository


detection_repository = DetectionRepository()


class DetectionService:

    @staticmethod
    def create_detection(
        db: Session,
        attack_id: int,
        asset_id: int,
        detection_result,
        owner_id: int,
    ):
        detection = detection_repository.create(
            db,
            detection_repository.model(
                attack_id=attack_id,
                asset_id=asset_id,
                detected=detection_result.detected,
                severity=detection_result.severity,
                threat_level=detection_result.threat_level,
                reason=detection_result.reason,
                owner_id=owner_id,
            )
        )

        return detection

    @staticmethod
    def get_detections(
        db: Session,
        owner_id: int,
    ):
        return detection_repository.get_by_owner(
            db,
            owner_id,
        )

    @staticmethod
    def get_attack_detections(
        db: Session,
        attack_id: int,
        owner_id: int,
    ):
        return detection_repository.get_by_attack(
            db,
            attack_id,
            owner_id,
        )