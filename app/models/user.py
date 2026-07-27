from sqlalchemy import Column, Integer, String, Boolean
from app.database.base import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    email = Column(String(150), unique=True, nullable=False)

    username = Column(String(50), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    role = Column(String(50), default="SOC Analyst")

    is_active = Column(Boolean, default=True)

    assets = relationship(
    "Asset",
    back_populates="owner",
    cascade="all, delete-orphan"
    )
    networks = relationship(
    "Network",
    back_populates="owner",
    cascade="all, delete-orphan",
)