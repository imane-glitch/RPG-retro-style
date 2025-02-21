import random

class Monstre:
    def __init__(self, nom, vie, force, defense, inventaire=None):
        self.nom, self.vie, self.force, self.defense = nom, vie, force, defense
        self.niveau, self.experience = 1, 0
        self.inventaire = inventaire or []

    def attaquer(self, cible):
        degats = max(self.force - cible.defense, 0)
        print(f"{self.nom} attaque {cible.nom} et inflige {degats} dégâts!")
        cible.recevoir_degats(degats)
        self.gagner_experience(degats)

    def recevoir_degats(self, degats):
        self.vie = max(self.vie - degats, 0)
        print(f"{self.nom} a {self.vie} points de vie restants.")
    
    def gagner_experience(self, degats):
        if self.niveau < 3:  # Le monstre ne peut pas dépasser le niveau 3
            self.experience += degats
            if self.experience >= self.niveau * 10:
                self.niveau += 1
                if self.niveau > 3:
                    self.niveau = 3
                print(f"{self.nom} passe au niveau {self.niveau}!")

    def est_vivant(self):
        return self.vie > 0

class Lutin(Monstre):
    def lancer_cadeau_explosif(self, cible):
        degats = self.force * 2
        print(f"{self.nom} lance un cadeau explosif et inflige {degats} dégâts!")
        cible.recevoir_degats(degats)

    def cerf_empoisonne(self, cible):
        print(f"{self.nom} empoisonne {cible.nom} avec son cerf.")
        cible.vie -= 5

class Grinch(Monstre):
    def coup_critique(self, cible):
        degats = self.force * 3
        print(f"{self.nom} fait un coup critique et inflige {degats} dégâts!")
        cible.recevoir_degats(degats)

    def couteau_empoisonne(self, cible):
        print(f"{self.nom} attaque {cible.nom} avec un couteau empoisonné.")
        cible.vie -= 10

class Frosty(Monstre):
    def pluie_balles_enneigees(self, cible):
        degats = 15
        print(f"{self.nom} lance une pluie de balles et inflige {degats} dégâts!")
        cible.recevoir_degats(degats)

    def cadeau_piege(self, cible):
        degats = 25
        print(f"{self.nom} lance un cadeau piégé et inflige {degats} dégâts!")
        cible.recevoir_degats(degats)

if __name__ == "__main__":
    lutin = Lutin("Lutin", 100, 30, 10)
    grinch = Grinch("Grinch", 120, 40, 20)
    frosty = Frosty("Frosty", 150, 35, 25)

    print(f"Vous affrontez un {lutin.nom} (Niveau {lutin.niveau})")
    print(f"Vous affrontez aussi un {grinch.nom} (Niveau {grinch.niveau})")
    print(f"Un autre monstre dans les parages : {frosty.nom} (Niveau {frosty.niveau})")
    print("\nLe combat commence...\n")

    while lutin.est_vivant() and grinch.est_vivant():
        lutin.lancer_cadeau_explosif(grinch)  # Attaque spéciale
        if grinch.est_vivant():
            grinch.attaquer(lutin)
        if lutin.est_vivant():
            lutin.cerf_empoisonne(grinch)  # Attaque spéciale empoisonnée

    if lutin.est_vivant():
        print(f"{lutin.nom} a gagné!")
    else:
        print(f"{grinch.nom} a gagné!")

    # Combat entre le Grinch et Frosty
    print("\nCombat entre Grinch et Frosty\n")

    while grinch.est_vivant() and frosty.est_vivant():
        grinch.coup_critique(frosty)  # Attaque spéciale
        if frosty.est_vivant():
            frosty.pluie_balles_enneigees(grinch)

    if grinch.est_vivant():
        print(f"{grinch.nom} a gagné!")
    else:
        print(f"{frosty.nom} a gagné!")