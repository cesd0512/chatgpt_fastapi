from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Rol(Base):
    """Model rols in db."""

    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    users = relationship("User", back_populates="rol")


class User(Base):
    """Model User in db."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True , index=True, autoincrement=True)
    username = Column(String)
    password = Column(String)
    rol_id = Column(Integer, ForeignKey("roles.id"), nullable=True)
    rol = relationship("Rol", back_populates="users")
    messages = relationship("ChatMessage", back_populates="user")

