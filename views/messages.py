
class Messages:

    def messages_ok(self, table, message_number):
        if message_number == 1:
            print(f'Le {table} a bien été enregistré')
        if message_number == 2:
            print(f'Le {table} a bien été modifié')

    def message_error(self, table, message_number):
        if message_number == 1:
            print("Email ou mot de passe invalide")
        elif message_number == 2:
            print(
                "Veuillez fermer l'application et vous authentifier de nouveau avec la commande"
                "'pipenv run python main.py'"
            )
        elif message_number == 3:
            print(f"Ce {table} est inconnu.")
        elif message_number == 4:
            print("Vous n'êtes pas autorisé(e) à effectuer cette action.")
