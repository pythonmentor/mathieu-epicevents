from __future__ import annotations
import typing
from typing import List
import enum
from datetime import date
from sqlalchemy import Column, Integer, String, func, ForeignKey, Table, Enum, update, text, insert
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from CONFIG import SESSION, ENGINE
from models.staff import Staff
from models.contract import Contract
from models.event import Event


class Base(DeclarativeBase):
    type_annotation_map = {
        enum.Enum: Enum(enum.Enum),
        typing.Literal: Enum(enum.Enum),
    }


class Client(Base):
    __tablename__ = 'client'
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    fullname: Mapped[str] = mapped_column(String(100), unique=True)
    email : Mapped[str] = mapped_column(String(300), nullable=True)
    phone : Mapped[int]
    name_company : Mapped[str] = mapped_column(String(300))
    date_creation : Mapped[date] = mapped_column(insert_default=func.now())
    date_update : Mapped[date] = mapped_column(insert_default=func.now())
    contact_commercial_id: Mapped[int] = mapped_column(ForeignKey("staff.id"))
    #contact_commercial_id: Mapped[List["Staff"]] = relationship(back_populates="client")
    #contracts: Mapped[List["Contract"]] = relationship(back_populates="contract")
    #events: Mapped[List["Event"]] = relationship()
    
    def __repr__(self) -> str:
        return f"Client(id={self.id}, fullname={self.fullname})"


class ClientRepository:

    def find_by_fullname(self, fullname):
        return SESSION.query(Client).filter(Client.fullname==f'{fullname}').first()
        
        #with ENGINE.connect() as conn:
            #result = conn.execute(text(f"SELECT * FROM client WHERE fullname = '{fullname}'"))
        #return result
    
    
    def find_by_id(self, id) :
        with ENGINE.connect() as conn:
            result = conn.execute(text(f"SELECT * FROM client WHERE id = {id}"))
        return result
    
    @classmethod
    def find_by_email(cls, session, email) :
        return session.query(cls).filter_by(email=email).all()
    
    
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
        
  
        


    

