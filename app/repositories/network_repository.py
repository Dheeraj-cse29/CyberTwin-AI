from sqlalchemy.orm import Session

from app.models.network import Network
from app.repositories.base_repository import BaseRepository


class NetworkRepository(BaseRepository[Network]):
    def __init__(self):
        super().__init__(Network)

    def get_by_owner(
        self,
        db: Session,
        owner_id: int
    ):
        return (
            db.query(Network)
            .filter(Network.owner_id == owner_id)
            .all()
        )