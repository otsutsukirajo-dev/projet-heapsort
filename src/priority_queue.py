"""
priority_queue.py
Tâche T5 (P5 - Meddy) — File de priorité basée sur un tas

Conforme au contrat d'interfaces du projet :
    FilePriorite.ajouter(valeur)   -> void
    FilePriorite.retirer()         -> valeur

Cette implémentation est une file de priorité MIN (le plus petit élément
sort en premier). Le tas est maintenu comme une liste interne classique,
avec les opérations standard de remontée (sift-up) et descente (sift-down).

Remarque équipe :
Si T2 (heap_ops.py, inserer/extraire_min) est terminé et qu'on préfère
factoriser le code commun, on peut remplacer _remonter/_descendre par des
appels aux fonctions de heap_ops.py — la classe garde la même interface
publique (ajouter/retirer), donc ça n'impacte personne d'autre.
"""


class FilePriorite:
    """File de priorité (min-tas) codée à la main, sans bibliothèque."""

    def __init__(self):
        self._tas = []

    def est_vide(self):
        """Renvoie True si la file ne contient aucun élément."""
        return len(self._tas) == 0

    def __len__(self):
        return len(self._tas)

    def ajouter(self, valeur):
        """Insère `valeur` dans la file de priorité. Complexité O(log n)."""
        self._tas.append(valeur)
        self._remonter(len(self._tas) - 1)

    def retirer(self):
        """Retire et renvoie l'élément de plus petite valeur. O(log n).

        Lève IndexError si la file est vide.
        """
        if self.est_vide():
            raise IndexError("retirer() sur une FilePriorite vide")

        minimum = self._tas[0]
        dernier = self._tas.pop()

        if self._tas:
            self._tas[0] = dernier
            self._descendre(0)

        return minimum

    def regarder_min(self):
        """Renvoie le plus petit élément sans le retirer."""
        if self.est_vide():
            raise IndexError("regarder_min() sur une FilePriorite vide")
        return self._tas[0]

    def tas_interne(self):
        """Renvoie une copie du tableau interne (utile pour la visualisation)."""
        return list(self._tas)

    # ------------------------------------------------------------------
    # Opérations internes sur le tas
    # ------------------------------------------------------------------

    def _remonter(self, i):
        """Sift-up : remonte l'élément d'indice i tant qu'il est plus petit
        que son parent."""
        while i > 0:
            parent = (i - 1) // 2
            if self._tas[i] < self._tas[parent]:
                self._tas[i], self._tas[parent] = self._tas[parent], self._tas[i]
                i = parent
            else:
                break

    def _descendre(self, i):
        """Sift-down : descend l'élément d'indice i tant qu'il est plus grand
        qu'un de ses enfants."""
        n = len(self._tas)
        while True:
            gauche = 2 * i + 1
            droite = 2 * i + 2
            plus_petit = i

            if gauche < n and self._tas[gauche] < self._tas[plus_petit]:
                plus_petit = gauche
            if droite < n and self._tas[droite] < self._tas[plus_petit]:
                plus_petit = droite

            if plus_petit == i:
                break

            self._tas[i], self._tas[plus_petit] = self._tas[plus_petit], self._tas[i]
            i = plus_petit


if __name__ == "__main__":
    # Petite démo manuelle
    fp = FilePriorite()
    for v in [5, 3, 8, 1, 9, 2, 7]:
        fp.ajouter(v)

    print("Tas interne :", fp.tas_interne())

    print("Extraction dans l'ordre :", end=" ")
    while not fp.est_vide():
        print(fp.retirer(), end=" ")
    print()
