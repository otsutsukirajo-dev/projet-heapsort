"""
heap.py
Tâche T1 (P1) — Structure de tas & entassement

Contient les fonctions de base manipulant un tas binaire (max-tas par défaut)
représenté sous forme de tableau (liste Python), sans utiliser de structure
de données de bibliothèque (pas de heap etc.).

Convention d'indexation (indices à partir de 0) :
    - parent(i)       = (i - 1) // 2
    - enfant_gauche(i) = 2 * i + 1
    - enfant_droit(i)  = 2 * i + 2
"""


def parent(i):
    """Retourne l'indice du parent du nœud i."""
    return (i - 1) // 2


def enfant_gauche(i):
    """Retourne l'indice de l'enfant gauche du nœud i."""
    return 2 * i + 1


def enfant_droit(i):
    """Retourne l'indice de l'enfant droit du nœud i."""
    return 2 * i + 2


def entasser(tableau, i, taille):
    """
    Restaure la propriété de max-tas à partir de l'indice i (sift-down / percolate-down).

    On suppose que les sous-arbres enracinés en enfant_gauche(i) et enfant_droit(i)
    respectent déjà la propriété de tas, mais que tableau[i] peut être plus petit
    que ses enfants.

    Paramètres :
        tableau (list) : le tableau représentant le tas
        i (int)         : indice du nœud à partir duquel on entasse
        taille (int)    : taille effective du tas (peut être < len(tableau)
                           si on trie en place, cf. heapsort)

    Complexité : O(log n)
    """
    plus_grand = i
    gauche = enfant_gauche(i)
    droite = enfant_droit(i)

    if gauche < taille and tableau[gauche] > tableau[plus_grand]:
        plus_grand = gauche

    if droite < taille and tableau[droite] > tableau[plus_grand]:
        plus_grand = droite

    if plus_grand != i:
        tableau[i], tableau[plus_grand] = tableau[plus_grand], tableau[i]
        entasser(tableau, plus_grand, taille)


def entasser_iteratif(tableau, i, taille):
    """
    Version itérative de entasser() (sift-down), utile pour éviter
    la récursion sur de très grands tableaux.

    Même contrat que entasser().
    """
    while True:
        plus_grand = i
        gauche = enfant_gauche(i)
        droite = enfant_droit(i)

        if gauche < taille and tableau[gauche] > tableau[plus_grand]:
            plus_grand = gauche

        if droite < taille and tableau[droite] > tableau[plus_grand]:
            plus_grand = droite

        if plus_grand == i:
            break

        tableau[i], tableau[plus_grand] = tableau[plus_grand], tableau[i]
        i = plus_grand


def entasser_vers_haut(tableau, i):
    """
    Restaure la propriété de max-tas en remontant depuis l'indice i (sift-up / percolate-up).

    Utile après un ajout en fin de tableau (voir T2 - insérer()).

    Paramètres :
        tableau (list) : le tableau représentant le tas
        i (int)         : indice du nœud à partir duquel on remonte

    Complexité : O(log n)
    """
    while i > 0 and tableau[parent(i)] < tableau[i]:
        p = parent(i)
        tableau[i], tableau[p] = tableau[p], tableau[i]
        i = p


def est_un_tas(tableau, taille=None):
    """
    Vérifie si tableau[0:taille] respecte la propriété de max-tas.
    Fonction utilitaire pratique pour les tests (T6 / P6) et le débogage.

    Retourne True si c'est un tas valide, False sinon.
    """
    if taille is None:
        taille = len(tableau)

    for i in range(taille):
        g = enfant_gauche(i)
        d = enfant_droit(i)
        if g < taille and tableau[g] > tableau[i]:
            return False
        if d < taille and tableau[d] > tableau[i]:
            return False
    return True


if __name__ == "__main__":
    # Démonstration de entasser() : ne restaure qu'un seul nœud.
    # Pour transformer un tableau quelconque en tas, utiliser
    # construire_tas() de build_heap.py (T3).

    # Exemple 1 : entasser sur un tableau déjà presque-tas
    #   [10, 4, 3, 5, 1] est un max-tas valide (racine = 10)
    #   On échange volontairement la racine pour simuler une extraction
    exemple = [4, 10, 3, 5, 1]
    print("Tableau de départ (racine dégradée) :", exemple)
    entasser(exemple, 0, len(exemple))  # restaure uniquement depuis la racine
    print("Après entasser(0) :", exemple)
    print("Est un tas ?", est_un_tas(exemple))
    print()

    # Exemple 2 : entasser_iteratif produit le même résultat
    exemple2 = [4, 10, 3, 5, 1]
    entasser_iteratif(exemple2, 0, len(exemple2))
    print("Version itérative :", exemple2)
    print("Est un tas ?", est_un_tas(exemple2))
