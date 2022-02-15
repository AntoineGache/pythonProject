

class ListeChainee:
    def __init__(self, prem):
        self.premier = prem
        self.dernier = None

    def longueur(self):
        longueur = 0
        if self.premier is not None:
            next = self.premier
            while next is not None:
                longueur += 1
                next = next.suivant
        return longueur

    def convert_tab_liste_chainee(self, tab):
        liste = ListeChainee(None)
        for i in range(len(tab)):
            maillon = Maillon(tab[i], None)
            if i == 0:
                liste.premier = maillon
            else:
                next.suivant = maillon
            next = maillon
        self.premier = liste.premier

    def affichage_liste(self):
        compteur = 0
        print("[", end="")
        if self.premier is not None:
            next = self.premier
            while next is not None:
                print(next.valeur, " " ,end="")
                next = next.suivant
                compteur += 1
        else:
            print(None)
        print("]")

    def inverse(self):
        """Permet d'inverser la liste chaînée."""

        if self.premier is None:
            raise ValueError("Liste chainée vide")

        if self.premier != self.dernier:
            maillon = self.premier
            maillon_suivant = self.premier.suivant
            temp = maillon_suivant.suivant
            maillon_suivant.suivant = maillon
            maillon.suivant = None
            self.dernier = maillon

            while temp is not None:
                maillon = maillon_suivant
                maillon_suivant = temp
                temp = maillon_suivant.suivant
                maillon_suivant.suivant = maillon

            self.premier = maillon_suivant

            return self

class Maillon:
    def __init__(self, val, suiv):
        self.valeur = val
        self.suivant = suiv

