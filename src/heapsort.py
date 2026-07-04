"""
heapsort.py
Tâche T4 (P4) — Algorithme Heapsort complet

Dépend de :
    - T1 (heap.py)       : fonction entasser() (sift-down)
    - T3 (build_heap.py) : fonction construire_tas() (O(n))

Contrainte respectée : aucune bibliothèque de structure de données,
tri effectué entièrement en place sur le tableau Python (list).
"""

from heap import entasser
from build_heap import construire_tas


def heapsort(tableau):
    """
    Trie tableau en place, par ordre croissant, en utilisant l'algorithme Heapsort.

    Étapes :
        1. Construire un max-tas à partir du tableau (T3, O(n))
        2. Répéter n-1 fois :
             - échanger la racine (le plus grand élément restant) avec
               le dernier élément de la portion non triée
             - réduire la taille effective du tas de 1
             - ré-entasser depuis la racine pour restaurer la propriété de tas (T1)

    Paramètres :
        tableau (list) : tableau à trier (modifié en place)

    Complexité :
        - Temps  : O(n log n) dans tous les cas (meilleur, moyen, pire cas)
        - Espace : O(1) supplémentaire (tri en place), hors pile d'appel
                   de la récursion de entasser() qui est O(log n)

    Cas limites gérés : tableau vide, tableau à un seul élément,
    tableau déjà trié, tableau trié en ordre inverse, doublons.
    """
    n = len(tableau)

    if n <= 1:
        return  # rien à trier

    # Étape 1 : construire le max-tas initial (T3)
    construire_tas(tableau)

    # Étape 2 : extraire répétitivement le maximum et ré-entasser
    for taille_tas in range(n - 1, 0, -1):
        # Le plus grand élément du tas (racine) est mis à sa place finale
        tableau[0], tableau[taille_tas] = tableau[taille_tas], tableau[0]

        # Restaurer la propriété de tas sur la portion restante [0, taille_tas)
        entasser(tableau, 0, taille_tas)


if __name__ == "__main__":
    exemples = [
        [4, 10, 3, 5, 1, 8, 6],
        [],
        [42],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 3, 1, 1, 2, 2],
    ]

    for ex in exemples:
        original = ex[:]
        heapsort(ex)
        print(f"{original}  ->  {ex}")
