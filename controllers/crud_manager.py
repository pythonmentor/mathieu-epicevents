
from models.client import ClientRepository
from controllers.permissions import Permissions
from views.menu import Menu
from views.get_datas import GetDatas
from settings import SESSION

class CrudManager:

    def __init__(self, staff_id, token):
        self.staff_id = staff_id
        self.token = token
        self.menu = Menu()
        self.permissions = Permissions()
        self.get_datas = GetDatas()

    def create(self, table):
        if self.permissions.permission_create(self.token, table):
            datas = self.get_datas.get_create_datas(table)
            if table == "client":
                client = ClientRepository()
                return client.create_client(SESSION, datas, self.staff_id)
        return False
        
    def modify(self, table):
        if table == "client":
            fullname = self.get_datas.get_fullname()
            client_repository = ClientRepository()
            client = client_repository.find_by_fullname(fullname)
            if self.permissions.permission_update(self.staff_id, client.id, self.token, table):
                column_to_update = self.menu.choice_column_to_update_client()
                new_value = self.get_datas.get_new_value()
                if column_to_update == "phone":
                    new_value = int(new_value)
                return client_repository.update(client.id, column_to_update, new_value)
            else:
                return False

