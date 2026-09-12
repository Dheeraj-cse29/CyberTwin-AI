from sqlalchemy.orm import Session

from app.models.detection import Detection
from app.repositories.base_repository import BaseRepository


class DetectionRepository(BaseRepository[Detection]):

    def __init__(self):
        super().__init__(Detection)

    def get_by_owner(
        self,
        db: Session,
        owner_id: int,
    ):
        return (
            db.query(Detection)
            .filter(
                Detection.owner_id == owner_id
            )
            .all()
        )

    def get_by_attack(
        self,
        db: Session,
        attack_id: int,
        owner_id: int,
    ):
        return (
            db.query(Detection)
            .filter(
                Detection.attack_id == attack_id,
                Detection.owner_id == owner_id,
            )
            .all()
        )