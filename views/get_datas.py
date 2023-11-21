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
            id = int(input("N° du client:"))
            return id
        elif table == "event":
            id = int(input("N° de l'évènement : "))
            return id

    def get_create_datas(self, table):
        if table == "client":
            print("Veuillez taper les données suivantes.")
            fullname = self.get_fullname()
            email = input("Email : ")
            try:
                phone = int(input("Téléphone : "))
            except ValueError:
                print("Le n° de téléphone doit être composé uniquement de chiffres, sans espaces.")
                phone = input("Téléphone : ")
            name_company = input("Nom de l'entreprise : ")
            datas = {"fullname": fullname, "email": email, "phone": phone, "name_company": name_company}
            return datas
        if table == "event":
            print("Veuillez taper les données suivantes.")
            name = input("Nom de l'évènement : ")
            contract_id = input("numéro (id) du contrat : ")
            print("Indiquer la date et l'heure du début de l'évènement : ")
            year = input("année : ")
            month = input("mois : ")
            day = input("jour : ")
            hour = input("heure : ")
            event_date_start = f"{year}-{month}-{day} {hour}:00"
            print("Indiquer la date et l'heure de la fin de l'évènement : ")
            year = input("année : ")
            month = input("mois : ")
            day = input("jour : ")
            hour = input("heure : ")
            event_date_end = f"{year}-{month}-{day} {hour}:00"
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

    def get_new_value(self):
        new_value = input("Veuillez entrer la nouvelle valeur : ")
        return new_value
    
    def get_support_contact(self):
        support_contact = input("Veuillez taper le nom ou l'id du collaborateur support de l'évènement")
        return support_contact

