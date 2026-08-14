from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from app.database.base import Base
from app.core.enums import AssetType, AssetStatus


class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    asset_type = Column(
    Enum(
        AssetType,
        values_callable=lambda enum: [e.value for e in enum]
    ),
    nullable=False
)

    ip_address = Column(String, nullable=False)

    operating_system = Column(String, nullable=False)

    status = Column(
    Enum(
        AssetStatus,
        values_callable=lambda enum: [e.value for e in enum]
    ),
    default=AssetStatus.ACTIVE,
    nullable=False
)
    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    owner = relationship(
        "User",
        back_populates="assets"
    )

    subnet_id = Column(
    Integer,
    ForeignKey("subnets.id"),
    nullable=True
    )
    subnet = relationship(
    "Subnet",
    back_populates="assets"
    )