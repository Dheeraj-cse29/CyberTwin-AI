from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.attack import Attack
from app.models.asset import Asset
from app.repositories.attack_repository import AttackRepository


class AttackService:

    def __init__(self):
        self.repository = AttackRepository()

    def simulate_attack(
        self,
        db: Session,
        attack_data,
        owner_id: int,
    ):
        # Make sure the target asset belongs to the current user
        target_asset = (
            db.query(Asset)
            .filter(
                Asset.id == attack_data.target_asset_id,
                Asset.owner_id == owner_id,
            )
            .first()
        )

        if target_asset is None:
            raise HTTPException(
                status_code=404,
                detail="Target asset does not exist or does not belong to you."
            )

        attack = Attack(
            attack_type=attack_data.attack_type,
            source_ip=attack_data.source_ip,
            target_asset_id=attack_data.target_asset_id,
            severity=attack_data.severity,
            description=attack_data.description,
            owner_id=owner_id,
        )

        return self.repository.create(
            db,
            attack,
        )

    def get_attacks(
        self,
        db: Session,
        owner_id: int,
    ):
        return self.repository.get_by_owner(
            db,
            owner_id,
        )

    def get_attack(
        self,
        db: Session,
        attack_id: int,
        owner_id: int,
    ):
        attack = self.repository.get_by_id_and_owner(
            db,
            attack_id,
            owner_id,
        )

        if attack is None:
            raise HTTPException(
                status_code=404,
                detail="Attack does not exist."
            )

        return attack

    def delete_attack(
        self,
        db: Session,
        attack_id: int,
        owner_id: int,
    ):
        attack = self.repository.get_by_id_and_owner(
            db,
            attack_id,
            owner_id,
        )

        if attack is None:
            raise HTTPException(
                status_code=404,
                detail="Attack does not exist."
            )

        return self.repository.delete(
            db,
            attack_id,
        )