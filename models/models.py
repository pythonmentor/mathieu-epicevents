import enum
from datetime import date, datetime
from sqlalchemy import String, func, ForeignKey, Enum, Table, text, UniqueConstraint
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from settings import Base, SESSION, ENGINE



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

    
    clients: Mapped[List["Client"]] = relationship(back_populates="commercial_contact", lazy="selectin")

    contracts: Mapped[List["Contract"]] = relationship(back_populates="commercial_contact", lazy="selectin")

    events: Mapped[List["Event"]] = relationship(back_populates="support_contact", lazy="selectin")
 
 
    def __repr__(self) -> str:
        return f"Staff(id={self.id!r}, name={self.name!r}, first_name={self.first_name!r})"
    

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
    commercial_contact = relationship('Staff', back_populates="clients")
    
    contracts: Mapped[List["Contract"]] = relationship(back_populates="client")
    events: Mapped[List["Event"]] = relationship(back_populates="client")
    
    def __repr__(self) -> str:
        return f"Client(id={self.id!r}, fullname={self.fullname!r})"



class Event(Base):
    
    __tablename__ = 'event'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(500), unique=True)

    contract_id = mapped_column(ForeignKey("contract.id"))
    contract = relationship('Contract', back_populates="event")

    __table_args__ = (UniqueConstraint("contract_id"),)

    
    client_id = mapped_column(ForeignKey("client.id"))
    client = relationship('Client', back_populates="events")

    event_date_start : Mapped[datetime] 
    event_date_end : Mapped[datetime]

    support_contact_id = mapped_column(ForeignKey("staff.id"))
    support_contact = relationship('Staff', back_populates="events")

    location : Mapped[str] = mapped_column(String(250))
    attendees : Mapped[int]
    notes : Mapped[str] = mapped_column(String(1000))

    
    def __repr__(self) -> str:
        return f"Event(id={self.id!r}, name={self.name!r}, location={self.location!r})"


"""
rappel : client_name, client_contact_email, client_contact_phone : FK

"""

class Contract(Base):
    
    __tablename__ = 'contract'
    id: Mapped[int] = mapped_column(primary_key=True)

    client_id = mapped_column(ForeignKey("client.id"))
    #client: Mapped[client.Client()] = relationship(back_populates="contracts")
    client = relationship('Client', back_populates='contracts')

    commercial_contact_id = mapped_column(ForeignKey("staff.id"))
    commercial_contact = relationship('Staff', back_populates="contracts")

    event: Mapped["Event"] = relationship(back_populates="contract")
    
    total_amount : Mapped[int]
    balance_due : Mapped[int]
    date_creation : Mapped[date] = mapped_column(insert_default=func.now())
    status : Mapped[bool]

    def __repr__(self) -> str:
        return f"Contract(id={self.id!r}, client.fullname={self.client.fullname!r}), event={self.event!r})"

"""
rappel : contact_commercial : FK (= le commercial associé au
client) ;

statut (= si le contrat a été signé) : boolean

"""


class ClientRepository:

    def find_by_fullname(self, fullname):
        return SESSION.query(Client).filter(Client.fullname==fullname).first()
    
    
    def find_by_id(self, id) :
        return SESSION.query(Client).filter(Client.id==id).first()
    
    
    def find_by_email(self, email) :
        return SESSION.query(Client).filter_by(email=email).all()
    
    
    def get_all(self) :
        with ENGINE.connect() as conn:
            result = conn.execute(text("SELECT * FROM client"))
        return result
        #return session.query(cls).all()

    def create_client(self, session, datas, staff_id):
        client = Client(fullname=datas["fullname"], email=datas["email"], phone=datas["phone"], name_company=datas["name_company"], commercial_contact_id = staff_id )
        #client.commercial_contact = staff_id
        #session.merge(client)
        session.add(client)
        SESSION.commit() 


        
    def update(self, client_id, column, new_value):       
        client = SESSION.query(Client).filter_by(id=client_id).first()
        if column == "fullname":
            client.fullname = new_value
        if column == "email":
            client.email = new_value
        if column == "phone":
            client.phone = new_value
        if column == "name_company":
            client.name_company = new_value
        SESSION.commit()

        
        
    def delete(self, client):
        SESSION.delete(client)
        SESSION.commit() 
        

