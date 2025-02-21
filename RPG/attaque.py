import random

class attaque:
    def __init__(self, nom, degats, critiques, echecs, description, utilisations_max):
        self.nom = nom
        self.degats = degats
        self.critiques = critiques
        self.echecs = echecs 
        self.description = description
        self.utilisations_max = utilisations_max
        self.utilisations_restantes = utilisations_max

    def lancer(self):
        if self.utilisations_restantes > 0:
            self.utilisations_restantes -= 1
            print(f"{self.nom} est lancée.") # Vérifier si l'attaque peut être utilisée
            if random.random() < self.echecs:
                print(f"{self.nom} a échoué.")
                return 0
            if random.random() < self.critiques:
                print("Coup critique !")
                return self.degats * 2
            print(f"{self.degats} dégâts infligé.")
            return self.degats
        else:
            print(f"Plus d'utilisations pour l'attaque {self.nom}.")
            return 0

    def afficher_infos(self):
        print(f"Attaque : {self.nom}")
        print(f"Description : {self.description}")
        print(f"Dégâts : {self.degats}")
        print(f"Critiques : {self.critiques * 100}%")
        print(f"Échecs : {self.echecs * 100}%")
        print(f"Utilisations restantes : {self.utilisations_restantes}/{self.utilisations_max}")