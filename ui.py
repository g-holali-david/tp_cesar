# interface.py

from cesar import ChiffreCesar

class Ui:
    def __init__(self):
        self.cesar = None

    def afficher_menu(self):
        """
        Interface utilisateur pour choisir entre chiffrement et déchiffrement
        """
        print("Bienvenue dans le Chiffre de César !")
        while True:
            print("\nChoisissez une option :")
            print("1. Chiffrer un message")
            print("2. Déchiffrer un message")
            print("3. Attaque brute-force sur un message chiffré")
            print("4. Quitter")

            option = input("Entrez le numéro de l'option: ")

            if option == '1':
                self.chiffrer_message()

            elif option == '2':
                self.dechiffrer_message()

            elif option == '3':
                self.attaque_brute_force()

            elif option == '4':
                print("Au revoir!")
                break
            else:
                print("Option invalide. Essayez de nouveau.")

    def chiffrer_message(self):
        """
        Fonction pour gérer le chiffrement du message
        """
        message = input("Entrez le message à chiffrer: ")
        decalage = int(input("Entrez le décalage: "))
        self.cesar = ChiffreCesar(decalage)
        print(f"Message chiffré: {self.cesar.chiffrer(message)}")

    def dechiffrer_message(self):
        """
        Fonction pour gérer le déchiffrement du message
        """
        message_chiffre = input("Entrez le message chiffré à déchiffrer: ")
        decalage = int(input("Entrez le décalage: "))
        self.cesar = ChiffreCesar(decalage)
        print(f"Message déchiffré: {self.cesar.dechiffrer(message_chiffre)}")

    def attaque_brute_force(self):
        """
        Fonction pour gérer l'attaque brute-force sur un message chiffré
        """
        message_chiffre = input("Entrez le message chiffré à attaquer: ")
        print(self.cesar.brute_force_attack(message_chiffre))
