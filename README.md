# Projet Heapsort — Sujet 5

Implémentation complète du tri par tas (Heapsort), d'une file de priorité basée
sur un tas binaire, et comparaison de performance avec Quicksort et Tri fusion.

**Contrainte du projet :** aucune bibliothèque de structure de données externe
n'est utilisée — le tas, la file de priorité et les algorithmes de tri sont
codés entièrement à la main en Python standard.

---

## Équipe et répartition des tâches

| Tâche | Description | Responsable | Statut |
|-------|--------------|-------------|--------|
| T1 | Structure de tas & entassement (sift-down/sift-up) | Rajo | ✅ Terminé |
| T2 | Insertion & extraction (min/max) | Mampita | ✅ Terminé |
| T3 | Construction du tas en O(n) | Alex | ✅ Terminé (référence fournie, à valider par P3) |
| T4 | Algorithme Heapsort complet | Feno | ✅ Terminé |
| T5 | File de priorité + visualisation | Meddy| ✅ Terminé |
| T6 | Tests, benchmarks, rapport, vidéo | Mihajasoa | ✅ Terminé  |



---

## Structure du projet

```
projet-heapsort/
│
├── README.md                     # Ce document
├── GUIDE_DEMARRAGE.md            # Guide de démarrage détaillé
├── requirements.txt              # Dépendances Python (à générer avec pip freeze)
│
├── rapport/
│   └── rapport_final.pdf         # Livrable final (P6)
│
├── video/
│   └── demo.mp4                  # Capture vidéo de démonstration (P6)
│
├── src/
│   ├── heap.py                   # T1 - Structure de tas & entassement (P1)
│   ├── heap_ops.py               # T2 - Insertion & extraction (P2)
│   ├── build_heap.py             # T3 - Construction du tas O(n) (P3)
│   ├── heapsort.py               # T4 - Algorithme Heapsort (P4)
│   ├── priority_queue.py         # T5 - File de priorité (P5)
│   └── main.py                   # Point d'entrée, assemble tout
│
├── visualisation/
│   └── afficher_tas.py           # T5 - Affichage/visualisation du tas (P5)
│
├── tests/
│   ├── test_heap.py              # Tests unitaires T1/T2
│   ├── test_build_heap.py        # Tests unitaires T3
│   ├── test_heapsort.py          # Tests unitaires T4
│   └── test_priority_queue.py    # Tests unitaires T5
│
├── benchmarks/
│   └── comparaison_tris.py       # T6 - Heapsort vs Quicksort/Tri fusion (P6)
│
└── .gitignore
```

---

## Installation

### 1. Créer et activer l'environnement virtuel

```bash
python -m venv venv
```

**Windows (PowerShell) :**
```powershell
venv\Scripts\Activate.ps1
```
Si erreur de policy d'exécution :
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Linux / macOS :**
```bash
source venv/bin/activate
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

Dépendances principales :
- `matplotlib` — génération des graphiques de benchmark (T6)
- `pytest` (optionnel) — exécution des tests, alternative à `unittest`
- `graphviz` (optionnel) — export DOT pour la visualisation du tas (T5)

---

## Utilisation

### Trier un tableau avec Heapsort

```python
from src.heapsort import heapsort

tableau = [4, 10, 3, 5, 1, 8, 6]
heapsort(tableau)
print(tableau)  # [1, 3, 4, 5, 6, 8, 10]
```

### Lancer tous les tests unitaires

```bash
python -m unittest discover -s tests
```

ou, avec pytest :

```bash
pytest tests/
```

### Lancer les benchmarks comparatifs

```bash
python benchmarks/comparaison_tris.py
```

Génère un tableau récapitulatif dans la console et un graphique
`comparaison_tris.png` comparant Heapsort, Quicksort et Tri fusion sur
plusieurs tailles de tableaux.

---

## Contrat d'interfaces

Signatures communes convenues en réunion d'équipe (voir `GUIDE_DEMARRAGE.md`
section 4 pour le détail) :

```python
entasser(tableau, i, taille)          -> None        # T1
construire_tas(tableau)               -> None        # T3
heapsort(tableau)                     -> None        # T4
inserer(tas, valeur)                  -> None        # T2
extraire_min(tas)                     -> valeur      # T2
FilePriorite.ajouter(valeur)          -> None        # T5
FilePriorite.retirer()                -> valeur      # T5
afficher_tas(tas)                     -> None/texte  # T5
```

---

## Complexité des algorithmes

| Algorithme | Meilleur cas | Cas moyen | Pire cas | Espace |
|------------|:---:|:---:|:---:|:---:|
| Heapsort | O(n log n) | O(n log n) | O(n log n) | O(1) |
| Quicksort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Tri fusion | O(n log n) | O(n log n) | O(n log n) | O(n) |

Heapsort garantit O(n log n) dans **tous** les cas, contrairement à Quicksort
qui peut dégénérer en O(n²) sur des données défavorables (atténué ici par un
choix de pivot par médiane de trois). Il est aussi en place (O(1) d'espace
supplémentaire), contrairement au Tri fusion qui nécessite O(n).

---

## Workflow Git

1. Une branche par tâche : `feature/T1-heap`, `feature/T2-insertion`, etc.
2. Commits réguliers avec messages clairs sur sa branche
3. Pull request / merge vers `main` une fois la tâche testée individuellement
4. P6 vérifie l'intégration après chaque merge important

---

## Checklist avant rendu

- [x] T1 : structure de tas et entassement implémentée et testée
- [ ] T2 : insertion & extraction implémentées et testées
- [x] T3 : construction du tas en O(n) (référence fournie, à valider par P3)
- [x] T4 : Heapsort complet, testé sur tous les cas limites
- [ ] T5 : file de priorité + visualisation
- [x] T6 (partiel) : benchmarks comparatifs générés
- [ ] T6 : rapport PDF (noms des 6 étudiants + répartition des tâches)
- [ ] T6 : vidéo de démonstration
- [ ] Relecture croisée du code par l'équipe
