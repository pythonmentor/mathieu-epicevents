from datetime import datetime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, Text, String, func, ForeignKey
from typing import List, Optional
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.client import Base



class Event(Base):
    __tablename__ = 'event'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(500), unique=True)
    contract_id : Mapped[int] = mapped_column(ForeignKey("contract.id"))
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


