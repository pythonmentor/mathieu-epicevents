from datetime import datetime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, Text, String, func, ForeignKey, UniqueConstraint
from typing import List, Optional
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
#from models.client import Base
from models.contract import Contract


class Base(DeclarativeBase):
    pass

class Event(Base):
    
    __tablename__ = 'event'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(500), unique=True)
    contract_id = mapped_column(ForeignKey("contract.id"))
    contract = relationship("Contract", back_populates="event")
    #contract_id : Mapped[int] = mapped_column(ForeignKey("contract.id"))
    #contract: Mapped["Contract"] = relationship(back_populates="event")
    __table_args__ = (UniqueConstraint("contract_id"),)
    client_id : Mapped[int] = mapped_column(ForeignKey("client.id"))
    event_date_start : Mapped[datetime] 
    event_date_end : Mapped[datetime]
    support_contact : Mapped[int] = mapped_column(ForeignKey("staff.id"))
    location : Mapped[str] = mapped_column(String(250))
    attendees : Mapped[int]
    notes : Mapped[str] = mapped_column(String(1000))

    
    def __repr__(self) -> str:
        return f"Event(id={self.id!r}, name={self.name!r}, location={self.location!r})"


"""
rappel : client_name, client_contact_email, client_contact_phone : FK

"""

class EventRepository:

    @classmethod
    def find_by_name(cls, session, name):
        return session.query(cls).filter_by(name=name).all()
    
    @classmethod
    def find_by_id(cls, session, id) :
        return session.query(cls).filter_by(id=id).all()
    
    @classmethod
    def find_by_client_id(cls, session, client_id) :
        return session.query(cls).filter_by(email=client_id).all()
    
    @classmethod
    def get_all(cls, session) :
        return session.query(cls).all()

    def create_staff(self, session, staff):
        event = Event(name="Jeux Olympique")
        session.add(event)
        self.save(session)
        
    def update(self, table, event, column, new_value):
        event.column = new_value
        self.save()
        
    def delete(self, session, event):
        session.delete(event)
        self.save()
        
    def save(self, session):
        session.commit() 

