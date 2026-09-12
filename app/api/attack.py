from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.database import get_db
from app.models.user import User
from app.schemas.attack import (
    AttackCreate,
    AttackResponse,
)
from app.services.attack_service import AttackService


router = APIRouter(
    prefix="/attacks",
    tags=["Attack Simulation"]
)


@router.post(
    "/simulate",
    response_model=AttackResponse
)
def simulate_attack(
    attack: AttackCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return AttackService.simulate_attack(
        db=db,
        attack_data=attack,
        owner_id=current_user.id,
    )


@router.get(
    "/",
    response_model=list[AttackResponse]
)
def get_attacks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return AttackService.get_attacks(
        db=db,
        owner_id=current_user.id,
    )


@router.get(
    "/{attack_id}",
    response_model=AttackResponse
)
def get_attack(
    attack_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    attack = AttackService.get_attack(
        db=db,
        attack_id=attack_id,
        owner_id=current_user.id,
    )

    if attack is None:
        from fastapi import HTTPException

        raise HTTPException(
            status_code=404,
            detail="Attack event does not exist."
        )

    return attack