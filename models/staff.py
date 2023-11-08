import enum
import typing
from typing import Literal
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, Text, String, func, ForeignKey, Enum, Table
from typing import List, Optional
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.client import Base, client_staff_association




class Department(enum.Enum):
    COMMERCIAL = "commercial"
    SUPPORT = "support"
    MANAGEMENT = "management"


class Staff(Base):
    __tablename__ = 'staff'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    first_name: Mapped[str] = mapped_column(String(100))
    email : Mapped[str] = mapped_column(String(300))
    password : Mapped[str] = mapped_column(String(50))
    department : Mapped[Department]
    clients = relationship('Staff', secondary=client_staff_association, back_populates='staffs')
    #children: Mapped[List[Client]] = relationship(secondary=staff_member_client_table, back_populates="parents")


    def __repr__(self) -> str:
        return f"Staff(id={self.id!r}, name={self.name!r}, first_name={self.first_name!r})"
