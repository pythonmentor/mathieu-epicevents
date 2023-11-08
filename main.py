import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from models.client import Client, Base
from models.contract import Contract
from models.staff import Staff
from models.event import Event
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, Text, String, func, ForeignKey
from typing import List, Optional
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship

config = configparser.ConfigParser()
config.read('config.ini')  
config_root = config["root"]
password = config_root["password"]


# L’attribut echo=True oblige SQLAlchemy à enregistrer toutes les commandes SQL qu’il exécute
engine = create_engine(f'mysql+pymysql://root:{password}@localhost/epic_events', echo=True)
conn = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)


staff_support1 = Staff(name="Connor", first_name="Sarah", email="sarah@gmail.com", password="sarah", department="support")
session.add(staff_support1)
session.commit() 
client1 = Client(fullname='John Snow', email="john@life.fr", phone=215452014, name_company="Entreprise Coucou")
client1 = Client(fullname='John Snow', email="john@life.fr", phone=215452014, name_company="Entreprise Coucou", staff_member_commercial=staff_member_support1.id)
session.add(client1)
session.commit() 
staff_support1.clients.add(client1.id)

session.commit()
   
"""
if __name__ == "__main__":
    main()
"""
