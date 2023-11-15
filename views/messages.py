

class Messages:
      
    def messages_ok(self, table, message_number):
        if message_number == 1:
            print(f'Le {table} a bien été enregistré')

    def message_error(self, message_number):
        if message_number == 1:
            print("Email ou mot de passe invalide")
        elif message_number == 2: 
            print ('Veuillez vous authentifier avec la commande "python -m epic_events login" !')
        elif message_number == 3:
            print("Vous n'êtes pas autorisé(e) à effectuer cette action.")
        