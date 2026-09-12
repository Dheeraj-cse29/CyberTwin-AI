from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from app.database.base import Base
from app.core.enums import AttackType, AttackStatus


class Attack(Base):
    __tablename__ = "attacks"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    attack_type = Column(
        Enum(
            AttackType,
            values_callable=lambda enum: [e.value for e in enum]
        ),
        nullable=False
    )

    source_ip = Column(
        String,
        nullable=False
    )

    target_asset_id = Column(
        Integer,
        ForeignKey("assets.id"),
        nullable=False
    )

    status = Column(
        Enum(
            AttackStatus,
            values_callable=lambda enum: [e.value for e in enum]
        ),
        default=AttackStatus.SIMULATED,
        nullable=False
    )

    severity = Column(
        Integer,
        default=1,
        nullable=False
    )

    description = Column(
        String,
        nullable=True
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    target_asset = relationship(
        "Asset"
    )

    owner = relationship(
        "User"
    )