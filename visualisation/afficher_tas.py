"""
afficher_tas.py
Tâche T5 (P5 - Meddy) — Visualisation du tas

Conforme au contrat d'interfaces du projet :
    afficher_tas(tas) -> void/texte

Deux modes proposés :
1. affichage texte indenté (aucune dépendance, marche partout)
2. export au format DOT (Graphviz) pour générer une image de l'arbre
   avec la commande : dot -Tpng tas.dot -o tas.png
"""


def afficher_tas(tas, indice=0, prefixe="", est_dernier=True, racine=True):
    """Affiche le tas sous forme d'arbre indenté dans le terminal.

    Exemple pour [1, 3, 2, 7, 5] :
        1
        ├── 3
        │   └── 7
        └── 2
            └── 5

    Paramètres :
        tas (list) : tableau représentant le tas
    """
    if not tas:
        print("(tas vide)")
        return

    if racine:
        print(tas[indice])
    else:
        branche = "└── " if est_dernier else "├── "
        print(prefixe + branche + str(tas[indice]))

    gauche = 2 * indice + 1
    droite = 2 * indice + 2
    enfants = [e for e in (gauche, droite) if e < len(tas)]

    nouveau_prefixe = prefixe if racine else prefixe + ("    " if est_dernier else "│   ")

    for i, enfant in enumerate(enfants):
        dernier = (i == len(enfants) - 1)
        afficher_tas(tas, enfant, nouveau_prefixe, dernier, racine=False)


def exporter_dot(tas, nom_fichier="tas.dot"):
    """Génère un fichier .dot représentant le tas, exploitable avec Graphviz.

    Utilisation ensuite (nécessite Graphviz installé sur la machine) :
        dot -Tpng tas.dot -o tas.png
    """
    lignes = ["digraph Tas {", "    node [shape=circle, style=filled, fillcolor=lightblue];"]

    for i, valeur in enumerate(tas):
        lignes.append(f'    n{i} [label="{valeur}"];')
        gauche = 2 * i + 1
        droite = 2 * i + 2
        if gauche < len(tas):
            lignes.append(f"    n{i} -> n{gauche};")
        if droite < len(tas):
            lignes.append(f"    n{i} -> n{droite};")

    lignes.append("}")

    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write("\n".join(lignes))

    print(f"Fichier Graphviz généré : {nom_fichier}")


if __name__ == "__main__":
    exemple = [1, 3, 2, 7, 5, 8, 6, 9]
    print("Affichage texte :")
    afficher_tas(exemple)

    print()
    exporter_dot(exemple, "tas_demo.dot")
