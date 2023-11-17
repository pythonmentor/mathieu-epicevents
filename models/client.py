from __future__ import annotations

from typing import List
import enum
from datetime import date
from sqlalchemy import Column, Integer, String, func, ForeignKey, Table, Enum, update, text, insert
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from settings import Base, SESSION, ENGINE
#from models.staff import Staff
#from models.contract import Contract
#from models.event import Event




class Client(Base):
    __tablename__ = 'client'
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    fullname: Mapped[str] = mapped_column(String(100), unique=True)
    email : Mapped[str] = mapped_column(String(300), nullable=True)
    phone : Mapped[int]
    name_company : Mapped[str] = mapped_column(String(300))
    date_creation : Mapped[date] = mapped_column(insert_default=func.now())
    date_update : Mapped[date] = mapped_column(insert_default=func.now())

    commercial_contact_id = mapped_column(ForeignKey("staff.id"))
    commercial_contact: Mapped[Staff] = relationship(back_populates="clients")
    

    contracts: Mapped[List["Contract"]] = relationship(back_populates="client")
    events: Mapped[List["Event"]] = relationship(back_populates="client")
    
    def __repr__(self) -> str:
        return f"Client(id={self.id}, fullname={self.fullname})"


class ClientRepository:

    def find_by_fullname(self, fullname):
        return SESSION.query(Client).filter(Client.fullname==fullname).first()
    
    
    def find_by_id(self, id) :
        return SESSION.query(Client).filter(Client.id==id).first()
    
    
    @classmethod
    def find_by_email(cls, email) :
        return SESSION.query(cls).filter_by(email=email).all()
    
    
    def get_all(self) :
        with ENGINE.connect() as conn:
            result = conn.execute(text("SELECT * FROM client"))
        return result
        #return session.query(cls).all()

    def create_client(self, session, datas, staff_id):
        client = Client(fullname=datas["fullname"], email=datas["email"], phone=datas["phone"], name_company=datas["name_company"], contact_commercial_id = staff_id )
        #session.merge(client)
        session.add(client)
        SESSION.commit() 

        
    def update(self, client_id, column, new_value):       
        with ENGINE.connect() as conn:
            result = conn.execute(text(f"UPDATE client SET {column} = {new_value} WHERE id = {client_id};"))
            conn.commit()
        
        
    def delete(self, client):
        SESSION.delete(client)
        SESSION.commit() 
        
  
        


    

