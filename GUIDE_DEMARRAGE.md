# Guide de Démarrage — Projet Sujet 5 : Tri par Tas (Heapsort)

## 1. Avant de commencer

### Prérequis
- Choisir le langage de l'équipe (ex. Python, C, C++, Java...)
- Créer un dépôt Git partagé (GitHub/GitLab) — **fortement recommandé** pour un travail à 6
- Installer l'environnement de dev + un outil de test (ex. `unittest`/`pytest` en Python, ou un framework de tests unitaires simple selon le langage)
- Rappel contrainte : **aucune bibliothèque de structure de données** — tout (tas, file de priorité) doit être codé à la main

### Première réunion d'équipe (à faire ensemble)
1. Choisir le langage définitivement
2. Définir les signatures des fonctions communes (voir section 4) — **étape cruciale** pour que les 6 personnes puissent travailler en parallèle sans tout casser
3. Créer le dépôt Git et la structure de dossier (section 2)
4. Chacun clone le dépôt et fait un premier commit vide dans son fichier assigné

---

## 2. Structure du dossier du projet

```
projet-heapsort/+

│
├── README.md                     # Présentation générale du projet
├── GUIDE_DEMARRAGE.md
├── rapport/
│   └── rapport_final.pdf          # Livrable final (P6)
│
├── video/
│   └── demo.mp4                   # Capture vidéo de démonstration (P6)
│
├── src/
│   ├── heap.*                     # T1 - Structure de tas & entassement (P1)
│   ├── heap_ops.*                 # T2 - Insertion & extraction (P2)
│   ├── build_heap.*               # T3 - Construction du tas O(n) (P3)
│   ├── heapsort.*                 # T4 - Algorithme Heapsort (P4)
│   ├── priority_queue.*           # T5 - File de priorité (P5)
│   └── main.*                     # Point d'entrée, assemble tout
│
├── visualisation/
│   └── afficher_tas.*             # T5 - Affichage/visualisation du tas (P5)
│
├── tests/
│   ├── test_heap.*                # Tests unitaires T1/T2
│   ├── test_build_heap.*          # Tests unitaires T3
│   ├── test_heapsort.*            # Tests unitaires T4
│   └── test_priority_queue.*      # Tests unitaires T5
│
├── benchmarks/
│   └── comparaison_tris.*         # T6 - Heapsort vs Quicksort/Tri fusion (P6)
│
└── .gitignore
``` 

---

## 3. Répartition des 6 tâches

| # | Tâche | Responsable | Fichiers principaux | Dépend de |
|---|-------|-------------|---------------------|-----------|
| **T1** | Structure de tas & entassement (`sift-down`/`sift-up`) | **P1** | `src/heap.*` | Aucune (démarre en premier) |
| **T2** | Insertion & extraction (min/max) | **P2** | `src/heap_ops.*` | T1 (utilise `entasser`) |
| **T3** | Construction du tas (build-heap en O(n)) | **P3** | `src/build_heap.*` | T1 |
| **T4** | Algorithme Heapsort complet | **P4** | `src/heapsort.*` | T1, T3 |
| **T5** | File de priorité + visualisation | **P5** | `src/priority_queue.*`, `visualisation/afficher_tas.*` | T1, T2 |
| **T6** | Tests, benchmarks, rapport, vidéo | **P6** | `tests/`, `benchmarks/`, `rapport/`, `video/` | Toutes les autres (rôle transversal, démarre dès le début pour préparer les tests) |

### Détail des livrables par personne
- **P1** : fonction `entasser(tableau, i, taille)` qui restaure la propriété de tas à partir de l'indice `i`
- **P2** : `inserer(valeur)`, `extraire_min()` ou `extraire_max()`
- **P3** : `construire_tas(tableau)` — transforme un tableau quelconque en tas en O(n)
- **P4** : `heapsort(tableau)` — tri en place complet, utilisant T1 et T3
- **P5** : classe `FilePriorite` (basée sur le tas) + fonction d'affichage (texte indenté ou export Graphviz/DOT)
- **P6** : suite de tests, script de comparaison de performance (temps d'exécution Heapsort vs Quicksort/Tri fusion sur différentes tailles), rédaction du rapport PDF, organisation de la capture vidéo

---

## 4. Contrat d'interfaces (à valider en réunion avant de coder)

Exemple générique
```
entasser(tableau, i, taille)          -> void        (T1)
construire_tas(tableau)               -> void        (T3)
heapsort(tableau)                     -> void        (T4)
inserer(tas, valeur)                  -> void        (T2)
extraire_min(tas)                     -> valeur      (T2)
FilePriorite.ajouter(valeur)          -> void        (T5)
FilePriorite.retirer()                -> valeur      (T5)
afficher_tas(tas)                     -> void/texte  (T5)
```


## 5. Workflow Git recommandé

1. Une branche par tâche : `feature/T1-heap`, `feature/T2-insertion`, etc.
2. Chaque personne travaille sur sa branche, commits réguliers avec messages clairs
3. Pull request / merge vers `main` une fois la tâche testée individuellement
4. **P6** vérifie l'intégration après chaque merge important
5. Éviter de travailler tous en même temps sur `main` directement

---

## 6. Planning suggéré (4 semaines)

| Semaine | Actions |
|---------|---------|
| **1** | Réunion de démarrage, contrat d'interfaces, T1 (P1) + début T2 (P2) |
| **2** | T2 terminé, T3 (P3) et début T4 (P4). P6 commence les tests de T1/T2 |
| **3** | T4 terminé, T5 (P5) en parallèle. P6 continue tests + démarre benchmarks |
| **4** | Intégration finale, T6 (P6) : benchmarks complets, rapport, vidéo, relecture croisée |

---

## 7. Checklist finale avant rendu

- [ ] Toutes les fonctions listées dans le contrat d'interfaces sont implémentées et testées
- [ ] Heapsort fonctionne correctement sur : tableau aléatoire, déjà trié, trié en ordre inverse, tableau vide, un seul élément
- [ ] File de priorité fonctionnelle et testée
- [ ] Visualisation du tas lisible
- [ ] Benchmarks comparatifs présents (graphique ou tableau de résultats)
- [ ] Rapport PDF : noms des 6 étudiants + répartition des tâches clairement indiquée
- [ ] Vidéo de démonstration enregistrée (Vokoscreen/Bandicam) montrant le programme en fonctionnement
- [ ] Code source commenté et propre dans le dépôt
