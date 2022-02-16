from Liste_chainee import *

if __name__ == '__main__':
    print("Début du programme")

    tab = [1,2,3,4,5,9,14,15,24,28,36,59,78]
    tab2 = [1,2,3,3,3,5,6,6,9]
    tab3 = [11, 2, 38, 3, 3, 5, 6, 6, 9]

    print("------------ Exo.0 ------------")
    liste = ListeChainee(None)
    print("Taille de la liste chainée avant ajout :", liste.longueur())
    liste.convert_tab_liste_chainee(tab)
    print("Taille de la liste chainée après ajout:", liste.longueur())
    print("------------ Exo.1 ------------")
    liste.affichage_liste()
    liste.inverse()
    print(liste.affichage_liste())
    print("------------ Exo.2 ------------")
    print(liste.k_ieme_element(3))

    print("------------ Exo.3 ------------")
    liste2 = ListeChainee(None)
    liste2.convert_tab_liste_chainee(tab2)
    liste2.affichage_liste()
    k = 4
    print("Valeur du ", k ,"ème éléments :",liste2.k_ieme_element_distint(k))

    print("------------ Exo.4 ------------")
    liste3 = ListeChainee(None)
    liste3.convert_tab_liste_chainee(tab3)
    liste3.affichage_liste()
    print("Comparaison liste non croissante :", liste2.comparaison(3))

    print("------------ Exo.5 ------------")
    print("Comparaison croissante :", liste2.comparaison_croissante(3))

    print("------------ Exo.6 ------------")
    print("Nombre d'éléments distints :", liste2.nb_element_distint())

    print("------------ Exo.7 ------------")
    listeDistint = liste2
    listeDistint.liste_element_distint().affichage_liste()

