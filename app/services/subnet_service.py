from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.subnet import Subnet
from app.repositories.subnet_repository import SubnetRepository
from app.schemas.subnet import SubnetCreate, SubnetUpdate


class SubnetService:

    def __init__(self):
        self.repository = SubnetRepository()

    def create_subnet(
        self,
        db: Session,
        subnet: SubnetCreate,
    ):
        new_subnet = Subnet(**subnet.model_dump())

        return self.repository.create(
            db,
            new_subnet
        )

    def get_subnet(
        self,
        db: Session,
        subnet_id: int,
    ):
        subnet = self.repository.get_by_id(
            db,
            subnet_id
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
    ):
        return self.repository.get_all(db)

    def get_subnets_by_network(
        self,
        db: Session,
        network_id: int,
    ):
        return self.repository.get_by_network(
            db,
            network_id
        )

    def update_subnet(
        self,
        db: Session,
        subnet_id: int,
        subnet: SubnetUpdate,
    ):
        updated_subnet = self.repository.update(
            db,
            subnet_id,
            subnet.model_dump(exclude_unset=True)
        )

        if updated_subnet is None:
            raise HTTPException(
                status_code=404,
                detail="Subnet not found"
            )

        return updated_subnet

    def delete_subnet(
        self,
        db: Session,
        subnet_id: int,
    ):
        deleted = self.repository.delete(
            db,
            subnet_id
        )

        if not deleted:
            raise HTTPException(
                status_code=404,
                detail="Subnet not found"
            )

        return {"message": "Subnet deleted successfully"}