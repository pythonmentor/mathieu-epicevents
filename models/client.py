import configparser
import typing
import enum
from datetime import date
from sqlalchemy import Column, Integer, Text, String, func, ForeignKey, Table, Enum, update, text, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from CONFIG import ENGINE


class Base(DeclarativeBase):
    type_annotation_map = {
        enum.Enum: Enum(enum.Enum),
        typing.Literal: Enum(enum.Enum),
    }

client_staff_association = Table(
    'client_staff',
    Base.metadata,
    Column('client_id', Integer, ForeignKey('client.id'), primary_key=True),
    Column('staff_id', Integer, ForeignKey('staff.id'), primary_key=True)
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
    #staffs = relationship('Staff', secondary=client_staff_association, back_populates='clients')      
    #staffs : Mapped[List[Staff_member]] = relationship(secondary=client_staff_association, back_populates="clients")
    
    def __repr__(self) -> str:
        return f"Client(id={self.id}, fullname={self.fullname})"


class ClientRepository:

    def find_by_fullname(self, fullname):
        with ENGINE.connect() as conn:
            result = conn.execute(text(f"SELECT * FROM client WHERE fullname = '{fullname}'"))
        return result
    
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

    def create_client(self, session, staff):
        client = Client(fullname='John Snow', email="john@life.fr", phone=215452014, name_company="Entreprise Coucou", staff_member_commercial=staff.id)
        session.add(client)
        self.save(session)
        
    def update(self, table, client, column, new_value):
        client.column = new_value
        self.save()
        
    def delete(self, session, client):
        session.delete(client)
        self.save()
        
    def save(self, session):
        session.commit() 


    

