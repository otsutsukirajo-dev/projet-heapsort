"""
Tests unitaires pour T3 - construire_tas (P3)

Utilise pytest.
Lancement :
    pytest test_build_heap.py -v
"""

import pytest
from src.build_heap import construire_tas, entasser
from src.heap import est_un_tas as est_un_tas_valide  # alias pour compatibilité


# ---------------------------------------------------------------------
# Tests de construire_tas
# ---------------------------------------------------------------------

def test_tableau_vide():
    tableau = []
    resultat = construire_tas(tableau)
    assert resultat == []


def test_un_seul_element():
    tableau = [42]
    resultat = construire_tas(tableau)
    assert resultat == [42]


def test_deux_elements_deja_valides():
    tableau = [10, 5]
    resultat = construire_tas(tableau)
    assert est_un_tas_valide(resultat)


def test_deux_elements_a_inverser():
    tableau = [5, 10]
    resultat = construire_tas(tableau)
    assert est_un_tas_valide(resultat)
    assert resultat[0] == 10  # la racine doit être le max


def test_tableau_croissant():
    tableau = [1, 2, 3, 4, 5, 6, 7]
    resultat = construire_tas(tableau)
    assert est_un_tas_valide(resultat)
    assert resultat[0] == max(tableau)


def test_tableau_decroissant():
    tableau = [7, 6, 5, 4, 3, 2, 1]
    resultat = construire_tas(tableau)
    assert est_un_tas_valide(resultat)
    assert resultat[0] == max(tableau)


def test_tableau_avec_doublons():
    tableau = [4, 4, 4, 4, 4]
    resultat = construire_tas(tableau)
    assert est_un_tas_valide(resultat)


def test_tableau_avec_valeurs_negatives():
    tableau = [-1, -5, 3, 0, -2, 8]
    resultat = construire_tas(tableau)
    assert est_un_tas_valide(resultat)
    assert resultat[0] == max(tableau)


def test_grand_tableau_aleatoire():
    import random
    tableau = [random.randint(-1000, 1000) for _ in range(200)]
    resultat = construire_tas(tableau)
    assert est_un_tas_valide(resultat)
    assert resultat[0] == max(tableau)


def test_conserve_tous_les_elements():
    """construire_tas ne doit ni ajouter ni supprimer d'éléments,
    juste les réorganiser (même multiset avant/après)."""
    tableau = [3, 1, 4, 1, 5, 9, 2, 6]
    original_trie = sorted(tableau)
    resultat = construire_tas(tableau)
    assert sorted(resultat) == original_trie


def test_modifie_en_place():
    """construire_tas doit modifier le tableau en place (pas de copie)."""
    tableau = [3, 1, 4, 1, 5]
    resultat = construire_tas(tableau)
    assert resultat is tableau


# ---------------------------------------------------------------------
# Tests de entasser (dépendance T1, testée ici par ricochet)
# ---------------------------------------------------------------------

def test_entasser_ne_fait_rien_si_deja_valide():
    tableau = [10, 5, 6, 2, 3]
    entasser(tableau, 0, len(tableau))
    assert est_un_tas_valide(tableau)


def test_entasser_corrige_une_racine_invalide():
    # Ici, 1 est à la racine alors que ses enfants sont plus grands
    tableau = [1, 5, 6, 2, 3]
    entasser(tableau, 0, len(tableau))
    assert est_un_tas_valide(tableau)
    assert tableau[0] == 6


# ---------------------------------------------------------------------
# Test utilitaire : est_un_tas_valide lui-même
# ---------------------------------------------------------------------

def test_detecte_un_tas_invalide():
    tableau_invalide = [1, 10, 2]  # 1 (racine) < 10 (enfant) -> invalide
    assert not est_un_tas_valide(tableau_invalide)


def test_detecte_un_tas_valide():
    tableau_valide = [10, 5, 6, 2, 3]
    assert est_un_tas_valide(tableau_valide)


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))
