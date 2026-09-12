from fastapi import APIRouter, Depends
from app.auth.dependencies import get_current_user
from app.models.user import User
from app.core.enums import AttackType
from app.mitre.mitre_mapper import MitreMapper


router = APIRouter(
    prefix="/mitre",
    tags=["MITRE ATT&CK"],
)


@router.get("/{attack_type}")
def get_mitre_mapping(
    attack_type: AttackType,
    current_user: User = Depends(get_current_user),
):
    return MitreMapper.map_attack(attack_type)