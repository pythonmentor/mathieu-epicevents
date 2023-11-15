
from models.client import ClientRepository
from CONFIG import SESSION

class CrudManager:

    def __init__(self, table, datas):
        self.table = table
        self.datas = datas

    def create(self, table, datas):
        if self.table == "client":
            client = ClientRepository()
            return client.create_client(SESSION, datas)

