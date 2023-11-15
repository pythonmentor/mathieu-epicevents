import os
import platform

class ViewLogin:

    def get_email(self):
        #self.clean()
        print("Veuillez taper vos identifiants.")
        print()
        email = input("Email : ")
        print()
        return email
        
    
    def get_password(self):
        print()
        password = input("Password : ")
        return password
    
    

    def clean(self):
        """Fonction qui efface l'affichage de la console"""
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Linux":
            os.system("clear")
         




      