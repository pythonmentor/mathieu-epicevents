import jwt
from CONFIG import SECRET, SESSION
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
        
    def permission_update(self, user_id, token, table):
         
        if self.check_token_validity(token):
            token_decode = self.check_token_validity(token)
            department = token_decode['department']
            if table == "client":
                if department == "commercial":
                    pass






