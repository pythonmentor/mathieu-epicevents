from datetime import date
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, Text, String, func, ForeignKey
from typing import List, Optional
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.client import Base



class Contract(Base):
    __tablename__ = 'contract'
    id: Mapped[int] = mapped_column(primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"))
    commercial_contact_id : Mapped[int] = mapped_column(ForeignKey("staff.id"))
    total_amount : Mapped[int]
    balace_due : Mapped[int]
    date_creation : Mapped[date] = mapped_column(insert_default=func.now())
    status : Mapped[bool]

"""
rappel : contact_commercial : FK (= le commercial associé au
client) ;

statut (= si le contrat a été signé) : boolean

"""
