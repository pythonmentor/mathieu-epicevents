from argon2 import PasswordHasher, exceptions
import jwt
import configparser
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from views.menu import Menu
from models.client import Client, ClientRepository
from views.display import Display
from models.staff import Staff
from datetime import datetime, timezone, timedelta
from controllers.menu_manager import password, SECRET, SESSION

config = configparser.ConfigParser()
config.read('config.ini')  
config_root = config["root"]
password = config_root["password"]
config_jwt = config["jwt"]
SECRET = config_jwt["secret"]
algo = config_jwt["algorithme"]
print("algo : ", algo)
engine = create_engine(f'mysql+pymysql://root:{password}@localhost/epic_events', echo=True)
Session = sessionmaker(bind=engine)
SESSION = Session()


staff_member = SESSION.query(Staff).filter_by(email="sarah@gmail.com").first()
#print("staff_member: ", staff_member)
department = staff_member.department.value
email = staff_member.email
password = staff_member.password
ph = PasswordHasher()
hash = ph.hash('essai')
#print("mdp haché : ", hash)


def get_all(session) :
    return session.query(Staff).all()

print(get_all(SESSION))

