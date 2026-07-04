"""
test_heap.py
Tests unitaires pour la tâche T1 (P1) — heap.py

Lancer avec :
    python -m unittest test_heap.py
ou
    pytest test_heap.py
"""

import unittest
from src.heap import (
    parent,
    enfant_gauche,
    enfant_droit,
    entasser,
    entasser_iteratif,
    entasser_vers_haut,
    est_un_tas,
)


class TestIndices(unittest.TestCase):
    """Tests des fonctions utilitaires d'indexation."""

    def test_parent(self):
        self.assertEqual(parent(1), 0)
        self.assertEqual(parent(2), 0)
        self.assertEqual(parent(3), 1)
        self.assertEqual(parent(4), 1)
        self.assertEqual(parent(6), 2)

    def test_enfant_gauche(self):
        self.assertEqual(enfant_gauche(0), 1)
        self.assertEqual(enfant_gauche(1), 3)
        self.assertEqual(enfant_gauche(2), 5)

    def test_enfant_droit(self):
        self.assertEqual(enfant_droit(0), 2)
        self.assertEqual(enfant_droit(1), 4)
        self.assertEqual(enfant_droit(2), 6)


class TestEntasser(unittest.TestCase):
    """Tests de la fonction entasser() (sift-down)."""

    def test_tableau_deja_tas(self):
        tableau = [10, 5, 3, 1, 4]
        entasser(tableau, 0, len(tableau))
        self.assertTrue(est_un_tas(tableau))
        self.assertEqual(tableau, [10, 5, 3, 1, 4])

    def test_racine_trop_petite(self):
        tableau = [1, 10, 5, 4, 3]
        entasser(tableau, 0, len(tableau))
        self.assertTrue(est_un_tas(tableau))
        self.assertEqual(tableau[0], 10)

    def test_entasser_sous_arbre(self):
        # Le nœud d'indice 1 viole la propriété par rapport à ses enfants
        tableau = [10, 1, 8, 5, 4]
        entasser(tableau, 1, len(tableau))
        self.assertEqual(tableau[1], 5)

    def test_taille_reduite(self):
        # Simule le comportement pendant heapsort : on n'entasse
        # que sur une partie du tableau (taille < len(tableau))
        tableau = [1, 5, 3, 10, 9]
        entasser(tableau, 0, 3)  # ignore les indices 3 et 4
        self.assertTrue(est_un_tas(tableau, taille=3))

    def test_element_unique(self):
        tableau = [42]
        entasser(tableau, 0, 1)
        self.assertEqual(tableau, [42])

    def test_tableau_vide(self):
        tableau = []
        # Ne doit pas lever d'exception
        entasser(tableau, 0, 0)
        self.assertEqual(tableau, [])

    def test_version_iterative_equivalente(self):
        base = [1, 10, 5, 4, 3]
        t1 = base[:]
        t2 = base[:]
        entasser(t1, 0, len(t1))
        entasser_iteratif(t2, 0, len(t2))
        self.assertEqual(t1, t2)


class TestEntasserVersHaut(unittest.TestCase):
    """Tests de la fonction entasser_vers_haut() (sift-up)."""

    def test_remontee_simple(self):
        # Tas valide [10, 5, 3] auquel on ajoute 20 en fin de tableau
        tableau = [10, 5, 3, 20]
        entasser_vers_haut(tableau, 3)
        self.assertTrue(est_un_tas(tableau))
        self.assertEqual(tableau[0], 20)

    def test_pas_de_remontee_necessaire(self):
        tableau = [10, 5, 3, 1]
        entasser_vers_haut(tableau, 3)
        self.assertEqual(tableau, [10, 5, 3, 1])

    def test_racine_ne_bouge_pas(self):
        tableau = [10]
        entasser_vers_haut(tableau, 0)
        self.assertEqual(tableau, [10])


class TestEstUnTas(unittest.TestCase):
    """Tests de la fonction utilitaire est_un_tas()."""

    def test_tas_valide(self):
        self.assertTrue(est_un_tas([10, 8, 9, 5, 4, 7]))

    def test_tas_invalide(self):
        self.assertFalse(est_un_tas([5, 10, 9, 1, 2, 3]))

    def test_tableau_vide_est_un_tas(self):
        self.assertTrue(est_un_tas([]))

    def test_element_unique_est_un_tas(self):
        self.assertTrue(est_un_tas([1]))


if __name__ == "__main__":
    unittest.main()
