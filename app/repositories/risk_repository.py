from sqlalchemy.orm import Session

from app.models.risk import Risk
from app.repositories.base_repository import BaseRepository


class RiskRepository(BaseRepository[Risk]):

    def __init__(self):
        super().__init__(Risk)

    def get_by_owner(
        self,
        db: Session,
        owner_id: int,
    ):
        return (
            db.query(Risk)
            .filter(
                Risk.owner_id == owner_id
            )
            .all()
        )

    def get_by_detection(
        self,
        db: Session,
        detection_id: int,
        owner_id: int,
    ):
        return (
            db.query(Risk)
            .filter(
                Risk.detection_id == detection_id,
                Risk.owner_id == owner_id,
            )
            .all()
        )