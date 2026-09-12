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
        owner_id: int,
    ):
        new_network = Network(
            **network.model_dump(),
            owner_id=owner_id,
        )

        return self.repository.create(
            db,
            new_network,
        )

    def get_network(
        self,
        db: Session,
        network_id: int,
        owner_id: int,
    ):
        network = self.repository.get_by_id(
            db,
            network_id,
        )

        if network is None or network.owner_id != owner_id:
            return None

        return network

    def get_all_networks(
        self,
        db: Session,
        owner_id: int,
    ):
        return self.repository.get_by_owner(
            db,
            owner_id,
        )

    def update_network(
        self,
        db: Session,
        network_id: int,
        network: NetworkUpdate,
        owner_id: int,
    ):
        existing_network = self.repository.get_by_id(
            db,
            network_id,
        )

        if (
            existing_network is None
            or existing_network.owner_id != owner_id
        ):
            return None

        return self.repository.update(
            db,
            network_id,
            network.model_dump(exclude_unset=True),
        )

    def delete_network(
        self,
        db: Session,
        network_id: int,
        owner_id: int,
    ):
        existing_network = self.repository.get_by_id(
            db,
            network_id,
        )

        if (
            existing_network is None
            or existing_network.owner_id != owner_id
        ):
            return False

        return self.repository.delete(
            db,
            network_id,
        )

    def get_network_topology(
        self,
        db: Session,
        network_id: int,
        owner_id: int,
    ):
        network = self.repository.get_by_id(
            db,
            network_id,
        )

        if network is None or network.owner_id != owner_id:
            return None

        return network