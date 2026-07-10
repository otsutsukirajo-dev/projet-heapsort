"""
T3 - Construction du tas (build-heap en O(n))
Responsable : P3
Livrable    : construire_tas(tableau)
Dépend de   : T1 (fonctions entasser et est_un_tas, heap.py)

Ce module importe entasser() et est_un_tas() depuis heap.py (T1).
Il n'y a pas de copie locale : toute modification de heap.py est
automatiquement prise en compte ici.
"""

try:
    from .heap import entasser, est_un_tas
except ImportError:  # pragma: no cover - fallback when executed as a top-level module
    from heap import entasser, est_un_tas




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




if __name__ == "__main__":
    # --- Petite démo / test manuel de construire_tas ---
    exemples = [
        [4, 10, 3, 5, 1],
        [1, 2, 3, 4, 5, 6, 7],
        [9, 5, 6, 2, 3],
        [],
        [42],
    ]

    for exemple in exemples:
        original = exemple.copy()
        construire_tas(exemple)
        valide = est_un_tas(exemple)   # fournie par heap.py (T1)
        print(f"Original  : {original}")
        print(f"Tas obtenu: {exemple}")
        print(f"Valide    : {valide}")
        print("-" * 40)
