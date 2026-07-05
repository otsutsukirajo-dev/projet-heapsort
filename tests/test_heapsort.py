"""
test_heapsort.py
Tests unitaires pour la tâche T4 (P4) — heapsort.py

Lancer avec :
    python -m unittest test_heapsort.py
ou
    pytest test_heapsort.py
"""

import unittest
import random
from src.heapsort import heapsort


class TestHeapsort(unittest.TestCase):
    """Tests de l'algorithme Heapsort complet."""

    def test_tableau_vide(self):
        tableau = []
        heapsort(tableau)
        self.assertEqual(tableau, [])

    def test_un_seul_element(self):
        tableau = [42]
        heapsort(tableau)
        self.assertEqual(tableau, [42])

    def test_tableau_deja_trie(self):
        tableau = [1, 2, 3, 4, 5]
        heapsort(tableau)
        self.assertEqual(tableau, [1, 2, 3, 4, 5])

    def test_tableau_trie_ordre_inverse(self):
        tableau = [5, 4, 3, 2, 1]
        heapsort(tableau)
        self.assertEqual(tableau, [1, 2, 3, 4, 5])

    def test_tableau_aleatoire(self):
        tableau = [4, 10, 3, 5, 1, 8, 6]
        heapsort(tableau)
        self.assertEqual(tableau, sorted([4, 10, 3, 5, 1, 8, 6]))

    def test_avec_doublons(self):
        tableau = [3, 3, 1, 1, 2, 2, 3, 1]
        heapsort(tableau)
        self.assertEqual(tableau, [1, 1, 1, 2, 2, 3, 3, 3])

    def test_tous_elements_identiques(self):
        tableau = [7, 7, 7, 7, 7]
        heapsort(tableau)
        self.assertEqual(tableau, [7, 7, 7, 7, 7])

    def test_nombres_negatifs(self):
        tableau = [-5, 3, -1, 0, 8, -10]
        heapsort(tableau)
        self.assertEqual(tableau, [-10, -5, -1, 0, 3, 8])

    def test_deux_elements(self):
        self.assertEqualApresTri([2, 1], [1, 2])
        self.assertEqualApresTri([1, 2], [1, 2])

    def assertEqualApresTri(self, entree, attendu):
        heapsort(entree)
        self.assertEqual(entree, attendu)

    def test_grand_tableau_aleatoire(self):
        """Test de robustesse sur un grand tableau généré aléatoirement."""
        random.seed(42)  # reproductibilité
        tableau = [random.randint(-1000, 1000) for _ in range(1000)]
        resultat_attendu = sorted(tableau)
        heapsort(tableau)
        self.assertEqual(tableau, resultat_attendu)

    def test_tri_stable_sur_le_contenu(self):
        """Vérifie que heapsort ne perd ni n'ajoute d'éléments (multiset préservé)."""
        tableau = [5, 3, 8, 3, 1, 5, 9, 1]
        original_trie = sorted(tableau)
        heapsort(tableau)
        self.assertEqual(tableau, original_trie)
        self.assertEqual(len(tableau), 8)


if __name__ == "__main__":
    unittest.main()
