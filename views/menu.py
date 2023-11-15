import os
import platform
import time



class Menu:
    def main_menu(self):
        """
        Affiche le menu principal
        retourne le choix de l'utilisateur
        """

        print()
        while True:
            menu_options = {1: "Clients", 2: "Evènements", 3: "Contrats", 4: "collaborateurs: ", 5: "Fermer"}
            print("****Menu principal****")
            print()
            for key in menu_options:
                print(key, "--", menu_options[key])
                print()
            try:
                option = int(input("Entrer votre choix : "))
            except ValueError:
                print("Vous devez taper un nombre entre 1 et 5.")
                time.sleep(2)
                self.clean()
                print()
            else:
                for key in menu_options:
                    if option == key:
                        self.clean()
                        return option
                print("Option invalide. Merci d'entrer un nombre entre 1 et 5")
                time.sleep(2)
                self.clean()
                print()

   
    def submenu(self, table):
        """
        Affiche le sous menu (client ou contrat ou évenènement ou collaborateur)
        retourne le choix de l'utilisateur
         """
        while True:
            print()
            print(f'*****Menu {table}*****')
            print()
            menu_options = {
                1: "Consulter",
                2: "Créer",
                3: "Modifier",
                4: "Supprimer un compte collaborateur",
                5: "Retour au menu principal",
                6: "Fermer",
               
            }
            for key in menu_options:
                print(key, "--", menu_options[key])
                print()
            try:
                option = int(input("Entrer votre choix : "))
            except ValueError:
                print("Vous devez taper un nombre entre 1 et 6.")
                time.sleep(2)
                self.clean()
                print()
            else:
                for key in menu_options:
                    if option == key:
                        self.clean()
                        return option
                print()
                print("Option invalide. Merci d'entrer un nombre entre 1 et 6")
                time.sleep(2)
                self.clean()
                print()

    
    def view_menu_read_only(self,name_submenu):
        """
        Affiche le sous menu (client ou contrat ou évenènement ou collaborateur)
        retourne le choix de l'utilisateur
         """
        while True:
            print()
            print(f'*****Consulter {name_submenu}*****')
            print()
            menu_options = {
                1: f"Afficher tous les {name_submenu}s",
                2: f'Chercher un {name_submenu} par son nom complet',
                3: f'Chercher un {name_submenu} par son numéro de compte(id)',
                4: "Retour au menu principal",
                5: "Fermer",
               
            }
            for key in menu_options:
                print(key, "--", menu_options[key])
                print()
            try:
                option = int(input("Entrer votre choix : "))
                return option
            except ValueError:
                print("Vous devez taper un nombre entre 1 et 5.")
                time.sleep(2)
                self.clean()
                print()
          

    def clean(self):
        """Fonction qui efface l'affichage de la console"""
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Linux":
            os.system("clear")

            
            
            

            


