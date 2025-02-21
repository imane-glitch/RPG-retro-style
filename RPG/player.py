class Player:
    def __init__(self, name, age, player_type):
        self.name = name
        self.age = age
        self.type = player_type
        self.level = 1
        self.stats = {
            "HP": 100,
            "Attack": 10,
            "Defense": 5,
            "Speed": 5
        }
        self.attacks = []
        self.inventory = []
        self.experience = 0

    def open_inventory(self):
        if not self.inventory:
            print("Votre inventaire est vide.")
        else:
            print("Contenu de l'inventaire 😊")
            for i, item in enumerate(self.inventory):
                print(f"{i + 1}. {item.name} - {item.description}")

    def death(self):
        if self.stats["HP"] <= 0:
            print(f"{self.name} est mort. Game Over.")
            return True
        return False

    def attack(self, target):
        if not self.attacks:
            print(f"{self.name} n'a pas d'attaque disponible.")
            return

        print(f"{self.name} attaque {target.name} !")
        # Choisir une attaque (par défaut la première)
        attack = self.attacks[0]
        damage = attack.damage()  # Calcul des dégâts
        print(f"L'attaque inflige {damage} dégâts.")
        target.stats["HP"] -= damage

        if target.stats["HP"] <= 0:
            print(f"{target.name} a été vaincu !")
        else:
            print(f"{target.name} a encore {target.stats['HP']} HP.")
    
    def level_up(self):
        self.level += 1
        self.stats["HP"] += 10
        self.stats["Attack"] += 5
        self.stats["Defense"] += 3
        self.stats["Speed"] += 2
        print(f"{self.name} monte au niveau {self.level} !")
        print(f"Statistiques améliorées : {self.stats}")

    def learn_attack(self, new_attack):
        """
        Ajoute une nouvelle attaque à la liste des attaques du joueur.
        """
        self.attacks.append(new_attack)
        print(f"{self.name} apprend une nouvelle attaque : {new_attack.name} !")

    def use_item(self, item_name):
        """
        Utilise un objet spécifique de l'inventaire.
        """
        for item in self.inventory:
            if item.name == item_name:
                print(f"{self.name} utilise {item.name}.")
                item.use()
                if item.stats.get("HP"):
                    self.stats["HP"] += item.stats["HP"]
                self.inventory.remove(item)
                return
        print(f"{item_name} n'est pas dans l'inventaire.")
