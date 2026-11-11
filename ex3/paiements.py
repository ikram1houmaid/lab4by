
from abc import ABC, abstractmethod


# Classe abstraite Paiement
class Paiement(ABC):

    def __init__(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif")

        self._montant = montant

    @abstractmethod
    def payer(self):
        pass


# Classe CarteBancaire
class CarteBancaire(Paiement):

    def __init__(self, montant, numero, cvv):
        super().__init__(montant)

        if not self.verifier_luhn(numero):
            raise ValueError("Numéro de carte invalide")

        if not (cvv.isdigit() and len(cvv) == 3):
            raise ValueError("CVV invalide")

        self.numero = numero
        self.cvv = cvv

    @staticmethod
    def verifier_luhn(numero):
        if not numero.isdigit():
            return False

        chiffres = [int(c) for c in numero]
        somme = 0

        for i, chiffre in enumerate(reversed(chiffres)):
            if i % 2 == 1:
                chiffre *= 2
                if chiffre > 9:
                    chiffre -= 9

            somme += chiffre

        return somme % 10 == 0

    def payer(self):
        return f"Paiement par Carte Bancaire de {self._montant:.2f} DH confirmé."


# Classe PayPal
class PayPal(Paiement):

    def __init__(self, montant, email, token):
        super().__init__(montant)

        if "@" not in email:
            raise ValueError("Email invalide")

        if not token:
            raise ValueError("Token API obligatoire")

        self.email = email
        self.token = token

    def payer(self):
        return f"Paiement par PayPal de {self._montant:.2f} DH confirmé."


# Classe Crypto
class Crypto(Paiement):

    def __init__(self, montant, wallet_id, reseau):
        super().__init__(montant)

        if not wallet_id:
            raise ValueError("Wallet ID obligatoire")

        if reseau not in ["BTC", "ETH"]:
            raise ValueError("Réseau non valide")

        self.wallet_id = wallet_id
        self.reseau = reseau

    def payer(self):
        return f"Paiement par Crypto ({self.reseau}) de {self._montant:.2f} DH confirmé."


# Fonction de traitement polymorphique
def traiter_paiements(liste):
    for paiement in liste:
        print(paiement.payer())


# Programme principal
if __name__ == "__main__":

    paiements = [

        CarteBancaire(200, "4532015112830366", "123"),
        CarteBancaire(350, "4716108999716531", "456"),

        PayPal(150, "ikram@gmail.com", "TOKEN123"),
        PayPal(250, "client@gmail.com", "TOKEN456"),

        Crypto(500, "WALLET001", "BTC"),
        Crypto(700, "WALLET002", "ETH")
    ]

    print("=== TRAITEMENT DES PAIEMENTS ===")

    traiter_paiements(paiements)
