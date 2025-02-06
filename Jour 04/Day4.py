import random

#JOB 1
class Personne():
    def __init__(self, age):
        self.age = age

    def bonjour(self):
        print("Hello")

    def modif_age(self, new_age):
        self.age = new_age


class Eleve(Personne):
    def __init__(self, age):
        super().__init__(age)

    def go_to_school(self):
        print("Je vais en cours")

    def get_age(self):
        print(f"J'ai {self.age} ans")

class Professeur():
    def __init__(self,matiere):
        self.__matiere = matiere

    def enseigner(self):
        return (f"Le cours de {self.__matiere} va commencer")
    
eleve1 = Eleve(14)
print(eleve1.get_age()) 
prof1 = Professeur("Mathématique")
print(prof1.enseigner())


#JOB 2
eleve1.go_to_school()
eleve1.bonjour()
eleve1.modif_age(15)
eleve1.get_age()


#JOB3
class Rectangle():
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        perimetre = (self.__longueur + self.__largeur) * 2
        print(f"Le perimetree du rectangle est : {perimetre}")

    def surface(self):
        surface = self.__longueur * self.__largeur
        print(f"La surface du rectangle est : {surface}")

    def get_longueur(self):
        return (f"La longueur est :{self.__longueur}")
    def get_largeur(self):
        return (f"La longueur est :{self.__largeur}")
    def set_longueur(self, new_longueur):
        self.__longueur = new_longueur
    def set_largeur(self, new_largeur):
        self.__largeur = new_largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
        self.__longueur = longueur
        self.__largeur = largeur

    def volume(self):
        volume = self.__largeur * self.__longueur * self.__hauteur
        return (f"Le volume du parallelepipede est :{volume}")

rect1 = Rectangle(10,5)
print(rect1.get_longueur())
rect1.set_longueur(15)
print(rect1.get_longueur())
rect1.surface()
rect1.perimetre()

parallele1 = Parallelepipede(10,5,2)
print(parallele1.volume())


#JOB 4
class Forme():
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    def aire(self):
        return 0
    
class Rectangle2(Forme):
    def __init__(self, longueur, largeur):
        super().__init__(longueur, largeur)
        self.__longueur = longueur
        self.__largeur = largeur

    def aire(self):
        aire = self.__longueur * self.__largeur
        return (f"L'aire du rectangle est {aire}")
    

rect2 = Rectangle2(10,20)
print(rect2.aire())

#JOB 5
class Cercle(Forme):
    def __init__(self, longueur, largeur, radius):
        super().__init__(longueur, largeur)
        self.radius = radius

    def aire(self):
        aire = self.radius * self.radius * 3.14 
        return (f"L'aire du cercle est {aire}")

cercle = Cercle (10,20,5)
print(cercle.aire())
print(rect2.aire())


#JOB 6 
class Vehicule():
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele 
        self.annee = annee 
        self.prix = prix

    def demarrer(self):
        print("Attention de roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def info_vehicule(self):
        return (f"La voiture {self.marque} {self.modele} \n de {self.annee}\n au prix de {self.prix}€\n possède {self.portes} portes")
    def demarrer(self):
        print("Je demarre ma voiture")

voiture = Voiture("BMW" , "M3", "2019", 30000)
print(voiture.info_vehicule())

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roue = 2

    def info_vehicule(self):
        return (f"La moto {self.roue}\n{self.marque} {self.modele} \n de {self.annee}\n au prix de {self.prix}€")
    def demarrer(self):
        print("Je demarre ma moto")

moto = Moto("Husqvarna","Svartpilen","2023",3000)
print(moto.info_vehicule())

voiture.demarrer()
moto.demarrer()



#JOB 7
class Jeu():
    def __init__(self,nom):
        self.nom = nom

    def win(self):
        return ("Congrat, you win")
    def loose(self):
        return ("Sorry you loose")
    
    def continuer(self):
        print("Do you want continue?(YES/NO)")
        self.choose = input(":")
        if self.choose == "YES" :
            return True
        if self.choose == "NO" :
            return False

class Jeu():
    def __init__(self, nom):
        self.nom = nom

    def win(self):
        return "Congrat, you win"

    def loose(self):
        return "Sorry you loose"

    def continuer(self):
        print("Do you want to continue? (YES/NO)")
        self.choose = input(":")
        return self.choose == "YES"


class Carte(Jeu):
    def __init__(self, nom):
        super().__init__(nom)
        self.joker ="un as de"
        self.valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, self.joker]
        self.couleurs = ["Coeur", "Carreau", "Pique", "Trefle"]
        self.carte_tiré = []

    def draw_card(self):
        self.valeur = random.choice(self.valeurs)
        self.couleur = random.choice(self.couleurs)
        print(f"Vous piochez {self.valeur} {self.couleur}")
        if self.valeur == self.joker:
            self.joker_choice()
        self.carte_tiré.append(self.valeur)
        self.total()

    def total(self):
        total = sum(self.carte_tiré)
        print(f"Votre total est {total}")
        return total

    def joker_choice(self):
        self.joker = int(input("You draw an as, choose between 1 or 11: "))
        if self.joker == 1: 
            print("You choose 1")
            return 1
        elif self.joker == 11:
            print("You choose 11")
            return 11
        else:
            print("Please enter a correct value (1 or 11)")
            self.joker_choice()
            


class Croupier(Carte):
    def __init__(self, nom):
        super().__init__(nom)

    def draw_card(self):
        self.valeur = random.choice(self.valeurs)
        self.couleur = random.choice(self.couleurs)
        print(f"Le croupier pioche {self.valeur} {self.couleur}")
        if self.valeur == self.joker:
            self.joker_choice()
        self.carte_tiré.append(self.valeur)
        self.total()

    def joker_choice(self):
        return 1
    
    def total(self):
        total = sum(self.carte_tiré)
        print(f"Le total du croupier est {total}")
        return total


def play():
    jeu = Jeu("Game")
    player = Carte("Arnaud")
    croupier = Croupier("Croupier")

    while True:
        player.draw_card()
        croupier.draw_card()
        if 17 < croupier.total() <= 21:
            pass
        if player.total() > 21:
            print(jeu.loose())
            break
        if croupier.total() > 21:
            print(jeu.win())
            break

        if not jeu.continuer():
            if croupier.total()<player.total():
                croupier.draw_card()
            if croupier.total() > 21:
                print(jeu.win())
                break
            if player.total() > croupier.total():
                print(jeu.win())
                break
            if  21 > croupier.total() > player.total() :
                print(jeu.loose())
            break


play()
