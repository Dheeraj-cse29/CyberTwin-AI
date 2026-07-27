from sqlalchemy.orm import Session

from app.models.asset import Asset
from app.repositories.base_repository import BaseRepository


class AssetRepository(BaseRepository[Asset]):

    def __init__(self):
        super().__init__(Asset)

    def get_assets_by_owner(
        self,
        db: Session,
        owner_id: int,
    ):
        return (
            db.query(Asset)
            .filter(Asset.owner_id == owner_id)
            .all()
        )