from views.menu import Menu
from views.get_datas import GetDatas
from views.messages import Messages
from models import models
from views.display import Display
from settings import SESSION
from controllers.permissions import Permissions
from controllers.crud_manager import CrudManager


class MenuManager:
    def __init__(self, staff_id, token):
        self.token = token
        self.menu = Menu()
        self.messages = Messages()
        self.display=Display()
        self.get_datas = GetDatas()
        self.permissions = Permissions()
        self.crud = CrudManager(staff_id, token)
        self.staff_id = staff_id
       

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
            SESSION.close()
            exit()

    def choice_submenu(self, table):
        option = self.menu.submenu(table)
        # Option 1 = Consulter. Dans ce cas, seul la validité du token est vérifiée car tous les collaborateurs authentifiés sont autorisées à lire les données
        
        if option == 1:
            self.manager_menu_read_only(table)
            return self.choice_main_menu()
        elif option == 2:
            if self.crud.create(table):
                print("menumanager")
                self.messages.messages_ok(table, 1)
                return self.choice_main_menu()
        elif option == 3:
            if self.crud.modify(table):
                self.messages.messages_ok(table, 2)
                return self.choice_main_menu()
            else: 
                self.messages.message_error(3)
                return self.choice_main_menu()

        elif option == 4:
            pass
        else:
            self.messages.message_error(3)
            return self.choice_main_menu()
    

    def manager_menu_read_only(self, table):
        print("read_only")
        option = self.menu.view_menu_read_only(table)
        if self.permissions.check_token_validity(self.token):
            client_repository = models.ClientRepository()
            if option == 1:
                query = client_repository.get_all()
                self.display.display_all_table(query)
                
            if option == 2:
                fullname = self.get_datas.get_fullname()
                client_repository = models.ClientRepository()
                query = client_repository.find_by_fullname(fullname)
                self.display.display_one_object(query)
                
            if option == 3:
                id = self.get_datas.get_id()
                client_repository = models.ClientRepository()
                query = client_repository.find_by_id(id)
                self.display.display_one_object(query)
            
    
        
        



    


    



   


