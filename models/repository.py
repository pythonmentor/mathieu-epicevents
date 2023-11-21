from sqlalchemy import text
from settings import SESSION, ENGINE
from .models import Client, Event, Staff


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

    def update_client(self, client_id, column, new_value):
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


class EventRepository:
    def find_by_name(self, name):
        return SESSION.query(Event).filter(Event.name == name).first()

    def find_by_id(self, id):
        return SESSION.query(Event).filter(Event.id == id).first()

    def find_by_client(self, client_id):
        return SESSION.query(Event).filter_by(client_id=client_id).all()

    def get_all(self):
        """
        with ENGINE.connect() as conn:
            result = conn.execute(text("SELECT * FROM event"))
        return result
        """
        return SESSION.query(Event).all()

    def create_event(self, session, datas, client_id):
        event = Event(
            name=datas["name"],
            contract_id=datas["contract_id"],
            client_id=client_id,
            
            event_date_start=datas["event_date_start"],
            event_date_end=datas["event_date_end"],
            location=datas["location"],
            attendees=datas["attendees"],
            notes=datas["notes"],
        )
        session.add(event)
        SESSION.commit()

    def update_event(self, event_id, column, new_value):
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

    """
    def delete(self, client):
        SESSION.delete(client)
        SESSION.commit()
    """


class StaffRepository:
    def find_by_name(self, name):
        return SESSION.query(Staff).filter(Event.name == name).first()