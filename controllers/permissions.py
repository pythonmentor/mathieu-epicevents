import jwt
from sqlalchemy import Column, Integer, String, func, ForeignKey, Table, Enum, update, text, insert
from settings import SECRET, SESSION, ENGINE
from views.login import ViewLogin
from views.messages import Messages

class Permissions:

    def __init__(self):
        self.messages=Messages()

    def check_token_validity(self, token):
        try:
            return jwt.decode(token, SECRET, algorithms="HS256")
        except jwt.ExpiredSignatureError:
            self.messages.message_error(message_number=2)
            return False
        
    def permission_create(self, token, table):
        if self.check_token_validity(token):
            token_decode = self.check_token_validity(token)
            department = token_decode['department']
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
            department = token_decode['department']
            print("department : ", department)
            if table == "client":
                print (department == "commercial" and self.is_own_client(staff_id, client_id,))
                return department == "commercial" and self.is_own_client(staff_id, client_id,)
        else:
            return False
                    


    def is_own_client(self, staff_id, client_id):

        with ENGINE.connect() as conn:
            result = conn.execute(text(f"SELECT * FROM client JOIN staff ON client.contact_commercial_id = staff.id WHERE staff.id = {staff_id};"))
        for row in result:
            return client_id == row[0]
        
                






