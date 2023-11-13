from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from argon2 import PasswordHasher, exceptions
from main import password, secret, algo, session
from models.staff import Staff
import jwt
from datetime import datetime, timezone, timedelta

class Authentication:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.ph = PasswordHasher()

    def create_token(self, department):
        encoded_jwt = jwt.encode({"exp": datetime.now()+ timedelta(seconds=60), "department": department}, secret, algorithm=algo)
        return encoded_jwt

    def check_password(self, password_user):
        email = "email"
        password_user = self.hash_password(password_user)
        engine = create_engine(f'mysql+pymysql://root:{password}@localhost/epic_events', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        query = session.query(Staff).filter_by(email='email')
        department = query.department
        if query.email == email and query.password == password :
            token = self.create_token()

    def hash_password(self, password):
        hash = self.ph.hash(f'{password}')
        return hash
    

#class Permissions:
