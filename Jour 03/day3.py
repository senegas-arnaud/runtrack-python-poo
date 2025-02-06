#JOB 1

class Ville():
    villes = []
    def __init__(self, nom, nombre):
        self.__nom = nom
        self.__nombre = nombre
        Ville.villes.append(self)

    def get_nom(self):
        return self.__nom
    
    def get_nombre(self):
        return self.__nombre
    
    def one_more_pop(self):
        self.__nombre +=1

    def display_pop(self):
        print(f"La ville de {self.__nom} possède {self.__nombre} habitants")

        

class Personne():
    def __init__(self, __prenom, __age):
        self.__prenom = __prenom 
        self.__age = __age 

    def add_pop(self, nom_ville):
        for ville in Ville.villes:
            if ville.get_nom() == nom_ville:
                ville.one_more_pop()
                break

    def pop_info(self, nom_ville):
        for ville in Ville.villes:
            if ville.get_nom() == nom_ville:
                print(f"{self.__prenom}, âgé de {self.__age} ans, habite à {ville.get_nom()}")
                break

paris = Ville("Paris",1000000)
marseille = Ville("Marseille",861635)
paris.display_pop()
marseille.display_pop()

john = Personne("John", 45)
john.add_pop("Paris")
myrtille = Personne("Myrtille", 4)
myrtille.add_pop("Paris")
chloe = Personne ("Chloé", 18)
chloe.add_pop("Marseille")

john.pop_info("Paris")
myrtille.pop_info("Paris")
chloe.pop_info("Marseille")

paris.display_pop()
marseille.display_pop()


#JOB 2
class CompteBancaire():
    def __init__(self, __num_compte, __nom, __prenom, __solde, __decouvert):
        self.__num_compte = __num_compte
        self.__nom = __nom
        self.__prenom = __prenom
        self.__solde = __solde
        self.__decouvert = __decouvert
        self.agios(50)

    def get_num_compte(self):
        return self.__num_compte
    def get_nom(self):
        return self.__nom
    def get_prenom(self):
        return self.__prenom
    def get_solde(self):
        return self.__solde
    
    def display_info(self):
        return (f"{self.__nom} {self.__prenom}, n°{self.__num_compte}, possède un solde de {self.__solde}€")

    def versement(self,montant):
        self.__solde += montant

    def retrait(self,m):
        if self.__decouvert == True :    
            if m == int(m) and m > 0:
                self.__solde -= m
            else :
                return ("Montant incorrect")
        if self.__decouvert == False : 
            if m < self.__solde :    
                if m == int(m) and m > 0:
                    self.__solde -= m
                else :
                    return ("Montant incorrect")
            else:
                return ("Solde du compte insuffisant")
            
    def agios(self,montant_agios):
        if self.__solde < 0 :
            self.__solde -= montant_agios
            return self.__solde

    def virement(self, __destinataire, somme):
        if self.__decouvert == True:
            self.__solde -= somme
            __destinataire.__solde += somme
            print(f"Vous avez fait un virement de {somme}€ à {compte1.__nom} {compte1.__prenom} ")
        if self.__decouvert == False :
            if self.__solde >= somme :
                self.__solde -= somme
                __destinataire.__solde += somme
                print(f"Vous avez fait un virement de {somme}€ à {compte1.__nom} {compte1.__prenom} ")
            if self.__solde < somme :
                return ("Montant indisponible sur votre compte")


compte1 = CompteBancaire(1,"Senegas","Arnaud",10000, True)
print(compte1.display_info())
compte1.versement(5000)
print(compte1.display_info())
print(compte1.retrait(16000))
print(compte1.display_info())
print(compte1.retrait(5.5))
compte1.retrait(12000)
print(compte1.display_info())

compte2 = CompteBancaire(2,"Senegas","Thomas",10000, False)
print(compte2.display_info())
compte2.versement(5000)
print(compte2.display_info())
print(compte2.retrait(16000))
print(compte2.display_info())

compte2.virement(compte1, 13000)
print(compte2.display_info())
print(compte1.display_info())


#JOB 3
#class Tache():
    #def __init__(self, titre, description, statut):
        #self.titre = titre
        #self.description = description
        #self.statut = statut

#class List_taches():
    #def __init__(self):
        #self.taches = []

    #def add_task(self,new_task):
        #self.taches.append(new_task)

    #def supr_task(self,task):
        #for element in self.taches:
            #if task == self.taches:
                #self.taches.remove(task)


#JOB 5
class Jeu():
    def __init__(self):
        self.niveau = ""

    def choisirniv(self):
        self.niveau = (input("Choisissez un niveau : Easy, Medium ou Hard : "))

    def game_over(self):
        print("Vous n'avez plus de vie, vous avez perdu")
    
    def win(self):
        print("Félicitation, vous avez gagné")


class Personnage():
    def __init__(self, nom, vie):
        self.nom = nom 
        self.vie = int(vie)

    def attaquer(self, adversaire):
        adversaire.vie -= 1
        print(f"{self.nom} attaque, {adversaire.nom} perd une vie")
         
    def set_hp(self,jeu, adversaire):
        if jeu.niveau == "Easy":
            self.vie = 7
            adversaire.vie = 3
        if jeu.niveau == "Medium":
            self.vie = 5
            adversaire.vie = 5
        if jeu.niveau == "Hard":
            self.vie = 3
            adversaire.vie = 7

def lancerJeu():  
    jeu = Jeu() 
    player = Personnage("Player", 0)
    ennemi = Personnage("Ennemi", 0)
    jeu.choisirniv()
    player.set_hp(jeu,ennemi)
    while player.vie >= 0 and ennemi.vie >= 0:
        player.attaquer(ennemi)
        ennemi.attaquer(player)
        if player.vie == 0 :
            jeu.game_over()
            break
        if ennemi.vie == 0 :
            jeu.win()
            break  
    
lancerJeu()

