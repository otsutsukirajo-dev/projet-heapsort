"""
Module src/heap_ops.py
Géré par : P2 (Tâche T2)
"""

try:
    from .heap import entasser
except ImportError:  # pragma: no cover - fallback when executed as a top-level module
    from heap import entasser

def sift_up(tas, i):
    """
    Restaure la propriété de Max-Tas vers le haut depuis l'indice i.
    Placer la plus grande valeur vers la racine.
    """
    parent = (i - 1) // 2
    while i > 0 and tas[i] > tas[parent]:
        tas[i], tas[parent] = tas[parent], tas[i]
        i = parent
        parent = (i - 1) // 2


def inserer(tas, valeur):
    """
    Insère une nouvelle valeur dans le tas.
    Complexité : O(log n)
    """
    tas.append(valeur)
    sift_up(tas, len(tas) - 1)


def extraire_max(tas):
    """
    Extrait et renvoie la valeur maximale (la racine du tas).
    Complexité : O(log n)
    """
    if not tas:
        raise IndexError("Impossible d'extraire d'un tas vide.")

    if len(tas) == 1:
        return tas.pop()

    racine_max = tas[0]
    tas[0] = tas.pop()
    entasser(tas, 0, len(tas))

    return racine_max


if __name__ == "__main__":
    # --- Démo manuelle des opérations sur le tas ---
    tas = []
    for v in [3, 1, 4, 1, 5, 9, 2, 6]:
        inserer(tas, v)
        print(f"inserer({v:2d}) -> tas: {tas}")

    print()
    while tas:
        print(f"extraire_max() -> {extraire_max(tas)}, tas restant: {tas}")