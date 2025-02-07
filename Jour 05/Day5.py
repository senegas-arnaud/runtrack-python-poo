class Part():
    def __init__(self, name, material):
        self.name = name
        self.material = material 

    def change_material(self, new_material):
        self.material = new_material

    def change_name(self, new_name):
        self.name = new_name

    def __str__(self):
        return (f"La pièce:{self.name}, construit en {self.material}")
    def get_name(self):
        return self.name
    def get_material(self):
        return self.material
    
part1 = Part("Mat","Bois")
part2 = Part ("Coque","Bois")

class Ship():
    def __init__(self, nom):
        self.nom = nom
        self.__part = {
            f"{part1.name}":f"{part1.material}",
            f"{part2.name}":f"{part2.material}",
        }
        self.history = []

    def display_state(self):
        return self.__part

    def replace_part(self, part_name, new_part):
        if part1.name == part_name:
            del self.__part[part1.name]
            part1.change_name(new_part)
            self.__part[part1.name] = part1.material
            self.history.append(f"Remplacement de {part_name} par {new_part}")
        if part2.name == part_name:
            del self.__part[part2.name]
            part2.change_name(new_part)
            self.__part[part2.name] = part2.material
            self.history.append(f"Remplacement de {part_name} par {new_part}")
                                                     

    def change_part(self,part_name, new_material):
        if part1.name == part_name:
            self.__part[f"{part1.name}"] = new_material
            self.history.append(f"Remplacement de {part1.name} en {new_material}")
        if part2.name == part_name:
            self.__part[f"{part2.name}"] = new_material  
            self.history.append(f"Remplacement de {part2.name} en {new_material}")

    def display_history(self):
        for modif in self.history:
            print(modif)


ship1 = Ship("Bateau")

class RacingShip(Ship):
    def __init__(self, nom, max_speed):
        super().__init__(nom)
        self.max_speed = max_speed
        self.nom = nom

    def display_speed(self):
        return self.max_speed
    def get_name(self):
        return self.nom

speed_boat = RacingShip("Fast Boat", 150)
print(f"La vitesse max de {speed_boat.get_name()} est : {speed_boat.display_speed()} km/h")


def display_menu():
    print("Menu:")
    print("1. Remplacer une pièce")
    print("2. Modifier le matériau d'une pièce")
    print("3. Afficher l'état du bateau")
    print("4. Afficher l'historique des modifications")
    print("5. Quitter")


def manage_ship():
    while True:
        display_menu()
        choice = input("Choisissez une option (1-5): ")

        if choice == "1":
            part_name = input("Entrez le nom de la pièce à remplacer: ")
            new_part = input("Entrez le nouveau nom de la pièce: ")
            ship1.replace_part(part_name, new_part)
            print(f"La pièce {part_name} a été remplacée par {new_part}.")

        if choice == "2":
            part_name = input("Entrez le nom de la pièce à modifier: ")
            new_material = input("Entrez le nouveau matériau: ")
            ship1.change_part(part_name, new_material)
            print(f"Le matériau de {part_name} a été changé en {new_material}.")

        if choice == "3":
            print("État actuel du bateau:")
            print(ship1.display_state())

        if choice == "4":
            print("Historique des modifications:")
            ship1.display_history()

        if choice == "5":
            print("Bye bye")
            break

        else:
            print("choisissez une option entre 1 et 5.")


manage_ship()