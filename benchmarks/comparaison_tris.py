"""
comparaison_tris.py
Tâche T6 (P6) — Benchmarks comparatifs : Heapsort vs Quicksort vs Tri fusion

Compare les temps d'exécution des trois algorithmes sur des tableaux
aléatoires de tailles croissantes, puis génère un graphique et un tableau
récapitulatif.

Dépend de :
    - heapsort.py (T4)

Quicksort et Tri fusion sont implémentés ici à la main (aucune bibliothèque
de tri utilisée), conformément à la contrainte du projet.

Lancer avec :
    python comparaison_tris.py
"""

import os
import random
import sys
import time
import copy

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from src.heapsort import heapsort


# ---------------------------------------------------------------------------
# Implémentations de référence pour la comparaison (codées à la main)
# ---------------------------------------------------------------------------

def quicksort(tableau):
    """
    Trie tableau en place par ordre croissant avec l'algorithme Quicksort
    (pivot = élément médian de [premier, milieu, dernier], partition de Lomuto).
    """
    _quicksort_recursif(tableau, 0, len(tableau) - 1)


def _quicksort_recursif(tableau, bas, haut):
    if bas < haut:
        indice_pivot = _partitionner(tableau, bas, haut)
        _quicksort_recursif(tableau, bas, indice_pivot - 1)
        _quicksort_recursif(tableau, indice_pivot + 1, haut)


def _partitionner(tableau, bas, haut):
    # Choix du pivot par médiane de trois, pour limiter les pires cas
    # sur des tableaux déjà triés ou triés en ordre inverse.
    milieu = (bas + haut) // 2
    candidats = [(tableau[bas], bas), (tableau[milieu], milieu), (tableau[haut], haut)]
    candidats.sort(key=lambda c: c[0])
    _, indice_median = candidats[1]
    tableau[indice_median], tableau[haut] = tableau[haut], tableau[indice_median]

    pivot = tableau[haut]
    i = bas - 1
    for j in range(bas, haut):
        if tableau[j] <= pivot:
            i += 1
            tableau[i], tableau[j] = tableau[j], tableau[i]
    tableau[i + 1], tableau[haut] = tableau[haut], tableau[i + 1]
    return i + 1


def tri_fusion(tableau):
    """
    Trie tableau par ordre croissant avec l'algorithme Tri fusion (Merge Sort).
    Retourne un nouveau tableau trié (non en place, par nature de l'algorithme).
    """
    if len(tableau) <= 1:
        return tableau[:]

    milieu = len(tableau) // 2
    gauche = tri_fusion(tableau[:milieu])
    droite = tri_fusion(tableau[milieu:])
    return _fusionner(gauche, droite)


def _fusionner(gauche, droite):
    resultat = []
    i = j = 0
    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1
    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])
    return resultat


# ---------------------------------------------------------------------------
# Mesure de performance
# ---------------------------------------------------------------------------

def mesurer_temps(fonction_tri, tableau, en_place=True):
    """
    Mesure le temps d'exécution d'une fonction de tri sur une copie du tableau.

    Paramètres :
        fonction_tri : fonction de tri à mesurer
        tableau      : tableau d'entrée (non modifié, on travaille sur une copie)
        en_place     : True si la fonction trie en place (retour None),
                       False si elle retourne un nouveau tableau (ex. tri_fusion)

    Retourne : temps écoulé en secondes (float)
    """
    copie = copy.copy(tableau)
    debut = time.perf_counter()
    if en_place:
        fonction_tri(copie)
    else:
        copie = fonction_tri(copie)
    fin = time.perf_counter()
    return fin - debut


def generer_tableau_aleatoire(taille, graine=None):
    """Génère un tableau de `taille` entiers aléatoires entre -10000 et 10000."""
    rng = random.Random(graine)
    return [rng.randint(-10000, 10000) for _ in range(taille)]


# ---------------------------------------------------------------------------
# Benchmark principal
# ---------------------------------------------------------------------------

TAILLES = [100, 500, 1000, 2000, 5000, 10000]
NB_REPETITIONS = 3  # moyenne sur plusieurs essais pour limiter le bruit de mesure


def executer_benchmark(tailles=TAILLES, nb_repetitions=NB_REPETITIONS):
    """
    Exécute le benchmark complet pour chaque taille et chaque algorithme.

    Retourne un dictionnaire :
        {
            "heapsort":  [temps_taille_1, temps_taille_2, ...],
            "quicksort": [...],
            "tri_fusion": [...],
        }
    """
    resultats = {"heapsort": [], "quicksort": [], "tri_fusion": []}

    algorithmes = [
        ("heapsort", heapsort, True),
        ("quicksort", quicksort, True),
        ("tri_fusion", tri_fusion, False),
    ]

    for taille in tailles:
        print(f"Taille {taille}...")
        tableau_base = generer_tableau_aleatoire(taille, graine=42)

        for nom, fonction, en_place in algorithmes:
            temps_mesures = [
                mesurer_temps(fonction, tableau_base, en_place=en_place)
                for _ in range(nb_repetitions)
            ]
            temps_moyen = sum(temps_mesures) / len(temps_mesures)
            resultats[nom].append(temps_moyen)
            print(f"  {nom:12s} : {temps_moyen:.6f} s (moyenne sur {nb_repetitions} essais)")

    return resultats


def afficher_tableau_resultats(tailles, resultats):
    """Affiche un tableau texte récapitulatif des résultats."""
    print("\n" + "=" * 60)
    print(f"{'Taille':>10} | {'Heapsort':>12} | {'Quicksort':>12} | {'Tri fusion':>12}")
    print("-" * 60)
    for idx, taille in enumerate(tailles):
        print(
            f"{taille:>10} | "
            f"{resultats['heapsort'][idx]:>10.6f}s | "
            f"{resultats['quicksort'][idx]:>10.6f}s | "
            f"{resultats['tri_fusion'][idx]:>10.6f}s"
        )
    print("=" * 60)


def generer_graphique(tailles, resultats, chemin_sortie="comparaison_tris.png"):
    """
    Génère un graphique comparatif (temps vs taille) et le sauvegarde en PNG.
    Nécessite matplotlib (pip install matplotlib).
    """
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print(
            "\n[Attention] matplotlib n'est pas installé — graphique non généré.\n"
            "Installez-le avec : pip install matplotlib"
        )
        return

    plt.figure(figsize=(9, 6))
    plt.plot(tailles, resultats["heapsort"], marker="o", label="Heapsort")
    plt.plot(tailles, resultats["quicksort"], marker="s", label="Quicksort")
    plt.plot(tailles, resultats["tri_fusion"], marker="^", label="Tri fusion")

    plt.xlabel("Taille du tableau (n)")
    plt.ylabel("Temps d'exécution (secondes)")
    plt.title("Comparaison des temps d'exécution : Heapsort vs Quicksort vs Tri fusion")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(chemin_sortie, dpi=150)
    print(f"\nGraphique sauvegardé : {chemin_sortie}")


if __name__ == "__main__":
    resultats = executer_benchmark()
    afficher_tableau_resultats(TAILLES, resultats)
    generer_graphique(TAILLES, resultats)