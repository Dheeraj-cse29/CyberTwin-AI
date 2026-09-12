from sqlalchemy.orm import Session

from app.models.incident import Incident
from app.repositories.base_repository import BaseRepository


class IncidentRepository(BaseRepository[Incident]):

    def __init__(self):
        super().__init__(Incident)

    def get_by_owner(
        self,
        db: Session,
        owner_id: int,
    ):
        return (
            db.query(Incident)
            .filter(Incident.owner_id == owner_id)
            .all()
        )

    def get_by_id_and_owner(
        self,
        db: Session,
        incident_id: int,
        owner_id: int,
    ):
        return (
            db.query(Incident)
            .filter(
                Incident.id == incident_id,
                Incident.owner_id == owner_id,
            )
            .first()
        )