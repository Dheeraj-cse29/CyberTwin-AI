from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class Risk(Base):
    __tablename__ = "risks"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    detection_id = Column(
        Integer,
        ForeignKey("detections.id"),
        nullable=False
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

    risk_score = Column(
        Float,
        nullable=False
    )

    risk_level = Column(
        String(20),
        nullable=False
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    detection = relationship(
        "Detection"
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