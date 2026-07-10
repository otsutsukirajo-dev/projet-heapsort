"""
priority_queue.py
Tâche T5 (P5 - Meddy) — File de priorité basée sur un tas

Conforme au contrat d'interfaces du projet :
    FilePriorite.ajouter(valeur)   -> void
    FilePriorite.retirer()         -> valeur  (retire le MINIMUM)
    FilePriorite.regarder_min()    -> valeur  (consulte sans retirer)

⚠️  CONVENTION DE TAS : ce module utilise un MIN-TAS (le plus petit
    élément sort en premier), à l'inverse de heap.py et heap_ops.py
    qui implémentent un MAX-TAS.
    - _remonter() échange si enfant < parent  (montée du petit)
    - _descendre() échange avec le plus petit enfant  (descente du grand)
    Ce choix est intentionnel : une file de priorité sert typiquement
    à extraire le plus urgent (le plus petit), pas le plus grand.

Remarque équipe :
Si T2 (heap_ops.py, inserer/extraire_max) est terminé et qu'on préfère
factoriser le code commun, les opérations internes _remonter/_descendre
peuvent rester dans cette classe (elles sont MIN alors que heap_ops est MAX).
L'interface publique (ajouter/retirer) reste inchangée pour les autres.
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
