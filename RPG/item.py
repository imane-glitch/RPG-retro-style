class Item:
    def __init__(self, nom, description, stats, utilisations_max, prix):
        self.nom = nom
        self.description = description
        self.stats = stats 
        self.utilisations_max = utilisations_max
        self.utilisations_restantes = utilisations_max
        self.prix = prix
    def utiliser(self):
        if self.utilisations_restantes > 0:
            self.utilisations_restantes -= 1
            print(f"{self.nom} choisi.")
            return self.stats
        else:
            print(f"L'objet {self.nom} ne peut plus être utilisé.")
            return None

    def afficher_infos(self):
        print(f"Objet : {self.nom}")
        print(f"Description : {self.description}")
        print(f"Effets : {self.stats}")
        print(f"Utilisations restantes : {self.utilisations_restantes}/{self.utilisations_max}")
        print(f"Prix : {self.prix} or")
