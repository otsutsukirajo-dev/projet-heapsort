"""
Module src/heap_ops.py
Géré par : P2 (Tâche T2)
"""

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
    
    # Appel de la fonction de P1 pour rétablir le tas vers le bas
    from heap import entasser
    entasser(tas, 0, len(tas))
    
    return racine_max