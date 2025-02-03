# JOB 1 , 2 , 3
class Operation:
    def __init__(self):
        self.nombre1 = 10
        self.nombre2 = 5

    def display_nombre(self):
        return (f"le nombre 1 est {self.nombre1} ""/n"f"Le nombre 2 est {self.nombre2}")

    def addition(self):
        return (self.nombre1 + self.nombre2)


operation_instance = Operation()

print(operation_instance.display_nombre())
print(operation_instance.addition())



#JOB 4 
nom = "Senegas"
prenom = "Arnaud"

class Personne():
    def __init__(self):
        self.nom = nom
        self.prenom = prenom

    def Sepresenter (self, nom, prenom):
        return (f"Je suis {nom} {prenom} ")


personne_instance = Personne()
print(personne_instance.Sepresenter("Guy","Jean"))
print(personne_instance.Sepresenter("Senegas","Arnaud"))

#JOB  5
class Point():
    def __init__(self):
        self.x = 10
        self.y = 20

    def afficherLesPoints(self):
        return (f"Les coordonnées du point sont ({self.x};{self.y})")

    def afficherX(self):
        return (f"La coordonée X est {self.x}")

    def afficherY(self):
        return (f"La coordonée X est {self.y}")

    def changerX(self, new_x):
        self.x = new_x
        return (f"La coordonée X est maintenant : {self.x}")

    def changerY(self, new_y ):
        self.y = new_y
        return (f"La coordonée X est maintenant : {self.y}")


point_instance = Point()

print(point_instance.afficherLesPoints())
print(point_instance.changerX(50))
print(point_instance.changerY(100))
print(point_instance.afficherLesPoints())


#JOB 6
class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def display_age(self):
        return (f"L'animal est âgé de {self.age} ans")

    def veillir(self):
        self.age += 1
        return (f"L'animal gagne 1 ans")

    def nommer(self, new_prenom):
        self.prenom = new_prenom
        return (f"L'animal se nomme {self.prenom}")

animal_instance = Animal()
print(animal_instance.display_age())
print(animal_instance.veillir())
print(animal_instance.display_age())
print(animal_instance.nommer("Luna"))


#JOB 7
class Personnage():
    def __init__(self):
        self.x = 0
        self.y = 0

    def gauche(self):
        self.x -=1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y += 1

    def bas(self):
        self.y -= 1
    
    def position(self):
        pos = (self.x , self.y)
        return (f"Le joueur se trouve a la position {pos}")
        

personnage_instance = Personnage()

print(personnage_instance.position())
personnage_instance.haut()
personnage_instance.gauche()
personnage_instance.gauche()
print(personnage_instance.position())

#JOB 8
class Cercle():
    def __init__(self):
        self.rayon = ""
        self.d = ""
        self.a = ""
        
    def changerRayon(self, new_rayon):
        self.rayon = new_rayon
        return (f"Le rayon est maintenant de {self.rayon}")

    def afficherInfos(self):
        return (f"Le cercle possède un diametre de {self.d} et une aire de {self.a}")


    def aire(self):
        a = ((self.rayon)*(self.rayon))*3
        self.a = a 
        return(f"L'aire du cercle est {self.a}")

    def diametre(self):
        d = (self.rayon)*2
        self.d = d 
        return (f"Le diametre du cercle est {self.d}")

instance_cercle = Cercle()
print(instance_cercle.changerRayon(4))
print(instance_cercle.aire())
print(instance_cercle.diametre())
print(instance_cercle.afficherInfos())

print(instance_cercle.changerRayon(7))
print(instance_cercle.aire())
print(instance_cercle.diametre())
print(instance_cercle.afficherInfos())


#JOB 9      
class Produit():
    def __init__(self):
        self.nom = ""
        self.prixHT = ""
        self.TVA = 1.2
        self.prixTTC = ""

    def Nom(self, new_nom):
        self.nom = new_nom
    
    def Prix(self, new_prixHT):
        self.prixHT = new_prixHT

    def calculerPrixTTC(self):
        self.prixTTC = self.prixHT * self.TVA
    
    def afficher(self):
        return (f"Le produit : {self.nom}, coute {self.prixHT}€ hors taxes et {self.prixTTC}€ TTC")
    

instance_produit = Produit()
instance_produit.Nom("Ordinateur")
instance_produit.Prix(1000)
instance_produit.calculerPrixTTC()
print(instance_produit.afficher())

instance_produit.Nom("Voiture")
instance_produit.Prix(5000)
instance_produit.calculerPrixTTC()
print(instance_produit.afficher())

instance_produit.Nom("CocaCola")
instance_produit.Prix(1.5)
instance_produit.calculerPrixTTC()
print(instance_produit.afficher())



    