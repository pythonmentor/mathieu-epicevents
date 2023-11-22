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
            if table == "client" or table == "event":
                if department == "commercial":
                    return True
                else:
                    return False
            elif table == "contract" and department == "management":
                return True
            else:
                return False
        else:
            return False

    def permission_update(self, staff_id, object_id, token, table):
        if self.check_token_validity(token):
            token_decode = self.check_token_validity(token)
            department = token_decode["department"]
            print("department : ", department)
            if table == "client":
                return department == "commercial" and self.is_own_client(staff_id, object_id)
            elif table == "event" and department == "support":
                return self.is_their_event(staff_id, object_id)
            elif (table == "event" or table == "contract") and department == "management":
                return True
            elif table == "contract" and department == "commercial" and self.is_own_client(staff_id, object_id):
                return True
            else:
                return False
        else:
            return False

    def is_own_client(self, staff_id, client_id):
        staff_member = SESSION.get(Staff, staff_id)
        clients = staff_member.clients
        for client in clients:
            if client.id == client_id:
                return True
        return False

    def is_their_event(self, staff_id, event_id):
        staff_member = SESSION.get(Staff, staff_id)
        events = staff_member.events
        for event in events:
            if event.id == event_id:
                return True
        return False
