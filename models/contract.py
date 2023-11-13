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


class ContractRepository:

    @classmethod
    def find_by_name(cls, session, name):
        return session.query(cls).filter_by(name=name).all()
    
    @classmethod
    def find_by_id(cls, session, id) :
        return session.query(cls).filter_by(id=id).all()
    
    @classmethod
    def find_by_client_id(cls, session, client_id) :
        return session.query(cls).filter_by(client_id=client_id).all()
    
    @classmethod
    def get_all(cls, session) :
        return session.query(cls).all()

    def create_staff(self, session, staff):
        contract = Contract(name="Jeux Olympique")
        session.add(contract)
        self.save(session)
        
    def update(self, table, contract, column, new_value):
        contract.column = new_value
        self.save()
        
    def delete(self, session, contract):
        session.delete(contract)
        self.save()
        
    def save(self, session):
        session.commit() 
