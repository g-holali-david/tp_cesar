class ChiffreCesar:
    def __init__(self, decalage: int):
        """
        Initialisation de l'objet avec un décalage.
        """
        self.set_decalage(decalage)

    def set_decalage(self, decalage: int):
        """
        Assure que le décalage est un entier valide entre 1 et 25.
        """
        if not isinstance(decalage, int):
            raise ValueError("Le décalage doit être un entier.")
        self.decalage = decalage

    def chiffrer(self, message: str) -> str:
        """
        Fonction de chiffrement avec le Chiffre de César.
        Chiffre tout caractère, y compris les caractères accentués.
        """
        if not isinstance(message, str):
            raise ValueError("Le message doit être une chaîne de caractères.")
        
        result = []
        for char in message:
            # Appliquer le décalage sur le code Unicode de chaque caractère
            new_char = chr((ord(char) + self.decalage) % 1114112)  # 1114112 = 2^20, max code Unicode
            result.append(new_char)
        
        return ''.join(result)

    def dechiffrer(self, message_chiffre: str) -> str:
        """
        Fonction de déchiffrement avec le Chiffre de César.
        Applique un décalage inverse pour déchiffrer tout caractère.
        """
        if not isinstance(message_chiffre, str):
            raise ValueError("Le message chiffré doit être une chaîne de caractères.")
        
        # Appliquer un décalage inverse pour déchiffrer
        self.decalage = -self.decalage
        return self.chiffrer(message_chiffre)  # Utiliser chiffrer avec le décalage négatif

    def brute_force_attack(self, message_chiffre: str):
        """
        Tentative de déchiffrement sans connaître le décalage en essayant tous les décalages.
        """
        if not isinstance(message_chiffre, str):
            raise ValueError("Le message chiffré doit être une chaîne de caractères.")
        
        for decalage in range(1, 26):
            self.decalage = decalage
            try_message = self.dechiffrer(message_chiffre)
            print(f"Déchiffré avec un décalage de {decalage}: {try_message}")
        return "Fin de l'attaque brute-force."
    
    
