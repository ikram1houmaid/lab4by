
from abc import ABC, abstractmethod
import math


# Classe abstraite Forme
class Forme(ABC):

    @abstractmethod
    def aire(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} – aire : {self.aire():.2f}"


# Classe Cercle
class Cercle(Forme):

    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2


# Classe Rectangle
class Rectangle(Forme):

    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur


# Classe Triangle
class Triangle(Forme):

    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return 0.5 * self.base * self.hauteur


# Extension 1 : classe Carre
class Carre(Rectangle):

    def __init__(self, cote):
        if cote <= 0:
            raise ValueError("Le côté doit être positif")

        super().__init__(cote, cote)


# Extension 2 : ColorMixin
class ColorMixin:

    def __init__(self, couleur="Blanc", **kwargs):
        self.couleur = couleur
        super().__init__(**kwargs)

    def __str__(self):
        return f"{super().__str__()} – couleur : {self.couleur}"


# Classe colorisée
class CercleColorise(ColorMixin, Cercle):

    def __init__(self, rayon, couleur="Blanc"):
        super().__init__(couleur=couleur)
        self.rayon = rayon


# Programme principal
if __name__ == "__main__":

    formes = [
        Cercle(3),
        Rectangle(4, 5),
        Triangle(6, 2),
        Carre(4),
        CercleColorise(2, "Rouge")
    ]

    print("=== Calcul des aires ===")

    for f in formes:
        print(f)

    print("\n=== Tests unitaires ===")

    import unittest

    class TestFormes(unittest.TestCase):

        def test_cercle(self):
            self.assertAlmostEqual(Cercle(3).aire(), math.pi * 9)

        def test_rectangle(self):
            self.assertEqual(Rectangle(4, 5).aire(), 20)

        def test_triangle(self):
            self.assertEqual(Triangle(6, 2).aire(), 6)

        def test_carre(self):
            self.assertEqual(Carre(4).aire(), 16)

        def test_carre_invalide(self):
            with self.assertRaises(ValueError):
                Carre(0)

        def test_cercle_colorise(self):
            cercle = CercleColorise(2, "Rouge")
            self.assertAlmostEqual(cercle.aire(), math.pi * 4)
            self.assertEqual(cercle.couleur, "Rouge")

    unittest.main(argv=[""], exit=False)
