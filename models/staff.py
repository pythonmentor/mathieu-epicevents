import enum
import typing
from typing import Literal
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, Text, String, func, ForeignKey, Enum, Table
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship




class Base(DeclarativeBase):
    pass



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
    #clients: Mapped[List["Client"]] = relationship(back_populates="contact_commercial")
    #contracts: Mapped[List["Contract"]] = relationship(back_populates="commercial_contact")
    #events: Mapped[List["Event"]] = relationship(back_populates="support_contact")
 
 



    def __repr__(self) -> str:
        return f"Staff(id={self.id!r}, name={self.name!r}, first_name={self.first_name!r})"
    

class StaffRepository:

    @classmethod
    def find_by_name(cls, session, name):
        return session.query(cls).filter_by(fullname=name).all()
    
    @classmethod
    def find_by_id(cls, session, id) :
        return session.query(cls).filter_by(id=id).all()
    
    @classmethod
    def find_by_email(cls, session, email) :
        return session.query(cls).filter_by(email=email).all()
    
    @classmethod
    def get_all(cls, session) :
        return session.query(cls).all()

    def create_staff(self, session, staff):
        staff = Staff(name="Connor", first_name="Sarah", email="sarah@gmail.com", password="sarah", department="support")
        session.add(staff)
        self.save(session)
        
    def update(self, table, staff, column, new_value):
        staff.column = new_value
        self.save()
        
    def delete(self, session, staff):
        session.delete(staff)
        self.save()
        
    def save(self, session):
        session.commit() 

