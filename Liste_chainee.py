

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

    def k_ieme_element(self,k):
        compteur = 1
        maillon = self.premier
        while compteur < k and maillon:
            compteur += 1
            maillon = maillon.suivant
        if maillon:
            return maillon.valeur
        else:
            raise Exception("pas assez de maillons !")

    def k_ieme_element_distint(self,k):
        compteur = 0
        precedent = None
        maillon = self.premier

        while maillon is not None and compteur < k:
            if maillon.valeur != precedent:
                compteur += 1

            precedent = maillon.valeur
            maillon = maillon.suivant

        return precedent

    def comparaison(self,x):
        maillon = self.premier
        while maillon is not None:
            if maillon.valeur == x:
                return True
            maillon = maillon.suivant

        return False

    def comparaison_croissante(self,x):
        maillon = self.premier
        while maillon is not None:
            if maillon.valeur == x:
                return True
            if x < maillon.valeur:
                print("Valeur dépassé, ", end="")
                return False
            maillon = maillon.suivant

        return False

    def nb_element_distint(self):

        compteur = 0
        maillon = self.premier
        precedent = None

        while maillon is not None:
            if maillon.valeur != precedent:
                compteur += 1
            precedent = maillon.valeur
            maillon = maillon.suivant

        return compteur

    def liste_element_distint(self):
        listeDistint = ListeChainee(None)

        if self.premier is None:
            return listeDistint

        listeDistint.premier = Maillon(self.premier.valeur, None)
        precedent = self.premier.valeur

        maillon = self.premier.suivant
        dernier_cree = listeDistint.premier

        while maillon is not None:
            if maillon.valeur != precedent:
                copie = Maillon(maillon.valeur,None)
                dernier_cree.suivant = copie
                dernier_cree = dernier_cree.suivant
                precedent = maillon.valeur

            maillon = maillon.suivant

        return listeDistint

    def liste_element_distint_remplacement(self):


class Maillon:
    def __init__(self, val, suiv):
        self.valeur = val
        self.suivant = suiv

