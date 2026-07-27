from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from app.database.base import Base
from app.core.enums import AssetType, AssetStatus


class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    asset_type = Column(
        Enum(AssetType),
        nullable=False
    )

    ip_address = Column(String, nullable=False)

    operating_system = Column(String, nullable=False)

    status = Column(
        Enum(AssetStatus),
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