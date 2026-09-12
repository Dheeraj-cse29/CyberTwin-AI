from sqlalchemy.orm import Session

from app.models.attack import Attack
from app.repositories.base_repository import BaseRepository


class AttackRepository(BaseRepository[Attack]):

    def __init__(self):
        super().__init__(Attack)

    def get_by_owner(
        self,
        db: Session,
        owner_id: int
    ):
        return (
            db.query(Attack)
            .filter(
                Attack.owner_id == owner_id
            )
            .all()
        )

    def get_by_id_and_owner(
        self,
        db: Session,
        attack_id: int,
        owner_id: int,
    ):
        return (
            db.query(Attack)
            .filter(
                Attack.id == attack_id,
                Attack.owner_id == owner_id,
            )
            .first()
        )