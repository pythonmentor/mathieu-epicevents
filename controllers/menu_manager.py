import configparser
import jwt
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from views.menu import Menu
from models.client import Client, ClientRepository
from models.staff import Staff, StaffRepository
from views.display import Display
from CONFIG import SESSION, SECRET


class MenuManager:
    def __init__(self, token):
        self.token = token
        self.menu = Menu()
        self.display=Display()

    def choice_main_menu(self):
        """
        Activation des méthodes selon le choix de l'utilisateur
        au menu principal 
        """
        option = self.menu.main_menu()
        if option == 1:
            self.choice_submenu("client")
        elif option == 2:
            self.choice_menu_event("event")
        elif option == 3:
            self.choice_menu_contract("contract")
        elif option == 4:
            self.choice_menu_staff("staff")
        elif option == 5:
            exit()

    def choice_submenu(self, table):
        option = self.menu.submenu(table)
        if option == 1:
            return self.read_only(table)
        if option == 2:
            datas = self.menu.get_create_datas(table)

    def read_only(self, table):
        print("read_only")
        option = self.menu.menu_read_only(table)
        if self.check_token_validity():
            repository = ClientRepository()
            if option == 1:
                query = repository.get_all()
                self.display.display_all_table(query)
                
                return self.choice_main_menu()
            if option == 2:
                fullname = self.menu.get_fullname()
                repository = ClientRepository()
                query = repository.find_by_fullname(fullname)
                self.display.display_one_object(query)
                return self.choice_main_menu()
            if option == 3:
                id = self.menu.get_id()
                repository = ClientRepository()
                query = repository.find_by_id(id)
                self.display.display_one_object(query)
                return self.choice_main_menu()


    def check_token_validity(self):
        try:
            return jwt.decode(self.token, SECRET, algorithms="HS256")
        except jwt.ExpiredSignatureError:
            self.menu.message_error(message_number=2)
            return self.check_password()


    



   


