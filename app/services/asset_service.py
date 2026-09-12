from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.asset import Asset
from app.models.subnet import Subnet
from app.models.network import Network
from app.repositories.asset_repository import AssetRepository

asset_repository = AssetRepository()


class AssetService:

    @staticmethod
    def create_asset(
        db: Session,
        asset_data,
        owner_id: int,
    ):
        # Validate subnet only when one is provided
        if asset_data.subnet_id is not None:
            subnet = (
                db.query(Subnet)
                .join(Network, Subnet.network_id == Network.id)
                .filter(
                    Subnet.id == asset_data.subnet_id,
                    Network.owner_id == owner_id,
                )
                .first()
            )

            if subnet is None:
                raise HTTPException(
                    status_code=404,
                    detail="Subnet does not exist or does not belong to you."
                )

        asset = Asset(
            name=asset_data.name,
            asset_type=asset_data.asset_type,
            ip_address=asset_data.ip_address,
            operating_system=asset_data.operating_system,
            status=asset_data.status,
            owner_id=owner_id,
            subnet_id=asset_data.subnet_id,
        )

        return asset_repository.create(db, asset)

    @staticmethod
    def get_assets(
        db: Session,
        owner_id: int,
    ):
        return asset_repository.get_assets_by_owner(
            db,
            owner_id,
        )

    @staticmethod
    def get_asset(
        db: Session,
        asset_id: int,
        owner_id: int,
    ):
        asset = asset_repository.get_by_id(
            db,
            asset_id,
        )

        if asset is None or asset.owner_id != owner_id:
            return None

        return asset

    @staticmethod
    def update_asset(
        db: Session,
        asset_id: int,
        asset_data,
        owner_id: int,
    ):
        asset = asset_repository.get_by_id(
            db,
            asset_id,
        )

        # Ownership check
        if asset is None or asset.owner_id != owner_id:
            return None

        update_data = asset_data.model_dump(
            exclude_unset=True
        )

        # Validate subnet only when subnet_id is being changed
        if "subnet_id" in update_data:
            subnet_id = update_data["subnet_id"]

            # Allow removing the subnet by setting it to None
            if subnet_id is not None:
                subnet = (
                    db.query(Subnet)
                    .join(Network, Subnet.network_id == Network.id)
                    .filter(
                        Subnet.id == subnet_id,
                        Network.owner_id == owner_id,
                    )
                    .first()
                )

                if subnet is None:
                    raise HTTPException(
                        status_code=404,
                        detail="Subnet does not exist or does not belong to you."
                    )

        return asset_repository.update(
            db,
            asset_id,
            update_data,
        )

    @staticmethod
    def delete_asset(
        db: Session,
        asset_id: int,
        owner_id: int,
    ):
        asset = asset_repository.get_by_id(
            db,
            asset_id,
        )

        # Ownership check
        if asset is None or asset.owner_id != owner_id:
            return False

        return asset_repository.delete(
            db,
            asset_id,
        )
    @staticmethod
    def get_asset_topology(
        db: Session,
        asset_id: int,
        owner_id: int,
    ):
        asset = asset_repository.get_by_id(
            db,
            asset_id,
        )

        if asset is None or asset.owner_id != owner_id:
            return None

        return asset