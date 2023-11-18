from views.menu import Menu


class GetDatas:

    def __init__(self):
        self.menu = Menu()
    
    def get_fullname(self):
        name = input("Nom : ").capitalize()
        firstname = input ("Prénom : ").capitalize()
        fullname = firstname+" "+name
        return fullname
        
    def get_id(self):
        id = int(input("N° du client:"))
        return id
    
    def get_create_datas(self, table):
        if table == 'client':
            print("Veuillez taper les données suivantes.")
            fullname = self.get_fullname()
            email = input("Email : ")
            phone = input("Phone : ")
            name_company = input("Name company : ")
            datas = {"fullname" : fullname, "email": email, "phone": phone, "name_company": name_company}
            return datas
        
    def get_new_value(self): 
        new_value = input("Veuillez entrer la nouvelle valeur : ")
        return new_value


           