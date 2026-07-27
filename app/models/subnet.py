from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class Subnet(Base):
    __tablename__ = "subnets"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    cidr_block = Column(String(50), nullable=False)

    network_id = Column(
        Integer,
        ForeignKey("networks.id"),
        nullable=False
    )

    network = relationship(
        "Network",
        back_populates="subnets"
    )