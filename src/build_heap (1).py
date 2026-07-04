"""
T3 - Construction du tas (build-heap en O(n))
Responsable : P3
Livrable    : construire_tas(tableau)
Dépend de   : T1 (fonction entasser)

Ce fichier est autonome : il contient une implémentation de entasser()
(normalement fournie par P1 dans src/heap.py) uniquement pour que
construire_tas() soit testable indépendamment. En intégration réelle,
il faudra remplacer cette copie par un import :

    from heap import entasser
"""


def entasser(tableau, i, taille):
    """
    (T1 - dépendance) Restaure la propriété de tas (max-tas) à partir
    de l'indice i, en supposant que les sous-arbres de i sont déjà
    des tas valides.

    tableau : liste représentant le tas
    i       : indice à partir duquel on restaure la propriété de tas
    taille  : taille "active" du tas (utile pour heapsort plus tard)
    """
    gauche = 2 * i + 1
    droite = 2 * i + 2
    plus_grand = i

    if gauche < taille and tableau[gauche] > tableau[plus_grand]:
        plus_grand = gauche

    if droite < taille and tableau[droite] > tableau[plus_grand]:
        plus_grand = droite

    if plus_grand != i:
        tableau[i], tableau[plus_grand] = tableau[plus_grand], tableau[i]
        # On continue à "descendre" là où on a fait l'échange
        entasser(tableau, plus_grand, taille)


def construire_tas(tableau):
    """
    T3 - Transforme un tableau quelconque en tas (max-tas) en O(n).

    Principe :
    Les feuilles (indices >= n//2) sont déjà des tas valides à elles
    seules (un seul élément). On part donc du dernier nœud interne
    (indice n//2 - 1) et on remonte vers la racine (indice 0) en
    appelant entasser() à chaque étape.

    tableau : liste à transformer en tas (modifiée en place)
    retour  : le même tableau, désormais organisé en tas
    """
    n = len(tableau)

    # Dernier nœud interne (parent de la dernière feuille)
    dernier_noeud_interne = n // 2 - 1

    for i in range(dernier_noeud_interne, -1, -1):
        entasser(tableau, i, n)

    return tableau


def est_un_tas_valide(tableau):
    """
    Fonction utilitaire (pour les tests) : vérifie que la propriété
    de max-tas est respectée pour tout le tableau.
    """
    n = len(tableau)
    for i in range(n):
        gauche = 2 * i + 1
        droite = 2 * i + 2
        if gauche < n and tableau[i] < tableau[gauche]:
            return False
        if droite < n and tableau[i] < tableau[droite]:
            return False
    return True


if __name__ == "__main__":
    # --- Petite démo / test manuel de construire_tas ---
    exemples = [
        [4, 10, 3, 5, 1],
        [1, 2, 3, 4, 5, 6, 7],
        [9, 5, 6, 2, 3],
        [],
        [42],
    ]

    for tableau in exemples:
        original = tableau.copy()
        construire_tas(tableau)
        valide = est_un_tas_valide(tableau)
        print(f"Original  : {original}")
        print(f"Tas obtenu: {tableau}")
        print(f"Valide    : {valide}")
        print("-" * 40)
