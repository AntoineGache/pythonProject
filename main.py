from Liste_chainee import *

if __name__ == '__main__':
    print("Début du programme")

    tab = [1,2,3,4,5,9,14,15,24,28,36,59,78]

    liste = ListeChainee(None)
    print("Taille de la liste chainée avant ajout :", liste.longueur())
    liste.convert_tab_liste_chainee(tab)
    print("Taille de la liste chainée après ajout:", liste.longueur())
    liste.affichage_liste()
    liste.inverse()
    print(liste.affichage_liste())

    print(liste.k_ieme_element(3))
