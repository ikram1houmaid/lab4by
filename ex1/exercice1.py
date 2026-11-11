
# Classe mère Animal
class Animal:
    def parler(self):
        raise NotImplementedError("Cette méthode doit être redéfinie")


# Classe Chien
class Chien(Animal):
    def parler(self):
        return "Ouaf !"


# Classe Chat
class Chat(Animal):
    def parler(self):
        return "Miaou !"


# Extension : classe Vache
class Vache(Animal):
    def parler(self):
        return "Meuh !"


# Fonction qui utilise le polymorphisme
def faire_parler(animal):
    print(animal.parler())


# Extension : classe Robot (Duck Typing)
class Robot:
    def parler(self):
        return "Bonjour, je suis un robot !"


# Programme principal
animaux = [
    Chien(),
    Chat(),
    Chien(),
    Vache()
]

print("=== Polymorphisme avec les animaux ===")

for animal in animaux:
    faire_parler(animal)


print("\n=== Duck Typing avec Robot ===")

robot = Robot()
faire_parler(robot)


print("\n=== Collection complète ===")

collection = [
    Chien(),
    Chat(),
    Vache(),
    Robot()
]

for element in collection:
    faire_parler(element)
