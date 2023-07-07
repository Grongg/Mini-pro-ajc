class Homme1:
    def __init__(self, nom="Ali", age=14):
        self.nom = nom
        self.age = age

class Homme2:
    def __init__(self, nom="Jhon", prenom="Doe", age=18, taille=100, poids=100):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
        self.__taille = taille
        self.__poids = poids
    def getNom(self):
        #print("voici le nom:", self.__nom)
        return self.__nom
    def setNom(self, nom):
        self.__nom = nom
        #print("voici le nouveau nom:", self.__nom)
        return self.__nom
    def getAge(self):
        print("voici le nom:", self.__age)
        return self.__age
    def setAge(self, age):
        self.__age = age
        print("voici le nouveau nom:", self.__age)
        return self.__age

class Animal:
    
    def __init__(self, nom, couleur, genre):
        self.nom = nom
        self.couleur = couleur
        self.genre = genre
    
    def display(self):
        print("\nnom:", self.nom)
        print("couleur:", self.couleur)
        print("genre:", self.genre)
        pass

    def manger(self):
        return "Je mange un peu de tout !"

class Carnivore(Animal):
    
    def __init__(self, nom, couleur, genre):
        super().__init__(nom, couleur, genre)
    
    def manger(self):
        return "Je mange de la viande"
    
class CarniSauvage(Carnivore):
    
    """Classe d\'animaux sauvages qui sont aussi carnivores."""
    
    def __init__(self, nom, couleur, genre):
        super().__init__(nom, couleur, "sauvage")

    
    def parler(self):
        print("Je vis dans la fôret !")
        pass

from abc import ABC, abstractmethod

class EtreVivant(ABC):
    
    @abstractmethod
    def manger(self):
        pass
    
    @abstractmethod
    def deplacer(self):
        pass
    
    @abstractmethod
    def description(self):
        pass
    
class Reptile(EtreVivant):

    def manger(self):
        print("oui, je mange !")
        pass
    
    def deplacer(self):
        print("oui, je me deplace !")
        pass
    
    def description(self):
        print("oui, je suis moi !")
        pass


if __name__ == '__main__':
    homme1 = Homme1()
    homme2 = Homme2()
    print(f"Mon nom est {homme1.nom}, j'ai {homme1.age} ans")
    print(homme2.__dict__.values(), end='')
    print(homme2.getNom(), homme2.getAge(), "\n\n--------------------------------------------")
    
    anim = Animal("Cliford1", "rouge", "chien domestique")
    anim.display()
    print(f"Je m'apelle {anim.nom}, je suis de couleur {anim.couleur} et je suis un {anim.genre}.\n{anim.manger()}")
    
    ca = Animal("Cliford2", "rouge", "chien sauvage")
    ca.display()
    print(f"\nJe m'apelle {ca.nom}, je suis de couleur {ca.couleur} et je suis un {ca.genre}.\n{ca.manger()}")
    
    carn = CarniSauvage("Cliford3", "rouge", "chien carnisauvage")
    carn.display() 
    print(f"\nJe m'apelle {carn.nom}, je suis de couleur {carn.couleur} et je suis un {carn.genre}.\n{carn.manger()}\ndoc = {carn.__doc__}")
    carn.parler()
    
    rep = Reptile()
    print("\n--------------------------------------------\n")
    rep.manger()
    rep.deplacer()
    rep.description()
    print("\n--------------------------------------------\n")
    