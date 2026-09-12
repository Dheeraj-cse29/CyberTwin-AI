from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(255),
        nullable=False
    )

    description = Column(
        String(500),
        nullable=False
    )

    severity = Column(
        Integer,
        nullable=False
    )

    status = Column(
        String(30),
        nullable=False,
        default="OPEN"
    )

    risk_id = Column(
        Integer,
        ForeignKey("risks.id"),
        nullable=False
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

    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    risk = relationship("Risk")
    detection = relationship("Detection")
    attack = relationship("Attack")
    asset = relationship("Asset")
    owner = relationship("User")