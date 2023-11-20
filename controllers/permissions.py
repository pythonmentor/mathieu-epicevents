import jwt
from settings import SECRET, SESSION
from views.messages import Messages
from models.models import Staff


class Permissions:
    def __init__(self):
        self.messages = Messages()

    def check_token_validity(self, token):
        try:
            return jwt.decode(token, SECRET, algorithms="HS256")
        except jwt.ExpiredSignatureError:
            self.messages.message_error(message_number=2)
            return False

    def permission_create(self, token, table):
        if self.check_token_validity(token):
            token_decode = self.check_token_validity(token)
            department = token_decode["department"]
            if table == "client":
                if department == "commercial":
                    return True
                elif department == "support":
                    return False
                elif department == "gestion":
                    return False
        else:
            return False

    def permission_update(self, staff_id, client_id, token, table):
        if self.check_token_validity(token):
            token_decode = self.check_token_validity(token)
            department = token_decode["department"]
            print("department : ", department)
            if table == "client":
                print(
                    "permission : ",
                    department == "commercial"
                    and self.is_own_client(
                        staff_id,
                        client_id,
                    ),
                )
                return department == "commercial" and self.is_own_client(
                    staff_id,
                    client_id,
                )
        else:
            return False

    def is_own_client(self, staff_id, client_id):
        staff_member = SESSION.get(Staff, staff_id)
        clients = staff_member.clients
        for client in clients:
            if client.id == client_id:
                return True
        return False
