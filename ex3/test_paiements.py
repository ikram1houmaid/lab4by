
import unittest

from paiements import CarteBancaire, PayPal, Crypto


class TestPaiements(unittest.TestCase):

    def test_carte_bancaire(self):
        paiement = CarteBancaire(
            200, "4532015112830366", "123"
        )

        resultat = paiement.payer()

        self.assertIn("200.00", resultat)
        self.assertIn("Carte Bancaire", resultat)

    def test_paypal(self):
        paiement = PayPal(
            150, "test@gmail.com", "TOKEN123"
        )

        resultat = paiement.payer()

        self.assertIn("150.00", resultat)
        self.assertIn("PayPal", resultat)

    def test_crypto(self):
        paiement = Crypto(
            500, "WALLET001", "BTC"
        )

        resultat = paiement.payer()

        self.assertIn("500.00", resultat)
        self.assertIn("Crypto", resultat)

    def test_montant_negatif(self):
        with self.assertRaises(ValueError):
            PayPal(-100, "test@gmail.com", "TOKEN")

    def test_carte_invalide(self):
        with self.assertRaises(ValueError):
            CarteBancaire(200, "123456789", "123")

    def test_reseau_invalide(self):
        with self.assertRaises(ValueError):
            Crypto(300, "WALLET001", "XYZ")


if __name__ == "__main__":
    unittest.main()

