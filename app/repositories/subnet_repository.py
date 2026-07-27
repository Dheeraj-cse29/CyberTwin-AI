from sqlalchemy.orm import Session

from app.models.subnet import Subnet
from app.repositories.base_repository import BaseRepository


class SubnetRepository(BaseRepository[Subnet]):

    def __init__(self):
        super().__init__(Subnet)

    def get_by_network(
        self,
        db: Session,
        network_id: int,
    ):
        return (
            db.query(Subnet)
            .filter(Subnet.network_id == network_id)
            .all()
        )