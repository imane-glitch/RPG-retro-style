import random

class Game:
    def __init__(self):
        # Initialisation du joueur
        self.player = {
            "name": "Klaus Noir",
            "age": 36,
            "level": 1,
            "xp": 0,
            "hp":100 ,
            "max_hp": 100,
            "attack": 10,
            "defense": 5,
            "inventory": ["Knife"],
        }
        
        self.current_location = "Starting Point"
        self.game_map = {
            "Starting Point": {
                "description": "You are in a forest surrounded by trees.",
                "items": [],
                "monsters": [],
                "next_locations": ["North Forest", "East Forest"]
            },
            "North Forest": {
                "description": "You see snowy trees all around.",
                "items": ["Potion"],
                "monsters": ["Grinch"],
                "next_locations": ["Summit"]
            },
            "East Forest": {
                "description": "The forest becomes darker and more mysterious.",
                "items": ["Shield"],
                "monsters": ["Elf Assassin"],
                "next_locations": []
            },
            "Summit": {
                "description": "You reach the icy summit where the boss awaits.",
                "items": [],
                "monsters": ["Frosty the Hitman"],
                "next_locations": []
            }
        }
        self.is_game_over = False

    def move(self, direction):
        # Déplacement entre les lieux
        if self.current_location in self.game_map:
            next_locations = self.game_map[self.current_location]["next_locations"]
            if direction in next_locations:
                self.current_location = direction
                print(f"You move to {direction}.")
                self.describe_location()
                self.check_for_events()
            else:
                print("You cannot go that way.")
        else:
            print("Invalid location.")

    def describe_location(self):
        # Description du lieu actuel
        if self.current_location in self.game_map:
            print(self.game_map[self.current_location]["description"])
        else:
            print("This place does not exist.")

    def check_for_events(self):
        # Vérifie s'il y a un monstre ou un objet
        location = self.game_map[self.current_location]
        if location["monsters"]:
            monster = random.choice(location["monsters"])
            print(f"You are attacked by {monster}!")
            self.start_combat(monster)
        elif location["items"]:
            item = random.choice(location["items"])
            print(f"You found a {item}!")
            self.player["inventory"].append(item)
            location["items"].remove(item)

    def start_combat(self, monster):
        # Démarrage d'un combat
        print(f"A wild {monster} appears!")
        monster_hp = 50
        while monster_hp > 0 and self.player["hp"] > 0:
            print(f"{monster}'s HP: {monster_hp}, Your HP: {self.player['hp']}")
            action = input("Choose an action: [Attack, Use Item, Run]: ").lower()
            if action == "attack":
                damage = self.player["attack"]
                monster_hp -= damage
                print(f"You deal {damage} damage to {monster}.")
                if monster_hp > 0:
                    self.monster_attack(monster)
            elif action == "use item":
                self.use_item()
            elif action == "run":
                print("You flee the battle.")
                return
            else:
                print("Invalid action.")
        if monster_hp <= 0:
            print(f"You defeated {monster}!")
            self.player["xp"] += 100
            self.level_up()
        elif self.player["hp"] <= 0:
            print("You have been defeated...")
            self.game_over()

    def monster_attack(self, monster):
        # L'attaque du monstre
        damage = random.randint(5, 15)
        self.player["hp"] -= damage
        print(f"{monster} attacks and deals {damage} damage.")

    def use_item(self):
        # Utilisation d'un objet de l'inventaire
        print(f"Inventory: {self.player['inventory']}")
        item = input("Choose an item to use: ")
        if item in self.player["inventory"]:
            if item == "Potion":
                self.player["hp"] = min(self.player["max_hp"], self.player["hp"] + 50)
                print(f"You used a Potion. HP restored to {self.player['hp']}.")
                self.player["inventory"].remove(item)
            else:
                print("You cannot use this item.")
        else:
            print("Item not found in inventory.")

    def level_up(self):
        # Gestion du passage au niveau supérieur
        required_xp = self.player["level"] * 500
        if self.player["xp"] >= required_xp:
            self.player["level"] += 1
            self.player["max_hp"] += 20
            self.player["attack"] += 5
            self.player["defense"] += 5
            self.player["xp"] -= required_xp
            print(f"You leveled up! You are now level {self.player['level']}.")

    def game_over(self):
        # Fin du jeu
        self.is_game_over = True
        print("Game Over. Returning to the main menu.")

    def launch_game(self):
        # Menu principal
        while not self.is_game_over:
            print("\nMain menu:")
            print("1- Create New Game")
            print("2- Load Saved Game")
            print("3- About")
            print("4- Exit")
            choice = input("> ")
            if choice == "1":
                name = input("Please enter your name: ")
                self.player["name"] = name
                print(f"Welcome, {self.player['name']}!")
                self.describe_location()
            elif choice == "2":
                print("Load game feature is not implemented yet.")
            elif choice == "3":
                print("RPG Game by Klaus Noir Productions.")
            elif choice == "4":
                print("Exiting the game.")
                self.is_game_over = True
            else:
                print("Invalid option.")


if __name__ == "__main__":
    game = Game()
    game.launch_game()