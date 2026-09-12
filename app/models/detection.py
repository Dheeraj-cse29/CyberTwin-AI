from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class Detection(Base):
    __tablename__ = "detections"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    attack_id = Column(
        Integer,
        ForeignKey("attacks.id"),
        nullable=False
    )

    asset_id = Column(
        Integer,
        ForeignKey("assets.id"),
        nullable=False
    )

    detected = Column(
        Boolean,
        nullable=False,
        default=True
    )

    severity = Column(
        Integer,
        nullable=False
    )

    threat_level = Column(
        String(20),
        nullable=False
    )

    reason = Column(
        String(255),
        nullable=False
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    attack = relationship(
        "Attack"
    )

    asset = relationship(
        "Asset"
    )

    owner = relationship(
        "User"
    )