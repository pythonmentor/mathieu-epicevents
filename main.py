import configparser
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from models.client import Client, Base
from models.contract import Contract
from models.staff import Staff
from models.event import Event
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine, Column, Integer, Text, String, func, ForeignKey
from typing import List, Optional
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship

config = configparser.ConfigParser()
config.read('config.ini')  
config_root = config["root"]
password = config_root["password"]
config_jwt = config["jwt"]
secret = config_jwt["secret"]
algo = config_jwt["algorithme"]
Session = sessionmaker(bind=engine)
session = Session()

def main():
    Base.metadata.create_all(engine)



session.add(staff_support1)
session.commit() 
staff_support1.clients.add(client1.id)

   
"""
if __name__ == "__main__":
    main()
"""
