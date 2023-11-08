import typing
import enum
from datetime import date
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, Text, String, func, ForeignKey, Table, Enum
from typing import List, Optional
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship



class Base(DeclarativeBase):
    type_annotation_map = {
        enum.Enum: Enum(enum.Enum),
        typing.Literal: Enum(enum.Enum),
    }

client_staff_association = Table(
    'client_staff',
    Base.metadata,
    Column('client_id', Integer, ForeignKey('client.id')),
    Column('staff_id', Integer, ForeignKey('staff.id'))
)

class Client(Base):
    #from models.staff import Staff
    __tablename__ = 'client'
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    fullname: Mapped[str] = mapped_column(String(100), unique=True)
    email : Mapped[str] = mapped_column(String(300), nullable=True)
    phone : Mapped[int]
    name_company : Mapped[str] = mapped_column(String(300))
    date_creation : Mapped[date] = mapped_column(insert_default=func.now())
    date_update : Mapped[date] = mapped_column(insert_default=func.now())
    staffs = relationship('Staff', secondary=client_staff_association, back_populates='clients')
    #staff_member_commercial : Mapped[int] = mapped_column(ForeignKey("staff_member.id"), nullable=True)
    #staff_member_support : Mapped[int] = mapped_column(ForeignKey("staff_member.id"), nullable=True)
    #staff_member_management : Mapped[int] = mapped_column(ForeignKey("staff_member.id"), nullable=True)
        



    #parents : Mapped[List[Staff_member]] = relationship(secondary=staff_member_client_table, back_populates="children")

    @classmethod
    def find_by_name(cls, session, fullname):
        return session.query(cls).filter_by(fullname=fullname).all()

    def __repr__(self) -> str:
        return f"Client(id={self.id}, fullname={self.fullname})"



