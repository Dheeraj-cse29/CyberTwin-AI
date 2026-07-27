from sqlalchemy.orm import Session

from app.models.network import Network
from app.repositories.network_repository import NetworkRepository
from app.schemas.network import NetworkCreate, NetworkUpdate


class NetworkService:
    def __init__(self):
        self.repository = NetworkRepository()

    def create_network(
        self,
        db: Session,
        network: NetworkCreate,
        owner_id: int
    ):
        new_network = Network(
            **network.model_dump(),
            owner_id=owner_id
        )

        return self.repository.create(db, new_network)

    def get_network(
        self,
        db: Session,
        network_id: int
    ):
        return self.repository.get_by_id(db, network_id)

    def get_all_networks(
        self,
        db: Session
    ):
        return self.repository.get_all(db)

    def get_user_networks(
        self,
        db: Session,
        owner_id: int
    ):
        return self.repository.get_by_owner(db, owner_id)

    def update_network(
        self,
        db: Session,
        network_id: int,
        network: NetworkUpdate
    ):
        return self.repository.update(
            db,
            network_id,
            network.model_dump(exclude_unset=True)
        )

    def delete_network(
        self,
        db: Session,
        network_id: int
    ):
        return self.repository.delete(db, network_id)