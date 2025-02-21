class Place:
    def __init__(self, coordonnees, nom, description, chemins, objets, type_lieu, monstre):
        self.coordonnees = coordonnees
        self.nom = nom
        self.description = description
        self.chemins = chemins
        self.objets = objets
        self.type_lieu = type_lieu
        self.monstre = monstre #Informations données lors de la création d'un lieu enregistrées dans les propriétés de l'objet
    
    def afficher_infos(self):
        print(f"Nom du lieu : {self.nom}")
        print(f"Description : {self.description}")
        print(f"Coordonnées : {self.coordonnees}")
        print(f"Type de lieu : {self.type_lieu}")
        print(f"Objets disponibles : {', '.join(self.objets) if self.objets else 'Aucun'}")
        print(f"Chemins vers d'autres lieux : {', '.join(self.chemins) if self.chemins else 'Aucun'}")
        if self.monstre:
            print(f"Monstre présent : {self.monstre}")
        else:
            print("Aucun monstre présent dans ce lieu.")
    
    def ajouter_objet(self, objet):
        self.objets.append(objet)
        print(f"L'objet {objet} a été ajouté au lieu {self.nom}.")#Fonction pour ajouter un objet à la liste des objets présents dans ce lieu
    
    def retirer_objet(self, objet):
        if objet in self.objets:
            self.objets.remove(objet)
            print(f"L'objet {objet} a été retiré du lieu {self.nom}.")#Fonction pour retirer un objet à la liste des objets présents dans ce lieu
        else:
            print(f"L'objet {objet} n'est pas présent dans le lieu {self.nom}.")
    
    def ajouter_chemin(self, lieu):
        if lieu not in self.chemins:
            self.chemins.append(lieu)
            print(f"Le chemin vers {lieu} a été ajouté au lieu {self.nom}.")
        else:
            print(f"Le chemin vers {lieu} existe déjà.") #Fonction pour ajouter un chemin vers un autre lieu
    
    def retirer_chemin(self, lieu):
        if lieu in self.chemins:
            self.chemins.remove(lieu)
            print(f"Le chemin vers {lieu} a été retiré du lieu {self.nom}.")
        else:
            print(f"Le chemin vers {lieu} n'existe pas.")#Fonction pour retirer un chemin