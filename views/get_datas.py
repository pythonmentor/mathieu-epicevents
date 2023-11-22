import re
from views.menu import Menu


class GetDatas:
    def __init__(self):
        self.menu = Menu()

    def get_fullname(self):
        print("Veuillez taper le nom complet du client.")
        name = input("Nom : ").capitalize()
        firstname = input("Prénom : ").capitalize()
        fullname = firstname + " " + name
        return fullname

    def get_name_event(self):
        print("Veuillez taper le nom de l'évènement.")
        name_event = input("Nom : ").capitalize()
        return name_event

    def get_id(self, table):
        if table == "client":
            id_str = input("N° (id) du client :")
        elif table == "event":
            id_str = input("N° (id) de l'évènement :")
        id = self.chek_id(id_str)
        return id

    def get_create_datas(self, table):
        if table == "client":
            print("Veuillez taper les données suivantes.")
            fullname = self.get_fullname()
            email_input = input("Email : ")
            email = self.chek_email(email_input)
            phone_input = int(input("Téléphone : "))
            phone = self.check_phone(phone_input)
            name_company = input("Nom de l'entreprise : ")
            datas = {"fullname": fullname, "email": email, "phone": phone, "name_company": name_company}
            return datas
        elif table == "event":
            print("Veuillez taper les données suivantes.")
            name = input("Nom de l'évènement : ")
            contract_id = input("numéro (id) du contrat : ")
            print("Indiquer la date et l'heure du début de l'évènement : ")
            event_date_start = self.get_datetime()
            print("Indiquer la date et l'heure de la fin de l'évènement : ")
            event_date_end = self.get_datetime()
            location = input("lieu : ")
            attendees = input("Nombre de personnes estimé : ")
            notes = input("Notes : ")
            datas = {
                "name": name,
                "contract_id": contract_id,
                "event_date_start": event_date_start,
                "event_date_end": event_date_end,
                "location": location,
                "attendees": attendees,
                "notes": notes,
            }
            return datas

        elif table == "contract":
            print("Veuillez taper les données suivantes.")
            client_id = input("N° (id) du client : ")
            total_amount = input("Montant total : ")
            total_amount = self.chek_number(total_amount)
            balance_due = input("Montant restant à payer : ")
            balance_due = self.chek_number(balance_due)
            status_input = input("Contrat signé? Taper 1 pour OUI, 2 pour NON : ")
            status = self.check_status(status_input)
            datas = {
                "client_id": client_id,
                "total_amount": total_amount,
                "balance_due": balance_due,
                "status": status,
            }
            return datas

    def get_datetime(self):
        year = input("année (ex : 2023) : ")
        month = input("mois (ex : 01): ")
        day = input("jour (ex : 04): ")
        hour = input("heure (ex : 14): ")
        date_time = f"{year}-{month}-{day} {hour}:00"
        return date_time

    def chek_email(self, email):
        while re.fullmatch(r"[a-z0-9._-]+@[a-z0-9._-]+\.[a-z0-9._-]+", email) is None:
            print("Veuillez taper un email valide. Exemple : alice@gmail.com")
            email = input("Email : ")
        return email

    def chek_id(self, id):
        while re.fullmatch(r"[0-9]", id) is None:
            print("Veuillez taper un nombre entre 0 et 9")
            id = input("id : ")
        return int(id)

    def chek_phone(self, phone):
        while re.fullmatch(r"[0-9]+", phone) is None:
            print("Le n° de téléphone doit être composé uniquement de chiffres, sans espaces.")
            phone = input("N° de téléphone : ")
        return int(phone)

    def chek_number(self, number_input):
        while re.fullmatch(r"[0-9]+", number_input) is None:
            print("Le montant doit être composé uniquement de chiffres, sans espaces.")
            number_input = input("Montant : ")
        return int(number_input)

    def check_status(self, status_input):
        while re.fullmatch(r"[1-2]", status_input) is None:
            print()
            status_input = input("Contrat signé? Merci de taper 1 pour OUI ou 2 pour NON : ")
            if status_input == 1:
                return "true"
            elif status_input == 2:
                return "false"

    def get_new_value(self, column):
        new_value = input("Veuillez entrer la nouvelle valeur : ")
        if column == "email":
            email = self.chek_email(new_value)
            return email
        if column == "phone":
            phone = self.chek_phone(new_value)
            return phone
        else:
            return new_value

    def get_support_contact(self):
        support_contact = input("Veuillez taper le nom ou l'id du collaborateur support de l'évènement")
        return support_contact
