from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.subnet import Subnet
from app.models.network import Network

from app.repositories.subnet_repository import SubnetRepository
from app.schemas.subnet import SubnetCreate, SubnetUpdate


class SubnetService:

    def __init__(self):
        self.repository = SubnetRepository()

    def _get_owned_subnet(
        self,
        db: Session,
        subnet_id: int,
        owner_id: int,
    ):
        subnet = self.repository.get_by_id(
            db,
            subnet_id
        )

        if subnet is None:
            return None

        network = (
            db.query(Network)
            .filter(
                Network.id == subnet.network_id,
                Network.owner_id == owner_id
            )
            .first()
        )

        if network is None:
            return None

        return subnet

    def create_subnet(
        self,
        db: Session,
        subnet: SubnetCreate,
        owner_id: int,
    ):
        network = (
            db.query(Network)
            .filter(
                Network.id == subnet.network_id,
                Network.owner_id == owner_id
            )
            .first()
        )

        if network is None:
            raise HTTPException(
                status_code=404,
                detail="Network not found"
            )

        new_subnet = Subnet(
            **subnet.model_dump()
        )

        return self.repository.create(
            db,
            new_subnet
        )

    def get_subnet(
        self,
        db: Session,
        subnet_id: int,
        owner_id: int,
    ):
        subnet = self._get_owned_subnet(
            db,
            subnet_id,
            owner_id
        )

        if subnet is None:
            raise HTTPException(
                status_code=404,
                detail="Subnet not found"
            )

        return subnet

    def get_all_subnets(
        self,
        db: Session,
        owner_id: int,
    ):
        return (
            db.query(Subnet)
            .join(
                Network,
                Subnet.network_id == Network.id
            )
            .filter(
                Network.owner_id == owner_id
            )
            .all()
        )

    def get_subnets_by_network(
        self,
        db: Session,
        network_id: int,
        owner_id: int,
    ):
        network = (
            db.query(Network)
            .filter(
                Network.id == network_id,
                Network.owner_id == owner_id
            )
            .first()
        )

        if network is None:
            raise HTTPException(
                status_code=404,
                detail="Network not found"
            )

        return self.repository.get_by_network(
            db,
            network_id
        )

    def update_subnet(
        self,
        db: Session,
        subnet_id: int,
        subnet: SubnetUpdate,
        owner_id: int,
    ):
        existing_subnet = self._get_owned_subnet(
            db,
            subnet_id,
            owner_id
        )

        if existing_subnet is None:
            raise HTTPException(
                status_code=404,
                detail="Subnet not found"
            )

        update_data = subnet.model_dump(
            exclude_unset=True
        )

        if "network_id" in update_data:
            network = (
                db.query(Network)
                .filter(
                    Network.id == update_data["network_id"],
                    Network.owner_id == owner_id
                )
                .first()
            )

            if network is None:
                raise HTTPException(
                    status_code=404,
                    detail="Network not found"
                )

        updated_subnet = self.repository.update(
            db,
            subnet_id,
            update_data
        )

        return updated_subnet

    def delete_subnet(
        self,
        db: Session,
        subnet_id: int,
        owner_id: int,
    ):
        existing_subnet = self._get_owned_subnet(
            db,
            subnet_id,
            owner_id
        )

        if existing_subnet is None:
            raise HTTPException(
                status_code=404,
                detail="Subnet not found"
            )

        self.repository.delete(
            db,
            subnet_id
        )

        return {
            "message": "Subnet deleted successfully"
        }