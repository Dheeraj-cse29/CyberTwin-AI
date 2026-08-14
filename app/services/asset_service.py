from sqlalchemy.orm import Session

from app.models.asset import Asset
from app.repositories.asset_repository import AssetRepository

asset_repository = AssetRepository()


class AssetService:

    @staticmethod
    def create_asset(db: Session, asset_data, owner_id: int):

        asset = Asset(
            name=asset_data.name,
            asset_type=asset_data.asset_type,
            ip_address=asset_data.ip_address,
            operating_system=asset_data.operating_system,
            status=asset_data.status,
            owner_id=owner_id,
            subnet_id=asset_data.subnet_id,   # <-- Add this line
        )

        return asset_repository.create(db, asset)

    @staticmethod
    def get_assets(db: Session, owner_id: int):
        return asset_repository.get_assets_by_owner(
            db,
            owner_id,
        )