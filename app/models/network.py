from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class Network(Base):
    __tablename__ = "networks"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    description = Column(String(255), nullable=True)

    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    owner = relationship(
        "User",
        back_populates="networks"
    )

    subnets = relationship(
        "Subnet",
        back_populates="network",
        cascade="all, delete-orphan"
    )