from sqlalchemy import text
from settings import SESSION, ENGINE
from .models import Client


class ClientRepository:
    def find_by_fullname(self, fullname):
        
        return SESSION.query(Client).filter(Client.fullname == fullname).first()

    def find_by_id(self, id):
        return SESSION.query(Client).filter(Client.id == id).first()

    def find_by_email(self, email):
        return SESSION.query(Client).filter_by(email=email).all()

    def get_all(self):
        with ENGINE.connect() as conn:
            result = conn.execute(text("SELECT * FROM client"))
        return result
        # return session.query(cls).all()

    def create_client(self, session, datas, staff_id):
        client = Client(
            fullname=datas["fullname"],
            email=datas["email"],
            phone=datas["phone"],
            name_company=datas["name_company"],
            commercial_contact_id=staff_id,
        )
        # client.commercial_contact = staff_id
        # session.merge(client)
        session.add(client)
        SESSION.commit()

    def update(self, client_id, column, new_value):
        client = SESSION.query(Client).filter_by(id=client_id).first()
        if column == "fullname":
            client.fullname = new_value
        if column == "email":
            client.email = new_value
        if column == "phone":
            client.phone = new_value
        if column == "name_company":
            client.name_company = new_value
        SESSION.commit()

    def delete(self, client):
        SESSION.delete(client)
        SESSION.commit()
