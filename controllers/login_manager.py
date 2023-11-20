from argon2 import PasswordHasher
from settings import password, SECRET, SESSION
import jwt
from datetime import datetime, timedelta
from controllers.menu_manager import MenuManager
from views.menu import Menu
from views.login import ViewLogin
from views.messages import Messages
from models.models import Staff

class AuthenticationAndPermissions:

    def __init__(self):
        self.menu=Menu()
        self.messages = Messages()
        self.password = password
        self.ph = PasswordHasher()

    def create_token(self, department):
        encoded_jwt = jwt.encode({"exp": datetime.now()+ timedelta(seconds=60), "department": department}, SECRET, algorithm="HS256")
        return encoded_jwt

    def hash_password(self, password):
        hash = self.ph.hash(f'{password}')
        return hash
    
    def check_password(self):
        login = ViewLogin()
        email = login.get_email()
        print(email)
        password = login.get_password()
        password_user = self.hash_password(password)
        staff_member = SESSION.query(Staff).filter_by(email=email).first()
        #print("staff_member: ", staff_member)
        if staff_member and staff_member.email == email and staff_member.password == password :
            user_id = staff_member.id
            department = staff_member.department.value
            token = self.create_token(department)
            menu_manager = MenuManager(user_id, token)
            print("token :", token)
            return menu_manager.choice_main_menu()
            
        else:
            self.messages.message_error(1)
            return self.check_password()
        

    