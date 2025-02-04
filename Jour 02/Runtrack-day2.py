# JOB 1
class Rectangle():
    def __init__(self,__longueur, __largeur):
        self.__longueur = __longueur
        self.__largeur = __largeur

    def set_dimensions(self, new_longueur, new_largeur):
        self.__longueur = new_longueur
        self.__largeur = new_largeur

    def get_dimensions(self):
        return (f" La longeur est {self.__longueur}, et la largeur {self.__largeur}")

instance_rect = Rectangle(10,5)
print(instance_rect.get_dimensions())
instance_rect.set_dimensions(20,10)
print(instance_rect.get_dimensions())

#JOB 2 & 3
class Livre():
    def __init__(self,__titre,__auteur,__pages,):
        self.__titre = __titre
        self.__auteur = __auteur
        self.__pages = __pages
        self.__disponible = True

    def set_livre(self, new_titre, new_auteur, new_pages):
        self.__titre = new_titre
        self.__auteur = new_auteur
        if new_pages != float(new_pages) or new_pages < 0 :
            return ("Le nombres de pages n'est pas valide")
            
        else :
            self.__pages = new_pages

    def get_livre(self):
        return (f"Le livre {self.__titre}, écrit par {self.__auteur} possède {self.__pages} pages.")

    def verification(self):
        if self.__disponible == True:
            print("Le livre est disponible")
            return True
        if self.__disponible == False:
            print("Le livre est indisponible")
            return False
        
    def emprunter(self):
        if self.__disponible == True:
            self.__disponible = False
            print("Vous emprunter le livre")
        if self.__disponible == False:
            print("Le livre n'est pas disponible")
        
    def rendre(self):
        if Livre.verification(self) == False:
            print("Vous rendez le livre")
            self.__disponible = True
        if Livre.verification(self) == True:
            print("Vous n'avez pas emprunté ce livre")

instance_livre = Livre("","","",)
print(instance_livre.set_livre("MessiGoat","C.Ronaldo","200.5"))
print(instance_livre.set_livre("MessiGoat","C.Ronaldo",350))
print(instance_livre.get_livre())
instance_livre.verification()
instance_livre.emprunter()
instance_livre.rendre()
instance_livre.verification()


#JOB 4
class Student():
    def __init__(self, __nom, __prenom, __numero, __credits):
        self.__nom = __nom
        self.__prenom = __prenom
        self.__numero = __numero
        self.__credits = __credits
        self.__level = ""
        self.__student_eval()

    def add_credit(self, add_cred):
        if add_cred > 0 :
            self.__credits += add_cred
            print(f"Vous ajoutez {add_cred} crédits a l'étudiant")
            self.__student_eval()
        else :
            print("Valeur des crédits insuffisant")

    def __student_eval(self):
        if self.__credits >= 90:
            self.__level = "Excellent"
        if 90 > self.__credits >= 80 :
            self.__level = "Très Bien"
        if 80 > self.__credits >= 70 :
            self.__level = "Bien"
        if 70 > self.__credits >= 60 :
            self.__level = "Passable"
        if self.__credits < 60:
            self.__level = "Insuffisant"

    def student_info(self):
        return (f"L'étudiant n°{self.__numero}, {self.__nom} {self.__prenom} possède un niveau {self.__level}.")

instance_student1 = Student("John","Doe","145", 0)
print(instance_student1.student_info())
instance_student1.add_credit(5)
instance_student1.add_credit(5)
instance_student1.add_credit(5)
print(instance_student1.student_info())
instance_student1.add_credit(70)
print(instance_student1.student_info())
instance_student1.add_credit(100)
print(instance_student1.student_info())


#JOB 5
class Voiture():
    def __init__(self, __marque, __modele, __annee, __kilometrage):
        self.__marque = __marque
        self.__modele = __modele
        self.__annee = __annee
        self.__kilometrage = __kilometrage
        self.en_marche = False
        self.__reservoir = 50

    def set_marque(self, __new_marque):
        self.__marque = __new_marque
    def set_modele(self, __new_modele):
        self.__modele = __new_modele
    def set_annee(self, __new_annee):
        self.__annee = __new_annee
    def set_kilometrage(self, __new_kilometrage):
        self.__kilometrage = __new_kilometrage
    
    def get_marque(self):
        return (f"La marque de la voiture est {self.__marque}")
    def get_modele(self):
        return (f"Le modele de la voiture est {self.__modele}")
    def get_annee(self):
        return (f"L'année de la voiture est {self.__annee}")
    def get_kilometrage(self):
        return (f"Le kilometrage de la voiture est {self.__kilometrage}km")

    def demarrer(self):
        Voiture.__verif_plein(self)
        if self.__reservoir >= 5 :
            if self.en_marche == False :
                print("Vous demarrez la voiture")
                self.en_marche = True
            if self.en_marche == True :
                print("La voiture est deja en marche")
        if self.__reservoir < 5 :
            print("Essence insuffisante pour démarrer la voiture")        

    def arreter(self):
        if self.en_marche == True :
            print("Vous arretez la voiture")
            self.en_marche == False
        if self.en_marche == False :
            return ("La voiture est deja arreté")

    def __verif_plein(self):
        print(f"Il y a {self.__reservoir}L dans le reservoir")
        return self.__reservoir

    def set_reservoir(self,new_reservoir):
        self.__reservoir = new_reservoir

instance_voiture = Voiture("FIAT","Panda","2006","150000")
print(instance_voiture.get_marque())
print(instance_voiture.get_modele())
print(instance_voiture.get_annee())
print(instance_voiture.get_kilometrage())
instance_voiture.set_marque("BMW")
instance_voiture.set_modele("M3")
instance_voiture.set_annee("2025")
instance_voiture.set_kilometrage("30000")
print(instance_voiture.get_marque())
print(instance_voiture.get_modele())
print(instance_voiture.get_annee())
print(instance_voiture.get_kilometrage())
instance_voiture.demarrer()
instance_voiture.arreter()
instance_voiture.set_reservoir(4)
instance_voiture.demarrer()


#JOB 6
class Commande():
    def __init__(self, __num_commande, __list_plat, __stat_commande):
        self.__num_commande = __num_commande
        self.__list_plat = __list_plat
        self.__stat_commande = __stat_commande
        self.__list_plat = []
        self.__list_prix = []
        self.__dict_commande = {
            "Plat" : f"{self.__list_plat}",
            "Prix" : f"{self.__list_prix}",
            "Statut" : f"{self.__stat_commande}",
            "Total" : 0
        }
        
    
    def add_plat(self, __new_plat, __add_prix, __stat_commande):
        self.__list_plat.append(__new_plat)
        self.__list_prix.append(__add_prix)
        

    def print_ticket(self):
        __final_price = sum(self.__list_prix)
        self.__dict_commande["Total"] = __final_price 
        print(self.__dict_commande)

        

instance_commande = Commande("","","")
instance_commande.add_plat ("Pizza", 12, "En cours")
instance_commande.print_ticket()
instance_commande.add_plat ("Pâte carbonara", 15, "Terminé")
instance_commande.print_ticket()

