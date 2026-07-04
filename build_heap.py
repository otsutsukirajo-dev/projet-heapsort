"""
build_heap.py
Tâche T3 (P3) — Construction du tas en O(n)

NOTE POUR L'ÉQUIPE : ce fichier est une implémentation de référence fournie
temporairement pour permettre à P4 (T4) de tester heapsort.py sans attendre.
P3 doit relire/valider (ou remplacer) ce fichier — tant que la signature
construire_tas(tableau) est respectée, l'intégration avec T4 reste inchangée.
"""

from heap import entasser


def construire_tas(tableau):
    """
    Transforme un tableau quelconque en max-tas, en place, en O(n).

    Principe : on applique entasser() (sift-down) sur tous les nœuds internes,
    en partant du dernier nœud non-feuille et en remontant vers la racine.
    Le dernier nœud non-feuille se trouve à l'indice (n // 2) - 1.

    Paramètres :
        tableau (list) : tableau à transformer en tas (modifié en place)

    Complexité : O(n) (et non O(n log n), grâce à l'analyse amortie du coût
    de entasser() sur les niveaux inférieurs de l'arbre, qui sont bien plus
    nombreux et bien moins coûteux à corriger)
    """
    n = len(tableau)
    dernier_non_feuille = n // 2 - 1

    for i in range(dernier_non_feuille, -1, -1):
        entasser(tableau, i, n)


if __name__ == "__main__":
    from heap import est_un_tas

    exemple = [4, 10, 3, 5, 1, 8, 6]
    print("Avant construire_tas :", exemple)
    construire_tas(exemple)
    print("Après construire_tas :", exemple)
    print("Est un tas ?", est_un_tas(exemple))
